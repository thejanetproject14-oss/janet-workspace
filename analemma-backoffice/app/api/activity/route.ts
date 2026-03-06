import { NextResponse } from "next/server";
import { getActivityLog } from "@/lib/notion";

export const revalidate = 30;

export async function GET() {
  try {
    const activity = await getActivityLog();
    return NextResponse.json(activity);
  } catch (error: any) {
    return NextResponse.json(
      { error: error.message || "Failed to fetch activity" },
      { status: 500 }
    );
  }
}
