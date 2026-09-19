# CS 599 — Secure Agentic AI Systems: Attacks, Defenses, and Human Oversight

**Course development document — not published on the course website.**
First offering: Fall 2027. Instructor: Sanghyun Hong.

---

## 1. Catalog Description (130 words)

> Studies the security of AI systems that act autonomously on behalf of users. Modern
> AI agents reason, plan, invoke tools, maintain memory, retrieve external content, and
> communicate with other agents, and each of these capabilities opens an attack surface
> that conventional machine learning security does not cover. The course examines agentic
> AI security from three perspectives: attacks on agent reasoning, tool use, memory,
> external content, inter-agent communication, and delegated authority; architectural and
> runtime defenses including isolation, mediation, least privilege, provenance, and
> containment; and the human oversight required to supervise increasingly autonomous
> systems. Students construct threat models for agent architectures, evaluate published
> security claims against adaptive adversaries, and complete a research project.
> Organized around recent research papers. Graduate standing and CS 434 or equivalent;
> a prior course in security is recommended.

---

## 2. Course Proposal Description (long form)

AI systems are moving from passive prediction to autonomous action. An AI agent built on a
large language model does not merely produce text: it decides what to do next, calls tools
with real-world effects, reads content it did not author, writes to memory that persists
across sessions, and increasingly delegates subtasks to other agents. This shift changes
the security question. A model that produces a wrong answer is a quality problem. An agent
that sends the wrong email, executes the wrong command, or authorizes the wrong transaction
is a security incident, and it reached that state through a control path that no one
explicitly programmed.

This course treats agentic AI security as a **systems and security problem** rather than as
an extension of prompt engineering or adversarial machine learning. Its organizing claim is
that the interesting failures come from composition: reasoning, tool use, memory, retrieval,
and multi-agent delegation are individually well studied, but wiring them together produces
a system in which untrusted data and trusted instructions share a channel, in which
privilege is delegated without being scoped, and in which compromise persists in state.
Students therefore begin with a concrete systems-level model of how an agent actually
works, and only then ask what an adversary can do to it.

The course progresses through seven stages: **agent foundations → threat modeling →
attacks → defenses → evaluation → human oversight → frontier problems.** Attacks covered
include direct and indirect prompt injection, malicious tool outputs, excessive agency and
over-privilege, memory and retrieval poisoning, persistent and cross-session compromise,
and inter-agent manipulation. Defenses are examined as architecture rather than as
mitigation lists: where in an agent's execution should a reference monitor sit, what
isolation buys and costs, how information-flow restrictions interact with task utility, and
when detection should be replaced by containment. A dedicated unit on evaluation asks how
one distinguishes a security result from a benchmark artifact, with emphasis on
threat-model validity, adaptive attacks, and the security–utility tradeoff.

A distinguishing feature of the course is a unit on **human oversight and agentic-system
literacy**. As agents take more consequential actions, the operator becomes part of the
security architecture, and the question of what a human must be shown — and must
understand — in order to intervene in time is a first-class research problem rather than a
usability afterthought. This unit connects the HCI literature on human–AI interaction and
calibrated trust to the systems question of what an agent should be required to expose.

The course is organized around recent research papers, with two required papers and one
optional paper per session. Assessment is through student-led paper discussions, four
weekly paper critiques, a research-oriented final project, and a
cumulative online final exam built entirely from scenario-based security reasoning. The
first offering deliberately includes **no programming labs or weekly homework**: agent
frameworks and APIs change fast enough that lab infrastructure would consume instructor
effort better spent on research supervision, and students' implementation effort is
directed into the final project instead.

### Learning Objectives

By the end of the course, students will be able to:

1. Explain how reasoning, planning, tool use, memory, retrieval, and multi-agent
   interaction compose into modern agentic AI systems.
2. Identify assets, trust boundaries, privileges, data flows, external dependencies, and
   security assumptions in an agentic AI architecture.
3. Construct threat models for adversaries targeting prompts, external content, tools,
   memory, communication channels, and other agents.
4. Analyze attacks including prompt injection, indirect prompt injection, malicious tool
   outputs, excessive agency, memory poisoning, privilege abuse, and inter-agent
   manipulation.
5. Apply security principles — least privilege, isolation, provenance, mediation,
   authorization, runtime monitoring, containment — to agentic AI systems.
6. Evaluate security claims using appropriate threat models, attack and utility metrics,
   adaptive attacks, and realistic experimental designs.
7. Analyze what information humans need to supervise autonomous agents, and determine when
   intervention is necessary.
8. Critically evaluate agent-security research and formulate new research questions.

### Assessment

| Component | Weight |
|---|---:|
| Paper discussions | 15% |
| Paper critiques (one per class) | 20% |
| Final research project | 40% |
| Online final exam | 25% |

No separate participation grade; preparation and engagement are assessed through the
paper critiques and the student-led discussion.

### Prerequisites

Graduate standing, and CS 434: Machine Learning and Data Mining (or equivalent) — required.
CS 578: Cyber-Security and CS 499/599 | AI 539: Trustworthy ML are recommended, not required.

---

## 3. Reading-List Philosophy

The reading list has two layers, and only the first should ever appear in the catalog
description.

**Venue rule (set 2026-09-18).** Readings are drawn from top-tier security and ML venues —
IEEE S&P, USENIX Security, ACM CCS, NDSS, ESORICS; NeurIPS, ICML, ICLR; and ACL/EMNLP, CHI,
UIST, FAccT where the work belongs there. Preprints are used only where the subarea has no
published equivalent yet. The live schedule currently carries **3 preprints out of 42 entries**.
Venues are a selection criterion only and are **not printed on the course page** — they were
shown next to each title briefly on 2026-09-18 and removed the same day as clutter.

The three current preprints, and why each survives the rule:

| Paper | Slot | Why |
|---|---|---|
| Defeating Prompt Injections by Design (CaMeL) | 10/21, Required | The reference design for capability-based least privilege in agents. Nothing published covers it. Swap in the peer-reviewed version when it appears. |
| Securing AI Agents with Information-Flow Control | 11/02, Optional | Same gap on the IFC side. |
| Multi-Agent Risks from Advanced AI | 11/23, Optional | Frontier week is preprint-heavy by design. |

**Stable foundational papers** — carried forward each offering:
ReAct (ICLR'23), Toolformer (NeurIPS'23), Generative Agents (UIST'23), Reflexion (NeurIPS'23),
Greshake et al. (AISec@CCS'23), Liu et al. "Formalizing and Benchmarking Prompt Injection"
(USENIX Sec'24), InjecAgent (ACL'24), AgentDojo (NeurIPS'24), AgentPoison (NeurIPS'24),
ToolEmu (ICLR'24), Agent Security Bench (ICLR'25), Amershi et al. (CHI'19), Lee & See
"Trust in Automation" (Human Factors'04).

**Dynamically updated papers** — replaced or re-selected every offering, especially for:
tool authorization, MCP and agent-protocol security, multi-agent security, runtime
defenses, human oversight, and frontier agent-security research.

**Rule for the 11/23 session (Frontier Problems):** do not fix this reading list. Select 2–3
papers published within the previous 12 months each time the course is offered.

**Dropped on 2026-09-18** when the list moved to published venues — all were arXiv-only:
MemGPT, τ-bench, Ignore Previous Prompt, "Prompt Injection attack against LLM-integrated
Applications", Agent-SafetyBench, Progent, Authenticated Delegation, Prompt Infection, Open
Challenges in Multi-Agent Security, Design Patterns for Securing LLM Agents, Commercial LLM
Agents Are Already Vulnerable, A Trembling House of Cards, Governing AI Agents, Fully
Autonomous AI Agents Should Not Be Developed, Agentic AI Needs a Systems Theory, Sleeper
Agents, and the arXiv surveys. Several are excellent; bring one back only if it gets published
or if no peer-reviewed paper covers the slot.

Maintain this file as the annual reading-list document. Diff it against the live
`current/syllabus.html` before each offering.

---

## 3b. Schedule Table Conventions

Moved out of `current/syllabus.html` on 2026-09-18: HTML comments are served to the browser and
are visible in view-source, so instructor notes do not belong in a published page.

**Row colours**, matched to the other course sites:

| Colour | Meaning |
|---|---|
| `#FFB500` | part header |
| *(none)* | ordinary lecture, in person |
| `#F7A162` | project presentation day (same as CS 578) |
| `#FAE0D6` | no class — prep for a presentation |
| `#FFE8EA` | no class — holiday, and finals week (same as MLSec) |
| `#E8F4FF` | session held online (same as MLSec) |

**To move a lecture online** (every lecture is currently in person):

1. On that `<tr>`, add `style="background-color: #E8F4FF;"`
2. Change the Mode cell to `<td><b>Online</b></td>`
3. For an asynchronous session, append `<span class="badge badge-info">(Async)</span>`

Do not put this back into the HTML as a comment.

---

## 4. Week 1 Lecture Outline — Foundations of Agentic AI Systems

**Central question: what transforms an LLM into an agent?**
This is an overview lecture, not a security lecture. Resist the urge to open with attacks.
Students should leave with a systems-level mental model they can later annotate with trust
boundaries.

### Session 1 (Wed 09/23) — From LLMs to Agents

1. **Course logistics** (15 min) — grading, why no homework, why an online final,
   critique and discussion sign-ups.
2. **What a language model is, as a system component** (15 min) — a stateless function from
   context to token distribution. Everything else is scaffolding. This framing pays off all
   term: the model has no notion of who wrote which part of its context.
3. **The agent loop** (25 min) — observe → reason → act → observe. Draw it on the board and
   leave it up; every later lecture annotates this diagram.
4. **Reasoning and planning** (20 min) — chain of thought, decomposition, ReAct's
   interleaving of reasoning traces and actions. Why interleaving helps, and what it means
   that an observation can now steer reasoning.
5. **Tool use and function calling** (25 min) — Toolformer and learned tool invocation
   versus schema-driven function calling. What a "tool" actually is: an arbitrary
   side-effecting function the model selects by name.
6. **Closing hook** (10 min) — one worked example of an agent doing something useful,
   traced through the loop. Ask the class where they would attack it. Do not answer; that
   is Week 2.

### Session 2 (Mon 09/28) — Agent Architectures

1. **Environment interaction** (15 min) — browsers, filesystems, shells, APIs. The
   environment is an input channel the agent's developer does not control.
2. **Retrieval** (20 min) — RAG as context construction; the retrieval corpus as an
   attacker-writable surface (foreshadow only).
3. **Memory** (30 min) — short-term (context window) versus long-term (external store).
   MemGPT's OS analogy: paging, eviction, and a memory hierarchy managed by the model
   itself. Emphasize that the model both reads and *writes* this store.
4. **Reflection and self-improvement** (15 min) — Reflexion; verbal reinforcement; agents
   that modify their own future prompts.
5. **Single- versus multi-agent systems** (20 min) — Generative Agents as the canonical
   demonstration; role specialization; agent-to-agent messages as a data channel.
6. **Autonomy and delegated action** (10 min) — the spectrum from suggestion to execution.
   Introduce the term *delegated authority*; it is the spine of Week 2.

**Board artifact to keep:** a single labeled diagram — model, loop, tools, environment,
retrieval, memory, other agents — which Week 2 re-draws with trust boundaries overlaid.

---

## 5. Week 2 Lecture Outline — Threat Modeling Agentic AI Systems

**Central question: why does adding tools, state, and autonomy change the security model?**

### Session 3 (Wed 09/30) — Assets, Adversaries, Trust Boundaries

1. **Recap: the Week 1 diagram** (10 min) — redraw it, then ask the class to place the
   boundaries before you do.
2. **Assets** (15 min) — what is actually worth protecting: user credentials and tokens,
   the tool-invocation capability itself, memory integrity, the confidentiality of context,
   and the user's downstream resources. Note that the model's weights are usually *not* the
   asset here.
3. **Adversaries** (20 min) — a taxonomy by position rather than by capability: the
   malicious user, the malicious third party who controls content the agent reads, the
   malicious tool or tool provider, the malicious peer agent, the compromised memory store.
   Each gets a different column all term.
4. **Trust boundaries** (30 min) — the core lecture. Where does data cross from untrusted
   to trusted? Key observation: in a conventional system, a trust boundary is a place in the
   code. In an agent, it is a place in the *context*, and the context has no type system.
   Instructions and data are the same tokens.
5. **Untrusted observations** (20 min) — anything the agent reads is adversary-controlled
   until proven otherwise: web pages, tool outputs, retrieved documents, other agents'
   messages, its own memory.
6. **Framing for the term** (10 min) — introduce Agent Security Bench's decomposition and
   the "Trembling House of Cards" attack map as two competing organizations of the same
   space; ask which one the class finds more useful and why.

### Session 4 (Mon 10/05) — Privilege, State, and Security Properties

1. **Delegated authority** (25 min) — the agent holds the user's privileges, but not the
   user's judgment. Introduce the confused-deputy framing early, informally; Week 4 makes
   it precise. Distinguish authentication (the agent is who it says) from authorization
   (the agent may do this).
2. **Persistent state as a security property** (20 min) — once the agent writes to memory,
   a one-time compromise becomes a durable one. Contrast with stateless prompt attacks.
   Introduce the recovery question: how do you clean an agent?
3. **Unsafe actions versus incorrect outputs** (25 min) — the central distinction of the
   course. Work through cases where the agent's output is *correct* and the action is
   *unsafe*, and vice versa. Argue that safety benchmarks measuring output quality do not
   measure this.
4. **Security properties, stated precisely** (20 min) — integrity of the instruction
   channel, confidentiality of context, authorization of actions, non-persistence of
   compromise, auditability of the trace. Give each a one-line formal-ish statement.
   Students will reuse these on the final exam.
5. **Live exercise** (20 min) — hand out one real agent product's architecture; students
   threat-model it in pairs for 10 minutes, then compare boundaries. This doubles as
   calibration for the Q1/Q2 exam format.

**Deliverable framing:** at the end of this session, students should be able to write the
threat-model section of their project proposal, due 10/21.

---

## 6. Open Decisions

- [ ] **Course number.** Currently CS 599 (special topics); AI 539 is not assigned. Decide whether to
      pursue a permanent number before the second offering.
- [ ] **Three project presentations** (10/19, 11/16, 12/02), each preceded by a cancelled prep
      session (10/14, 11/11, 11/30). This follows CS 578. It costs five lecture slots, so four
      topics dropped to a single session — see `SAIS-SYLLABUS.md` §7.
- [ ] **Meeting pattern and room.** Site currently says "MW (time TBA), Room TBA."
      All schedule rows are `In-person`; `current/syllabus.html` carries an HTML comment
      with the exact edit to flip any row to `Online` if the course goes hybrid.
- [ ] **Office hours.** TBA on the site.
- [ ] **Final exam window.** Currently 12/07 00:00 – 12/09 23:59, 3-hour limit once
      started. Confirm against the registrar's finals schedule for the term.
- [ ] **Written syllabus.** Draft in `SAIS-SYLLABUS.md`; open items listed in its §10.
- [ ] **Google Sheet** for team and discussion sign-up: create and link from Canvas
      (the site refers to it without a URL, deliberately).
- [ ] **Practice exam question** with worked answer, to be posted on Canvas on 11/16.
      Exam design now lives in `SAIS-FINAL-EXAM.md`; `current/exam.html` was removed and the
      site mentions the exam only in the grading list and the finals-week schedule row.
- [ ] **Course listing.** The `_data/courses.yml` entry is written but commented out.
      Uncomment when the course is approved, and add
      `assets/images/courses/course-sais.jpg`.
- [ ] **Enrollment cap.** Discussion sign-up is ≤ 2 students across the eleven lecture days
      10/05–11/23, i.e. **22 slots**. Above that, add a third slot per day.
