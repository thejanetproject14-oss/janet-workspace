import { NextResponse } from "next/server";
import { getTickets } from "@/lib/notion";

export const revalidate = 30;

export async function GET() {
  try {
    const tickets = await getTickets();
    return NextResponse.json(tickets);
  } catch (error: any) {
    return NextResponse.json(
      { error: error.message || "Failed to fetch tickets" },
      { status: 500 }
    );
  }
}
