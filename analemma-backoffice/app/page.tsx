import { getTickets, getActivityLog, Ticket, ActivityEntry } from "@/lib/notion";

const STATUS_ORDER = [
  "In Progress",
  "To Do",
  "Janet Review",
  "Sunshine Approval",
  "Backlog",
  "Done",
];

const STATUS_COLORS: Record<string, string> = {
  Backlog: "bg-neutral-700",
  "To Do": "bg-blue-900/50 border-blue-500/30",
  "In Progress": "bg-yellow-900/50 border-yellow-500/30",
  "Janet Review": "bg-purple-900/50 border-purple-500/30",
  "Sunshine Approval": "bg-pink-900/50 border-pink-500/30",
  Done: "bg-green-900/50 border-green-500/30",
};

const PRIORITY_BADGES: Record<string, string> = {
  "P1 Critical": "bg-red-500/20 text-red-400 border border-red-500/30",
  "P2 High": "bg-orange-500/20 text-orange-400 border border-orange-500/30",
  "P3 Normal": "bg-blue-500/20 text-blue-400 border border-blue-500/30",
  "P4 Low": "bg-neutral-500/20 text-neutral-400 border border-neutral-500/30",
};

const AGENT_COLORS: Record<string, string> = {
  Janet: "text-purple-400",
  "Content Agent": "text-blue-400",
  "Research Agent": "text-green-400",
  Sunshine: "text-pink-400",
};

const AGENT_EMOJIS: Record<string, string> = {
  Janet: "🟣",
  "Content Agent": "🔵",
  "Research Agent": "🟢",
  Sunshine: "🩷",
};

function StatusColumn({
  status,
  tickets,
}: {
  status: string;
  tickets: Ticket[];
}) {
  const filtered = tickets.filter((t) => t.status === status);
  return (
    <div className="min-w-[280px] flex-1">
      <div className="flex items-center gap-2 mb-3">
        <h3 className="text-sm font-semibold uppercase tracking-wider text-neutral-400">
          {status}
        </h3>
        <span className="text-xs bg-neutral-800 text-neutral-500 px-2 py-0.5 rounded-full">
          {filtered.length}
        </span>
      </div>
      <div className="space-y-2">
        {filtered.map((ticket) => (
          <div
            key={ticket.id}
            className={`p-3 rounded-lg border ${
              STATUS_COLORS[status] || "bg-neutral-800"
            } border-neutral-700/50 hover:border-neutral-600 transition-colors`}
          >
            <p className="text-sm font-medium mb-2">{ticket.task}</p>
            <div className="flex flex-wrap gap-1.5">
              {ticket.priority && (
                <span
                  className={`text-[10px] px-1.5 py-0.5 rounded ${
                    PRIORITY_BADGES[ticket.priority] || ""
                  }`}
                >
                  {ticket.priority}
                </span>
              )}
              {ticket.assignedTo && (
                <span
                  className={`text-[10px] ${
                    AGENT_COLORS[ticket.assignedTo] || "text-neutral-400"
                  }`}
                >
                  {AGENT_EMOJIS[ticket.assignedTo] || "⬜"}{" "}
                  {ticket.assignedTo}
                </span>
              )}
              {ticket.type && (
                <span className="text-[10px] text-neutral-500">
                  {ticket.type}
                </span>
              )}
            </div>
          </div>
        ))}
        {filtered.length === 0 && (
          <div className="text-xs text-neutral-600 italic p-3">No tickets</div>
        )}
      </div>
    </div>
  );
}

function AgentStatusCard({
  name,
  emoji,
  model,
  status,
  ticketCount,
}: {
  name: string;
  emoji: string;
  model: string;
  status: string;
  ticketCount: number;
}) {
  return (
    <div className="bg-neutral-900 border border-neutral-800 rounded-lg p-4 hover:border-neutral-700 transition-colors">
      <div className="flex items-center gap-2 mb-2">
        <span className="text-lg">{emoji}</span>
        <h3 className="font-semibold text-sm">{name}</h3>
      </div>
      <div className="space-y-1 text-xs text-neutral-400">
        <p>
          Model: <span className="text-neutral-300">{model}</span>
        </p>
        <p>
          Status:{" "}
          <span className="text-green-400">{status}</span>
        </p>
        <p>
          Active tickets:{" "}
          <span className="text-neutral-300">{ticketCount}</span>
        </p>
      </div>
    </div>
  );
}

function ActivityFeed({ entries }: { entries: ActivityEntry[] }) {
  if (entries.length === 0) {
    return (
      <p className="text-xs text-neutral-600 italic">No activity yet</p>
    );
  }
  return (
    <div className="space-y-2">
      {entries.map((entry) => (
        <div
          key={entry.id}
          className="flex items-start gap-3 text-xs border-b border-neutral-800/50 pb-2"
        >
          <span>
            {AGENT_EMOJIS[entry.agent] || "⬜"}
          </span>
          <div className="flex-1">
            <p className="text-neutral-300">{entry.activity}</p>
            <div className="flex gap-2 mt-0.5 text-neutral-500">
              <span>{entry.agent}</span>
              {entry.type && <span>· {entry.type}</span>}
              {entry.modelUsed && <span>· {entry.modelUsed}</span>}
              {entry.timestamp && (
                <span>
                  ·{" "}
                  {new Date(entry.timestamp).toLocaleDateString("en-SG", {
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
      ))}
    </div>
  );
}

export const revalidate = 30;

export default async function Dashboard() {
  const [tickets, activity] = await Promise.all([
    getTickets(),
    getActivityLog(),
  ]);

  const agentTicketCounts: Record<string, number> = {};
  tickets
    .filter((t) => t.status !== "Done")
    .forEach((t) => {
      if (t.assignedTo) {
        agentTicketCounts[t.assignedTo] =
          (agentTicketCounts[t.assignedTo] || 0) + 1;
      }
    });

  return (
    <main className="min-h-screen p-6 max-w-[1400px] mx-auto">
      {/* Header */}
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-2xl font-bold flex items-center gap-2">
            <span>🎛️</span> Analemma Backoffice
          </h1>
          <p className="text-sm text-neutral-500 mt-1">
            Agent command center · Last updated{" "}
            {new Date().toLocaleString("en-SG", {
              timeZone: "Asia/Singapore",
              day: "numeric",
              month: "short",
              hour: "2-digit",
              minute: "2-digit",
            })}
          </p>
        </div>
        <div className="flex items-center gap-2">
          <span className="inline-block w-2 h-2 rounded-full bg-green-500 animate-pulse" />
          <span className="text-xs text-neutral-400">System active</span>
        </div>
      </div>

      {/* Agent Status Cards */}
      <section className="mb-8">
        <h2 className="text-sm font-semibold uppercase tracking-wider text-neutral-500 mb-3">
          Agents
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
          <AgentStatusCard
            name="Janet"
            emoji="🟣"
            model="Claude Opus 4.6"
            status="● Live"
            ticketCount={agentTicketCounts["Janet"] || 0}
          />
          <AgentStatusCard
            name="Content Agent"
            emoji="🔵"
            model="Claude Sonnet 4"
            status="● Live"
            ticketCount={agentTicketCounts["Content Agent"] || 0}
          />
          <AgentStatusCard
            name="Research Agent"
            emoji="🟢"
            model="Claude Sonnet 4"
            status="● Live"
            ticketCount={agentTicketCounts["Research Agent"] || 0}
          />
        </div>
      </section>

      {/* Kanban Board */}
      <section className="mb-8">
        <h2 className="text-sm font-semibold uppercase tracking-wider text-neutral-500 mb-3">
          Ticket Board
        </h2>
        <div className="flex gap-4 overflow-x-auto pb-4">
          {STATUS_ORDER.map((status) => (
            <StatusColumn key={status} status={status} tickets={tickets} />
          ))}
        </div>
      </section>

      {/* Activity Feed */}
      <section>
        <h2 className="text-sm font-semibold uppercase tracking-wider text-neutral-500 mb-3">
          Recent Activity
        </h2>
        <div className="bg-neutral-900 border border-neutral-800 rounded-lg p-4">
          <ActivityFeed entries={activity} />
        </div>
      </section>
    </main>
  );
}
