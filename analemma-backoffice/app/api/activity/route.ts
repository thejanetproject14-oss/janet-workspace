import { NextResponse } from "next/server";
import { getActivityLog } from "@/lib/notion";

const NOTION_TOKEN = process.env.NOTION_TOKEN!;
const ACTIVITY_LOG_ID = process.env.ACTIVITY_LOG_ID!;

export const revalidate = 30;

export async function GET() {
  const entries = await getActivityLog();
  return NextResponse.json(entries);
}

export async function POST(req: Request) {
  const body = await req.json();
  const { agent, activity, ticket, details, type, modelUsed } = body;

  if (!agent || !activity) {
    return NextResponse.json({ error: "agent and activity are required" }, { status: 400 });
  }

  const now = new Date().toISOString();

  const props: Record<string, unknown> = {
    Activity: { title: [{ text: { content: String(activity) } }] },
    Agent: { select: { name: String(agent) } },
    Timestamp: { date: { start: now } },
  };

  if (ticket) props["Ticket"] = { rich_text: [{ text: { content: String(ticket) } }] };
  if (details) props["Details"] = { rich_text: [{ text: { content: String(details).slice(0, 2000) } }] };
  if (type) props["Type"] = { select: { name: String(type) } };
  if (modelUsed) props["Model Used"] = { select: { name: String(modelUsed) } };

  const res = await fetch("https://api.notion.com/v1/pages", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${NOTION_TOKEN}`,
      "Notion-Version": "2022-06-28",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      parent: { database_id: ACTIVITY_LOG_ID },
      properties: props,
    }),
  });

  if (!res.ok) {
    const err = await res.json();
    return NextResponse.json({ error: err }, { status: 500 });
  }

  const result = await res.json();
  return NextResponse.json({ id: result.id, ok: true });
}
