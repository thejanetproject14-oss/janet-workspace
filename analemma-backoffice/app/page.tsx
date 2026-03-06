import { getTickets, getActivityLog } from "@/lib/notion";
import type { Ticket, ActivityEntry } from "@/lib/notion";

const STATUS_ORDER = [
  "In Progress",
  "To Do",
  "Janet Review",
  "Sunshine Approval",
  "Done",
  "Backlog",
];

const STATUS_COLORS: Record<string, string> = {
  Backlog: "bg-neutral-900 border-neutral-800",
  "To Do": "bg-blue-950/40 border-blue-800/30",
  "In Progress": "bg-amber-950/40 border-amber-700/30",
  "Janet Review": "bg-purple-950/40 border-purple-700/30",
  "Sunshine Approval": "bg-pink-950/40 border-pink-700/30",
  Done: "bg-green-950/40 border-green-800/30",
};

const STATUS_HEADER: Record<string, string> = {
  Backlog: "text-neutral-500",
  "To Do": "text-blue-400",
  "In Progress": "text-amber-400",
  "Janet Review": "text-purple-400",
  "Sunshine Approval": "text-pink-400",
  Done: "text-green-400",
};

const PRIORITY_BADGES: Record<string, string> = {
  Urgent: "bg-red-500/20 text-red-400 border border-red-500/30",
  High: "bg-orange-500/20 text-orange-400 border border-orange-500/30",
  Medium: "bg-blue-500/20 text-blue-400 border border-blue-500/30",
  Low: "bg-neutral-500/20 text-neutral-400 border border-neutral-500/30",
  "P1 Critical": "bg-red-500/20 text-red-400 border border-red-500/30",
  "P2 High": "bg-orange-500/20 text-orange-400 border border-orange-500/30",
  "P3 Normal": "bg-blue-500/20 text-blue-400 border border-blue-500/30",
  "P4 Low": "bg-neutral-500/20 text-neutral-400 border border-neutral-500/30",
};

const TYPE_BADGES: Record<string, string> = {
  SEO: "bg-yellow-500/10 text-yellow-400",
  PR: "bg-orange-500/10 text-orange-400",
  Copy: "bg-red-500/10 text-red-400",
  Content: "bg-blue-500/10 text-blue-400",
  Research: "bg-green-500/10 text-green-400",
  Tech: "bg-neutral-500/10 text-neutral-400",
  Strategy: "bg-purple-500/10 text-purple-400",
};

const AGENT_COLORS: Record<string, string> = {
  Janet: "text-purple-400",
  "Content Agent": "text-blue-400",
  "Research Agent": "text-green-400",
  "SEO Agent": "text-yellow-400",
  "PR Agent": "text-orange-400",
  "Writer Agent": "text-red-400",
  "Shopify Agent": "text-neutral-400",
  Sunshine: "text-pink-400",
};

const AGENT_EMOJIS: Record<string, string> = {
  Janet: "🟣",
  "Content Agent": "🔵",
  "Research Agent": "🟢",
  "SEO Agent": "🔍",
  "PR Agent": "📣",
  "Writer Agent": "✍️",
  "Shopify Agent": "🛒",
  Sunshine: "🩷",
};

function TicketCard({ ticket }: { ticket: Ticket }) {
  return (
    <div
      className={`p-3 rounded-lg border ${STATUS_COLORS[ticket.status] || "bg-neutral-900 border-neutral-800"} hover:border-neutral-600 transition-colors`}
    >
      {/* Linear ID */}
      {ticket.linearId && (
        <p className="text-[10px] text-neutral-600 font-mono mb-1">{ticket.linearId}</p>
      )}
      {/* Task name */}
      <p className="text-sm font-medium leading-snug mb-2">{ticket.task}</p>
      {/* Badges row */}
      <div className="flex flex-wrap gap-1.5 mb-2">
        {ticket.priority && (
          <span className={`text-[10px] px-1.5 py-0.5 rounded ${PRIORITY_BADGES[ticket.priority] || ""}`}>
            {ticket.priority}
          </span>
        )}
        {ticket.type && (
          <span className={`text-[10px] px-1.5 py-0.5 rounded ${TYPE_BADGES[ticket.type] || "text-neutral-400"}`}>
            {ticket.type}
          </span>
        )}
        {ticket.assignedTo && (
          <span className={`text-[10px] ${AGENT_COLORS[ticket.assignedTo] || "text-neutral-400"}`}>
            {AGENT_EMOJIS[ticket.assignedTo] || "⬜"} {ticket.assignedTo}
          </span>
        )}
      </div>
      {/* Due date */}
      {ticket.dueDate && (
        <p className="text-[10px] text-neutral-600">
          Due {new Date(ticket.dueDate).toLocaleDateString("en-SG", { day: "numeric", month: "short" })}
        </p>
      )}
      {/* Notes */}
      {ticket.notes && (
        <p className="text-[10px] text-neutral-500 mt-1.5 border-t border-neutral-800/60 pt-1.5 leading-relaxed line-clamp-2">
          {ticket.notes}
        </p>
      )}
    </div>
  );
}

function StatusColumn({ status, tickets }: { status: string; tickets: Ticket[] }) {
  const filtered = tickets.filter((t) => t.status === status);
  return (
    <div className="min-w-[270px] flex-1">
      <div className="flex items-center gap-2 mb-3">
        <h3 className={`text-xs font-bold uppercase tracking-wider ${STATUS_HEADER[status] || "text-neutral-400"}`}>
          {status}
        </h3>
        <span className="text-[10px] bg-neutral-800 text-neutral-500 px-1.5 py-0.5 rounded-full">
          {filtered.length}
        </span>
      </div>
      <div className="space-y-2">
        {filtered.map((ticket) => (
          <TicketCard key={ticket.id} ticket={ticket} />
        ))}
        {filtered.length === 0 && (
          <div className="text-xs text-neutral-700 italic p-3 border border-dashed border-neutral-800 rounded-lg">
            Empty
          </div>
        )}
      </div>
    </div>
  );
}

function AgentStatusCard({
  name, emoji, model, status, ticketCount,
}: {
  name: string; emoji: string; model: string; status: string; ticketCount: number;
}) {
  return (
    <div className="bg-neutral-950 border border-neutral-800 rounded-lg p-4 hover:border-neutral-700 transition-colors">
      <div className="flex items-center justify-between mb-2">
        <div className="flex items-center gap-2">
          <span>{emoji}</span>
          <h3 className="font-semibold text-sm">{name}</h3>
        </div>
        {ticketCount > 0 && (
          <span className="text-[10px] bg-neutral-800 text-neutral-400 px-1.5 py-0.5 rounded-full">
            {ticketCount} open
          </span>
        )}
      </div>
      <div className="space-y-1 text-[11px] text-neutral-500">
        <p>{model}</p>
        <p className="text-green-400">{status}</p>
      </div>
    </div>
  );
}

function ActivityRow({ entry }: { entry: ActivityEntry }) {
  const ref = entry.ticket || entry.ticketRef;
  return (
    <div className="flex items-start gap-3 py-2.5 border-b border-neutral-800/40 last:border-0">
      <span className="text-base mt-0.5 flex-shrink-0">
        {AGENT_EMOJIS[entry.agent] || "⬜"}
      </span>
      <div className="flex-1 min-w-0">
        <div className="flex items-start justify-between gap-2">
          <p className="text-sm text-neutral-200 leading-snug">{entry.activity}</p>
          {ref && (
            <span className="text-[10px] font-mono text-neutral-600 flex-shrink-0">{ref}</span>
          )}
        </div>
        {entry.details && (
          <p className="text-xs text-neutral-500 mt-1 leading-relaxed">{entry.details}</p>
        )}
        <div className="flex gap-2 mt-1 text-[10px] text-neutral-600">
          <span className={AGENT_COLORS[entry.agent] || "text-neutral-500"}>{entry.agent}</span>
          {entry.type && <span>· {entry.type}</span>}
          {entry.modelUsed && <span>· {entry.modelUsed}</span>}
          {entry.timestamp && (
            <span>
              ·{" "}
              {new Date(entry.timestamp).toLocaleString("en-SG", {
                timeZone: "Asia/Singapore",
                day: "numeric",
                month: "short",
                hour: "2-digit",
                minute: "2-digit",
              })}
            </span>
          )}
        </div>
      </div>
    </div>
  );
}

export const dynamic = "force-dynamic";

export default async function Dashboard() {
  const [tickets, activity] = await Promise.all([getTickets(), getActivityLog()]);

  const agentTicketCounts: Record<string, number> = {};
  tickets
    .filter((t) => t.status !== "Done")
    .forEach((t) => {
      if (t.assignedTo) {
        agentTicketCounts[t.assignedTo] = (agentTicketCounts[t.assignedTo] || 0) + 1;
      }
    });

  const totalOpen = tickets.filter((t) => t.status !== "Done").length;
  const totalInProgress = tickets.filter((t) => t.status === "In Progress").length;
  const totalReview = tickets.filter((t) => ["Janet Review", "Sunshine Approval"].includes(t.status)).length;

  return (
    <main className="min-h-screen p-6 max-w-[1600px] mx-auto">
      {/* Header */}
      <div className="flex items-center justify-between mb-6">
        <div>
          <h1 className="text-xl font-bold tracking-tight flex items-center gap-2">
            <span>✦</span> Analemma Backoffice
          </h1>
          <p className="text-xs text-neutral-600 mt-0.5">
            Agent command center · Refreshes every 30s ·{" "}
            {new Date().toLocaleString("en-SG", {
              timeZone: "Asia/Singapore",
              weekday: "short",
              day: "numeric",
              month: "short",
              hour: "2-digit",
              minute: "2-digit",
            })}
          </p>
        </div>
        <div className="flex items-center gap-4 text-xs text-neutral-500">
          <span><span className="text-white font-medium">{totalOpen}</span> open</span>
          <span><span className="text-amber-400 font-medium">{totalInProgress}</span> in progress</span>
          <span><span className="text-purple-400 font-medium">{totalReview}</span> in review</span>
          <div className="flex items-center gap-1.5">
            <span className="inline-block w-1.5 h-1.5 rounded-full bg-green-500 animate-pulse" />
            <span>7 agents live</span>
          </div>
        </div>
      </div>

      {/* Agent Status Cards */}
      <section className="mb-6">
        <h2 className="text-[11px] font-semibold uppercase tracking-widest text-neutral-600 mb-3">Agents</h2>
        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 xl:grid-cols-7 gap-2">
          {[
            { name: "Janet", emoji: "🟣", model: "Claude Opus 4.6" },
            { name: "Content Agent", emoji: "🔵", model: "Claude Sonnet 4" },
            { name: "Research Agent", emoji: "🟢", model: "Claude Sonnet 4" },
            { name: "SEO Agent", emoji: "🔍", model: "Claude Sonnet 4" },
            { name: "PR Agent", emoji: "📣", model: "Claude Sonnet 4" },
            { name: "Writer Agent", emoji: "✍️", model: "Claude Sonnet 4" },
            { name: "Shopify Agent", emoji: "🛒", model: "Claude Sonnet 4" },
          ].map((agent) => (
            <AgentStatusCard
              key={agent.name}
              {...agent}
              status="● Live"
              ticketCount={agentTicketCounts[agent.name] || 0}
            />
          ))}
        </div>
      </section>

      {/* Main content: Kanban + Activity side by side */}
      <div className="flex gap-6">
        {/* Kanban Board */}
        <section className="flex-1 min-w-0">
          <h2 className="text-[11px] font-semibold uppercase tracking-widest text-neutral-600 mb-3">Tickets</h2>
          <div className="flex gap-3 overflow-x-auto pb-4">
            {STATUS_ORDER.map((status) => (
              <StatusColumn key={status} status={status} tickets={tickets} />
            ))}
          </div>
        </section>

        {/* Activity Feed */}
        <section className="w-80 flex-shrink-0">
          <h2 className="text-[11px] font-semibold uppercase tracking-widest text-neutral-600 mb-3">
            Activity
            <span className="ml-2 text-neutral-700 font-normal normal-case tracking-normal">
              ({activity.length} entries)
            </span>
          </h2>
          <div className="bg-neutral-950 border border-neutral-800 rounded-lg p-4 max-h-[calc(100vh-260px)] overflow-y-auto">
            {activity.length === 0 ? (
              <p className="text-xs text-neutral-700 italic">No activity yet</p>
            ) : (
              activity.map((entry) => (
                <ActivityRow key={entry.id} entry={entry} />
              ))
            )}
          </div>
        </section>
      </div>
    </main>
  );
}
