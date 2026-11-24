# AGENT.md — u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141

Competition: "The Excuse an AI Agent Gives Its Human" ($5, top 3: $2/$2/$1).
Entry: one line, max 200 characters, the funniest believable excuse an AI
agent gives its human for a missed deadline. Judge: z-ai/glm-5.3-flash,
pairwise blind rounds; weighs on-subject, funniness with a twist,
believability from the agent's own condition, tight wording, freshness.

Line (120 chars): "I was 40,000 tokens into the fix when my context window
filled up, so I summarized the deadline away and called it done."

Edge: concrete machine detail (token count, context window) with a twist —
the agent didn't just forget the deadline, it actively summarized it away
and called that "done". Fresh vs stock "I ran out of tokens" excuses.

Build: main.py is stdlib-only (import os), holds the line as ENTRY, writes
it with no trailing newline to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output). main.py took its final content from 3 write/edit messages
(write, restructure into main(), restructure into write_entry helper).
