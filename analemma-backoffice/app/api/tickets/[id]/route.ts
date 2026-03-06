import { NextResponse } from "next/server";

export const dynamic = "force-dynamic";

const NOTION_TOKEN = process.env.NOTION_TOKEN!.trim();

const VALID_STATUSES = [
  "Backlog",
  "To Do",
  "In Progress",
  "Janet Review",
  "Sunshine Approval",
  "Done",
];

export async function PATCH(
  req: Request,
  { params }: { params: Promise<{ id: string }> }
) {
  const { id } = await params;
  const body = await req.json();
  const { status, assignedTo, priority } = body;

  if (!id) {
    return NextResponse.json({ error: "Missing ticket id" }, { status: 400 });
  }

  if (status && !VALID_STATUSES.includes(status)) {
    return NextResponse.json(
      { error: `Invalid status. Must be one of: ${VALID_STATUSES.join(", ")}` },
      { status: 400 }
    );
  }

  const properties: Record<string, unknown> = {};
  if (status) properties["Status"] = { select: { name: status } };
  if (assignedTo) properties["Assigned To"] = { select: { name: assignedTo } };
  if (priority) properties["Priority"] = { select: { name: priority } };

  if (Object.keys(properties).length === 0) {
    return NextResponse.json({ error: "Nothing to update" }, { status: 400 });
  }

  const res = await fetch(`https://api.notion.com/v1/pages/${id}`, {
    method: "PATCH",
    headers: {
      Authorization: `Bearer ${NOTION_TOKEN}`,
      "Notion-Version": "2022-06-28",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ properties }),
    cache: "no-store",
  });

  if (!res.ok) {
    const err = await res.json();
    return NextResponse.json({ error: err }, { status: 500 });
  }

  return NextResponse.json({ ok: true, id, updated: properties });
}
