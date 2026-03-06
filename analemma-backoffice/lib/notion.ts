const NOTION_TOKEN = process.env.NOTION_TOKEN!;
const TICKET_BOARD_ID = process.env.TICKET_BOARD_ID!;
const ACTIVITY_LOG_ID = process.env.ACTIVITY_LOG_ID!;

const headers = {
  Authorization: `Bearer ${NOTION_TOKEN}`,
  "Notion-Version": "2022-06-28",
  "Content-Type": "application/json",
};

export interface Ticket {
  id: string;
  task: string;
  status: string;
  priority: string;
  assignedTo: string;
  type: string;
  raisedBy: string;
  dueDate: string | null;
  linearId: string;
  notes: string;
}

export interface ActivityEntry {
  id: string;
  activity: string;
  agent: string;
  type: string;
  ticketRef: string;
  ticket: string;
  details: string;
  timestamp: string | null;
  modelUsed: string;
}

/* eslint-disable @typescript-eslint/no-explicit-any */
function getSelectValue(prop: any): string {
  return prop?.select?.name || "";
}

function getTitleValue(prop: any): string {
  return prop?.title?.[0]?.text?.content || "";
}

function getRichTextValue(prop: any): string {
  return prop?.rich_text?.[0]?.text?.content || "";
}

function getDateValue(prop: any): string | null {
  return prop?.date?.start || null;
}

export async function getTickets(): Promise<Ticket[]> {
  const res = await fetch(
    `https://api.notion.com/v1/databases/${TICKET_BOARD_ID}/query`,
    {
      method: "POST",
      headers,
      body: JSON.stringify({
        sorts: [
          { property: "Status", direction: "ascending" },
          { property: "Priority", direction: "ascending" },
        ],
        page_size: 100,
      }),
      next: { revalidate: 30 },
    }
  );

  const data = await res.json();
  if (!data.results) return [];

  return data.results.map((page: any) => ({
    id: page.id,
    task: getTitleValue(page.properties["Task"]),
    status: getSelectValue(page.properties["Status"]),
    priority: getSelectValue(page.properties["Priority"]),
    assignedTo: getSelectValue(page.properties["Assigned To"]),
    type: getSelectValue(page.properties["Type"]),
    raisedBy: getSelectValue(page.properties["Raised By"]),
    dueDate: getDateValue(page.properties["Due Date"]),
    linearId: getRichTextValue(page.properties["Linear ID"]),
    notes: getRichTextValue(page.properties["Notes"]),
  }));
}

export async function getActivityLog(): Promise<ActivityEntry[]> {
  const res = await fetch(
    `https://api.notion.com/v1/databases/${ACTIVITY_LOG_ID}/query`,
    {
      method: "POST",
      headers,
      body: JSON.stringify({
        sorts: [{ property: "Timestamp", direction: "descending" }],
        page_size: 50,
      }),
      next: { revalidate: 30 },
    }
  );

  const data = await res.json();
  if (!data.results) return [];

  return data.results.map((page: any) => ({
    id: page.id,
    activity: getTitleValue(page.properties["Activity"]),
    agent: getSelectValue(page.properties["Agent"]),
    type: getSelectValue(page.properties["Type"]),
    ticketRef: getRichTextValue(page.properties["Ticket Ref"]),
    ticket: getRichTextValue(page.properties["Ticket"]),
    details: getRichTextValue(page.properties["Details"]),
    timestamp: getDateValue(page.properties["Timestamp"]),
    modelUsed: getSelectValue(page.properties["Model Used"]),
  }));
}
