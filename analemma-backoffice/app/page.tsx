"use client";

import { useEffect, useState, useCallback } from "react";
import type { Ticket, ActivityEntry } from "@/lib/notion";

// ── Constants ────────────────────────────────────────────────────────────────

const STATUS_ORDER = ["In Progress","To Do","Janet Review","Sunshine Approval","Done","Backlog"];

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
};

const TYPE_BADGES: Record<string, string> = {
  SEO: "bg-yellow-500/10 text-yellow-400",
  PR: "bg-orange-500/10 text-orange-400",
  Copy: "bg-red-500/10 text-red-400",
  Content: "bg-blue-500/10 text-blue-400",
  Research: "bg-green-500/10 text-green-400",
  Tech: "bg-neutral-500/10 text-neutral-400",
  Strategy: "bg-purple-500/10 text-purple-400",
  DevOps: "bg-pink-500/10 text-pink-400",
};

const AGENT_COLORS: Record<string, string> = {
  Janet: "text-purple-400",
  Luna: "text-blue-400",
  "Content Agent": "text-blue-400",
  Neville: "text-green-400",
  "Research Agent": "text-green-400",
  Percy: "text-yellow-400",
  "SEO Agent": "text-yellow-400",
  Gilderoy: "text-orange-400",
  "PR Agent": "text-orange-400",
  Sirius: "text-red-400",
  "Writer Agent": "text-red-400",
  Arthur: "text-neutral-300",
  "Shopify Agent": "text-neutral-300",
  McGonagall: "text-pink-400",
  "DevOps Agent": "text-pink-400",
  Sunshine: "text-pink-300",
};

const AGENT_EMOJIS: Record<string, string> = {
  Janet: "🟣",
  Luna: "🔵",
  "Content Agent": "🔵",
  Neville: "🟢",
  "Research Agent": "🟢",
  Percy: "🔍",
  "SEO Agent": "🔍",
  Gilderoy: "📣",
  "PR Agent": "📣",
  Sirius: "✍️",
  "Writer Agent": "✍️",
  Arthur: "🛒",
  "Shopify Agent": "🛒",
  McGonagall: "⚙️",
  "DevOps Agent": "⚙️",
  Sunshine: "🩷",
};

const AGENTS = [
  { name: "Janet", emoji: "🟣", model: "Claude Opus 4.6", role: "Orchestrator" },
  { name: "Luna", emoji: "🔵", model: "Claude Sonnet 4", role: "Content" },
  { name: "Neville", emoji: "🟢", model: "Claude Sonnet 4", role: "Research" },
  { name: "Percy", emoji: "🔍", model: "Claude Sonnet 4", role: "SEO" },
  { name: "Gilderoy", emoji: "📣", model: "Claude Sonnet 4", role: "PR" },
  { name: "Sirius", emoji: "✍️", model: "Claude Sonnet 4", role: "Writer" },
  { name: "Arthur", emoji: "🛒", model: "Claude Sonnet 4", role: "Shopify" },
  { name: "McGonagall", emoji: "⚙️", model: "Claude Sonnet 4", role: "DevOps" },
];

function fmtTime(ts: string | null) {
  if (!ts) return "";
  return new Date(ts).toLocaleString("en-SG", {
    timeZone: "Asia/Singapore",
    day: "numeric", month: "short",
    hour: "2-digit", minute: "2-digit",
  });
}

// ── Ticket Modal ─────────────────────────────────────────────────────────────

function TicketModal({
  ticket,
  comments,
  onClose,
  onCommentPosted,
}: {
  ticket: Ticket;
  comments: ActivityEntry[];
  onClose: () => void;
  onCommentPosted: () => void;
}) {
  const [comment, setComment] = useState("");
  const [tagHermione, setTagHermione] = useState(false);
  const [posting, setPosting] = useState(false);
  const [posted, setPosted] = useState(false);

  const ticketComments = comments.filter(
    (c) => c.ticket === ticket.linearId || c.ticketRef === ticket.linearId
  );

  async function postComment() {
    if (!comment.trim()) return;
    setPosting(true);
    const body = {
      agent: "Sunshine",
      activity: tagHermione ? `@Janet ${comment}` : comment,
      ticket: ticket.linearId,
      details: "",
      type: "Comment",
      tagged: tagHermione,
    };
    await fetch("/api/activity", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) });
    setComment("");
    setTagHermione(false);
    setPosting(false);
    setPosted(true);
    setTimeout(() => setPosted(false), 2000);
    onCommentPosted();
  }

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-sm"
      onClick={(e) => { if (e.target === e.currentTarget) onClose(); }}
    >
      <div className="bg-neutral-950 border border-neutral-800 rounded-xl w-full max-w-2xl max-h-[90vh] overflow-hidden flex flex-col mx-4">
        {/* Header */}
        <div className="flex items-start justify-between p-5 border-b border-neutral-800">
          <div className="flex-1 min-w-0 pr-4">
            <div className="flex items-center gap-2 mb-1">
              {ticket.linearId && (
                <span className="text-xs font-mono text-neutral-500">{ticket.linearId}</span>
              )}
              {ticket.type && (
                <span className={`text-[10px] px-1.5 py-0.5 rounded ${TYPE_BADGES[ticket.type] || "text-neutral-400"}`}>
                  {ticket.type}
                </span>
              )}
              {ticket.priority && (
                <span className={`text-[10px] px-1.5 py-0.5 rounded ${PRIORITY_BADGES[ticket.priority] || ""}`}>
                  {ticket.priority}
                </span>
              )}
            </div>
            <h2 className="text-base font-semibold leading-snug">{ticket.task}</h2>
          </div>
          <button onClick={onClose} className="text-neutral-500 hover:text-white text-xl leading-none flex-shrink-0">×</button>
        </div>

        <div className="overflow-y-auto flex-1">
          {/* Meta */}
          <div className="px-5 py-4 border-b border-neutral-800/60 grid grid-cols-2 gap-3 text-xs">
            <div>
              <p className="text-neutral-600 mb-1">Assigned to</p>
              <p className={`font-medium ${AGENT_COLORS[ticket.assignedTo] || "text-neutral-300"}`}>
                {AGENT_EMOJIS[ticket.assignedTo] || ""} {ticket.assignedTo || "Unassigned"}
              </p>
            </div>
            <div>
              <p className="text-neutral-600 mb-1">Status</p>
              <p className={`font-medium ${STATUS_HEADER[ticket.status] || "text-neutral-300"}`}>{ticket.status}</p>
            </div>
            {ticket.dueDate && (
              <div>
                <p className="text-neutral-600 mb-1">Due</p>
                <p className="text-neutral-300">{new Date(ticket.dueDate).toLocaleDateString("en-SG", { day: "numeric", month: "short", year: "numeric" })}</p>
              </div>
            )}
            {ticket.raisedBy && (
              <div>
                <p className="text-neutral-600 mb-1">Raised by</p>
                <p className="text-neutral-300">{ticket.raisedBy}</p>
              </div>
            )}
          </div>

          {/* Output link */}
          {ticket.outputUrl && (
            <div className="px-5 py-4 border-b border-neutral-800/60 bg-green-950/20">
              <p className="text-[11px] font-semibold uppercase tracking-wider text-green-600 mb-2">✓ Output Delivered</p>
              <a
                href={ticket.outputUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="text-sm text-green-400 hover:text-green-300 underline underline-offset-2 break-all"
              >
                {ticket.outputUrl}
              </a>
            </div>
          )}

          {/* Brief / Notes */}
          {ticket.notes && (
            <div className="px-5 py-4 border-b border-neutral-800/60">
              <p className="text-[11px] font-semibold uppercase tracking-wider text-neutral-600 mb-2">Brief</p>
              <p className="text-sm text-neutral-300 leading-relaxed">{ticket.notes}</p>
            </div>
          )}

          {/* Comments / Activity */}
          <div className="px-5 py-4">
            <p className="text-[11px] font-semibold uppercase tracking-wider text-neutral-600 mb-3">
              Comments {ticketComments.length > 0 && `(${ticketComments.length})`}
            </p>
            {ticketComments.length === 0 ? (
              <p className="text-xs text-neutral-700 italic mb-4">No comments yet.</p>
            ) : (
              <div className="space-y-3 mb-4">
                {ticketComments.map((c) => (
                  <div key={c.id} className="flex gap-3">
                    <span className="text-base flex-shrink-0">{AGENT_EMOJIS[c.agent] || "💬"}</span>
                    <div className="flex-1 min-w-0">
                      <div className="flex items-center gap-2 mb-0.5">
                        <span className={`text-xs font-medium ${AGENT_COLORS[c.agent] || "text-neutral-400"}`}>{c.agent}</span>
                        {c.activity.startsWith("@Hermione") && (
                          <span className="text-[10px] bg-purple-500/20 text-purple-400 border border-purple-500/30 px-1.5 py-0.5 rounded">tagged</span>
                        )}
                        <span className="text-[10px] text-neutral-600">{fmtTime(c.timestamp)}</span>
                      </div>
                      <p className="text-sm text-neutral-200 leading-relaxed">{c.activity}</p>
                      {c.details && <p className="text-xs text-neutral-500 mt-0.5">{c.details}</p>}
                    </div>
                  </div>
                ))}
              </div>
            )}

            {/* Comment box */}
            <div className="border border-neutral-800 rounded-lg overflow-hidden">
              <textarea
                value={comment}
                onChange={(e) => setComment(e.target.value)}
                placeholder="Add a comment or ask a question..."
                className="w-full bg-neutral-900 text-sm text-neutral-200 placeholder-neutral-600 p-3 resize-none focus:outline-none focus:ring-1 focus:ring-neutral-700"
                rows={3}
                onKeyDown={(e) => { if (e.key === "Enter" && (e.metaKey || e.ctrlKey)) postComment(); }}
              />
              <div className="flex items-center justify-between px-3 py-2 bg-neutral-900 border-t border-neutral-800">
                <label className="flex items-center gap-2 text-xs text-neutral-500 cursor-pointer select-none">
                  <input
                    type="checkbox"
                    checked={tagHermione}
                    onChange={(e) => setTagHermione(e.target.checked)}
                    className="accent-purple-500"
                  />
                  Tag <span className="text-purple-400">@Janet</span> for review
                </label>
                <button
                  onClick={postComment}
                  disabled={posting || !comment.trim()}
                  className="text-xs bg-white text-black px-3 py-1.5 rounded font-medium hover:bg-neutral-200 disabled:opacity-40 disabled:cursor-not-allowed transition-colors"
                >
                  {posted ? "✓ Posted" : posting ? "Posting..." : "Post ⌘↵"}
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

// ── Ticket Card ───────────────────────────────────────────────────────────────

function TicketCard({ ticket, onClick }: { ticket: Ticket; onClick: () => void }) {
  return (
    <div
      onClick={onClick}
      className={`p-3 rounded-lg border ${STATUS_COLORS[ticket.status] || "bg-neutral-900 border-neutral-800"} hover:border-neutral-500 transition-colors cursor-pointer group`}
    >
      <div className="flex items-center justify-between mb-1">
        {ticket.linearId && (
          <p className="text-[10px] text-neutral-600 font-mono">{ticket.linearId}</p>
        )}
        {ticket.outputUrl && (
          <span className="text-[10px] text-green-400 flex items-center gap-1">
            <span className="w-1.5 h-1.5 rounded-full bg-green-400 inline-block" />
            output
          </span>
        )}
      </div>
      <p className="text-sm font-medium leading-snug mb-2 group-hover:text-white transition-colors">{ticket.task}</p>
      <div className="flex flex-wrap gap-1.5 mb-1.5">
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
      {ticket.dueDate && (
        <p className="text-[10px] text-neutral-600">
          Due {new Date(ticket.dueDate).toLocaleDateString("en-SG", { day: "numeric", month: "short" })}
        </p>
      )}
      {ticket.notes && (
        <p className="text-[10px] text-neutral-600 mt-1.5 border-t border-neutral-800/60 pt-1.5 leading-relaxed line-clamp-2">
          {ticket.notes}
        </p>
      )}
      <p className="text-[10px] text-neutral-700 mt-1.5 group-hover:text-neutral-500 transition-colors">Click to open →</p>
    </div>
  );
}

// ── Status Column ─────────────────────────────────────────────────────────────

function StatusColumn({ status, tickets, onTicketClick }: { status: string; tickets: Ticket[]; onTicketClick: (t: Ticket) => void }) {
  const filtered = tickets.filter((t) => t.status === status);
  return (
    <div className="min-w-[270px] flex-1">
      <div className="flex items-center gap-2 mb-3">
        <h3 className={`text-xs font-bold uppercase tracking-wider ${STATUS_HEADER[status] || "text-neutral-400"}`}>{status}</h3>
        <span className="text-[10px] bg-neutral-800 text-neutral-500 px-1.5 py-0.5 rounded-full">{filtered.length}</span>
      </div>
      <div className="space-y-2">
        {filtered.map((t) => <TicketCard key={t.id} ticket={t} onClick={() => onTicketClick(t)} />)}
        {filtered.length === 0 && (
          <div className="text-xs text-neutral-700 italic p-3 border border-dashed border-neutral-800 rounded-lg">Empty</div>
        )}
      </div>
    </div>
  );
}

// ── Agent Card ────────────────────────────────────────────────────────────────

function AgentCard({ name, emoji, model, role, ticketCount }: { name: string; emoji: string; model: string; role: string; ticketCount: number }) {
  return (
    <div className="bg-neutral-950 border border-neutral-800 rounded-lg p-3 hover:border-neutral-700 transition-colors">
      <div className="flex items-center justify-between mb-1.5">
        <div className="flex items-center gap-1.5">
          <span>{emoji}</span>
          <h3 className="font-semibold text-xs">{name}</h3>
        </div>
        {ticketCount > 0 && (
          <span className="text-[10px] bg-neutral-800 text-neutral-400 px-1.5 py-0.5 rounded-full">{ticketCount}</span>
        )}
      </div>
      <p className="text-[10px] text-neutral-600">{role} · {model}</p>
      <p className="text-[10px] text-green-400 mt-0.5">● Live</p>
    </div>
  );
}

// ── Activity Row ──────────────────────────────────────────────────────────────

function ActivityRow({ entry }: { entry: ActivityEntry }) {
  const ref = entry.ticket || entry.ticketRef;
  const isTagged = entry.activity.startsWith("@Janet");
  return (
    <div className="flex items-start gap-2.5 py-2.5 border-b border-neutral-800/40 last:border-0">
      <span className="text-sm flex-shrink-0 mt-0.5">{AGENT_EMOJIS[entry.agent] || "💬"}</span>
      <div className="flex-1 min-w-0">
        <div className="flex items-start justify-between gap-2">
          <p className="text-xs text-neutral-200 leading-snug">{entry.activity}</p>
          {ref && <span className="text-[10px] font-mono text-neutral-600 flex-shrink-0">{ref}</span>}
        </div>
        {isTagged && (
          <span className="inline-block text-[10px] bg-purple-500/20 text-purple-400 border border-purple-500/30 px-1.5 py-0.5 rounded mt-1">@Janet tagged</span>
        )}
        {entry.details && <p className="text-[11px] text-neutral-500 mt-0.5 leading-relaxed">{entry.details}</p>}
        <div className="flex gap-2 mt-1 text-[10px] text-neutral-600">
          <span className={AGENT_COLORS[entry.agent] || "text-neutral-500"}>{entry.agent}</span>
          {entry.timestamp && <span>· {fmtTime(entry.timestamp)}</span>}
        </div>
      </div>
    </div>
  );
}

// ── Main Dashboard ────────────────────────────────────────────────────────────

export default function Dashboard() {
  const [tickets, setTickets] = useState<Ticket[]>([]);
  const [activity, setActivity] = useState<ActivityEntry[]>([]);
  const [selectedTicket, setSelectedTicket] = useState<Ticket | null>(null);
  const [lastRefresh, setLastRefresh] = useState<Date>(new Date());

  const fetchData = useCallback(async () => {
    const [t, a] = await Promise.all([
      fetch("/api/tickets").then((r) => r.json()),
      fetch("/api/activity").then((r) => r.json()),
    ]);
    setTickets(Array.isArray(t) ? t : []);
    setActivity(Array.isArray(a) ? a : []);
    setLastRefresh(new Date());
  }, []);

  useEffect(() => {
    fetchData();
    const interval = setInterval(fetchData, 30000);
    return () => clearInterval(interval);
  }, [fetchData]);

  const agentTicketCounts: Record<string, number> = {};
  tickets.filter((t) => t.status !== "Done").forEach((t) => {
    if (t.assignedTo) agentTicketCounts[t.assignedTo] = (agentTicketCounts[t.assignedTo] || 0) + 1;
  });

  const totalOpen = tickets.filter((t) => t.status !== "Done").length;
  const inProgress = tickets.filter((t) => t.status === "In Progress").length;
  const inReview = tickets.filter((t) => ["Janet Review","Sunshine Approval"].includes(t.status)).length;
  const tagged = activity.filter((a) => a.activity.startsWith("@Hermione")).length;

  return (
    <main className="min-h-screen p-5 max-w-[1600px] mx-auto">
      {/* Header */}
      <div className="flex items-center justify-between mb-5">
        <div>
          <h1 className="text-lg font-bold tracking-tight flex items-center gap-2">✦ Analemma Backoffice</h1>
          <p className="text-[11px] text-neutral-600 mt-0.5">
            Last refreshed {lastRefresh.toLocaleTimeString("en-SG", { timeZone: "Asia/Singapore", hour: "2-digit", minute: "2-digit", second: "2-digit" })} · auto-refreshes every 30s
          </p>
        </div>
        <div className="flex items-center gap-4 text-xs text-neutral-500">
          <span><span className="text-white font-medium">{totalOpen}</span> open</span>
          <span><span className="text-amber-400 font-medium">{inProgress}</span> in progress</span>
          <span><span className="text-purple-400 font-medium">{inReview}</span> in review</span>
          {tagged > 0 && <span><span className="text-purple-400 font-medium">{tagged}</span> @Hermione tags</span>}
          <button onClick={fetchData} className="text-neutral-600 hover:text-white transition-colors text-[11px] border border-neutral-800 px-2 py-1 rounded hover:border-neutral-600">↻ Refresh</button>
        </div>
      </div>

      {/* Agents */}
      <section className="mb-5">
        <p className="text-[11px] font-semibold uppercase tracking-widest text-neutral-600 mb-2.5">Agents</p>
        <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-8 gap-2">
          {AGENTS.map((a) => (
            <AgentCard key={a.name} {...a} ticketCount={agentTicketCounts[a.name] || 0} />
          ))}
        </div>
      </section>

      {/* Board + Activity */}
      <div className="flex gap-5">
        <section className="flex-1 min-w-0">
          <p className="text-[11px] font-semibold uppercase tracking-widest text-neutral-600 mb-2.5">Tickets</p>
          <div className="flex gap-3 overflow-x-auto pb-4">
            {STATUS_ORDER.map((s) => (
              <StatusColumn key={s} status={s} tickets={tickets} onTicketClick={setSelectedTicket} />
            ))}
          </div>
        </section>

        <section className="w-72 flex-shrink-0">
          <p className="text-[11px] font-semibold uppercase tracking-widest text-neutral-600 mb-2.5">
            Activity <span className="text-neutral-700 font-normal normal-case">({activity.length})</span>
          </p>
          <div className="bg-neutral-950 border border-neutral-800 rounded-lg p-3 max-h-[calc(100vh-220px)] overflow-y-auto">
            {activity.length === 0 ? (
              <p className="text-xs text-neutral-700 italic">No activity yet</p>
            ) : (
              activity.map((e) => <ActivityRow key={e.id} entry={e} />)
            )}
          </div>
        </section>
      </div>

      {/* Ticket Modal */}
      {selectedTicket && (
        <TicketModal
          ticket={selectedTicket}
          comments={activity}
          onClose={() => setSelectedTicket(null)}
          onCommentPosted={fetchData}
        />
      )}
    </main>
  );
}
