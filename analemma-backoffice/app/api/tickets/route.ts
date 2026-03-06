import { NextResponse } from "next/server";
import { getTickets } from "@/lib/notion";

export const dynamic = "force-dynamic";

export async function GET() {
  try {
    const tickets = await getTickets();
    return NextResponse.json(tickets);
  } catch (error: unknown) {
    const msg = error instanceof Error ? error.message : "Unknown error";
    return NextResponse.json({ error: msg }, { status: 500 });
  }
}
