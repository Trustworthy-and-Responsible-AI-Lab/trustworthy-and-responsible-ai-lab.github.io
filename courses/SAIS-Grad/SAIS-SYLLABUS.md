# Written Syllabus — CS 599: Secure Agentic AI Systems

**Working draft. Not published on the course website.**
Attacks, Defenses, and Human Oversight · Fall 2027 · 4 credits · Graduate

> **What this file is for.** The course website (`current/`) is the student-facing version and
> stays the source of truth for dates and deliverables. This file is the *written* syllabus —
> the single document that goes to Canvas, to the curriculum committee, and to anyone who asks
> for "the syllabus" as a file. Finish it when the term details (time, room, office hours) are
> settled.
>
> **Rule:** anything factual here — dates, weights, deadlines — must match
> `current/index.html`, `current/syllabus.html`, `current/critiques.html`, and
> `current/project.html`. After editing either side, grep both for the fact you changed.
>
> Items marked **`[TBD]`** are the only things still undecided. Everything else is settled
> and copied from the live site.

---

## 1. Course Identification

| | |
|---|---|
| **Number** | CS 599 (special topics). **AI 539 is not assigned to this course** — do not advertise it. `[TBD]` permanent number, if pursued |
| **Title** | Secure Agentic AI Systems: Attacks, Defenses, and Human Oversight |
| **Credits** | 4 |
| **Level** | Graduate |
| **Term** | Fall 2027 — classes 09/23 – 12/04; finals week 12/07 – 12/11 |
| **Meeting pattern** | MW, `[TBD]` time |
| **Location** | `[TBD]` room. All sessions in person. |
| **Format** | Lecture + student-led paper discussion. No labs, no weekly homework. |
| **Course website** | https://true-lab.ai/courses/SAIS-Grad/current/ — four pages: Home, Syllabus, Critique/Discussion, Project |
| **Everything is submitted on** | Canvas |

**Instructor.** Sanghyun Hong · sanghyun.hong@oregonstate.edu · 2029 KEC (Kelley Engineering
Center) · https://www.sanghyun-hong.com
**Office hours.** `[TBD]`. No office hours in the first week. Subject to change at the
instructor's discretion.

---

## 2. Catalog Description

Studies the security of AI systems that act autonomously on behalf of users. Modern AI agents
reason, plan, invoke tools, maintain memory, retrieve external content, and communicate with
other agents, and each of these capabilities opens an attack surface that conventional machine
learning security does not cover. The course examines agentic AI security from three
perspectives: attacks on agent reasoning, tool use, memory, external content, inter-agent
communication, and delegated authority; architectural and runtime defenses including
isolation, mediation, least privilege, provenance, and containment; and the human oversight
required to supervise increasingly autonomous systems. Students construct threat models for
agent architectures, evaluate published security claims against adaptive adversaries, and
complete a research project. Organized around recent research papers. Graduate standing and
CS 434 or equivalent; a prior course in security is recommended.

*(128 words. The long-form proposal description lives in `SAIS-PROPOSAL.md` §2.)*

---

## 3. Prerequisites

Graduate standing, plus a basic understanding of machine learning:

- **CS 434: Machine Learning and Data Mining — required.**
- CS 499/599 | AI 539: Trustworthy ML — recommended.
- CS 578: Cyber-Security — recommended.

Students should be comfortable with the idea that a system's security depends on where its
trust boundaries are drawn, not on how good its model is.

---

## 4. Measurable Student Learning Outcomes

By the end of the course, students will be able to:

1. **Explain** how reasoning, planning, tool use, memory, retrieval, and multi-agent
   interaction compose into modern agentic AI systems.
2. **Identify** assets, trust boundaries, privileges, data flows, external dependencies, and
   security assumptions in an agentic AI architecture.
3. **Construct** threat models for adversaries targeting prompts, external content, tools,
   memory, communication channels, and other agents.
4. **Analyze** attacks including prompt injection, indirect prompt injection, malicious tool
   outputs, excessive agency, memory poisoning, privilege abuse, and inter-agent manipulation.
5. **Apply** security principles — least privilege, isolation, provenance, mediation,
   authorization, runtime monitoring, containment — to agentic AI systems.
6. **Evaluate** security claims using appropriate threat models, attack and utility metrics,
   adaptive attacks, and realistic experimental designs.
7. **Analyze** what information humans need to supervise autonomous agents, and determine when
   intervention is necessary.
8. **Critically evaluate** agent-security research and formulate new research questions.

### Outcome → assessment map

| Outcome | Paper discussions | Paper critiques | Final project | Final exam |
|---|:--:|:--:|:--:|:--:|
| 1. Compose agent systems | ● | | | ● (Q1) |
| 2. Identify trust boundaries | | ● | ● | ● (Q1) |
| 3. Construct threat models | | ● | ● | ● (Q2) |
| 4. Analyze attacks | ● | ● | ● | ● (Q3) |
| 5. Apply security principles | ● | | ● | ● (Q4) |
| 6. Evaluate security claims | ● | ● | ● | ● (Q5) |
| 7. Human oversight | ● | | | ● (Q6) |
| 8. Formulate research questions | ● | ● | ● | |

---

## 5. Evaluation of Student Performance

| Component | Weight | Details |
|---|---:|---|
| Paper discussions | 15% | One student-led session per student. `current/critiques.html` |
| Paper critiques | 20% | One per class, on Canvas. `current/critiques.html` |
| Final research project | 40% | Individual or teams of two. `current/project.html` |
| Online final exam | 25% | Cumulative, open-note. `SAIS-FINAL-EXAM.md` |
| **Total** | **100%** | |

**Extra credit, +5%:** submitting the final report to a workshop or conference. (A separate +2%
for discussion leadership was removed on 2026-09-18: the 15% band already *is* "outstanding",
so the two double-counted.)

**There is no separate participation grade** and **no homework.** Preparation and engagement
are assessed through the paper critiques and the student-led discussion. This is
deliberate: see `SAIS-PROPOSAL.md` for the reasoning.

### Grade scale — `[TBD]`

`[TBD]` Decide whether to state a scale at all, or to keep it at the instructor's discretion
as the other course sites do. If stated, the usual A ≥ 93, A− ≥ 90, B+ ≥ 87, … applies.

### 5.1 Paper Discussions (15%)

Each student leads the discussion **once**. From 10/05 on, the second half of each lecture day
belongs to the student leads; up to 2 students per day.

**Available days — the eleven lecture days 10/05 – 11/23** (10/05, 10/07, 10/12, 10/21, 10/26,
10/28, 11/02, 11/04, 11/09, 11/18, 11/23). The first two lectures fall before sign-up closes, so
they are instructor-led. That is **22 slots**; if enrollment exceeds it, add a third slot per day
and announce it on Canvas.

- Choose a paper relevant to that day's topic, from IEEE S&P, USENIX Security, ACM CCS, NDSS,
  NeurIPS, ICML, ICLR, OSDI, SOSP, or CHI (for the oversight sessions).
- The paper must **not** already be on the schedule. arXiv preprints from the last 12 months
  are allowed with prior approval.
- Sign-up opens 09/23 and closes 09/30, first come first served. Not signed up by 09/30 = 0 for
  this component.
- **Mandatory meeting with the instructor 3–4 days before**, with draft slides and 2–3
  discussion questions. Missing it costs 3% of this component.
- Slot: 25–30 min — 15 min presentation, 10–15 min discussion. Two per day fits a half-session.

| Score | Criterion |
|---:|---|
| 0% | No sign-up, or no presentation. |
| 7% | Signed up and presented, but the presentation or discussion lacked quality. |
| 12% | Presented a paper well and led a real discussion. |
| 15% | Outstanding: the room argued about something substantive and left with a question it did not have before. |

### 5.2 Paper Critiques (20%)

**One critique per lecture, submitted on Canvas before that class begins.** **No late
submissions; a missed critique is a zero.**

**Due on 13 days** — every lecture day 09/28 – 11/23 (09/28, 09/30, 10/05, 10/07, 10/12, 10/21,
10/26, 10/28, 11/02, 11/04, 11/09, 11/18, 11/23). **Not** due for the first class (09/23), the
three presentation days (10/19, 11/16, 12/02), or the four no-class days (10/14, 11/11, 11/25,
11/30). Rule students are given: if a schedule row lists required papers, a critique is due.

Each critique covers **one of the two required papers** for that day. Optional `(Opt)` papers
do not count. Required fields:

- Summary of the paper (a paragraph)
- Contributions (2–3 bullets)
- **Threat model** — who the adversary is, what they control, know, and want
- Strengths and weaknesses (2–3 each)
- **One adaptive attack or one missing experiment**
- Your opinions

Each critique is scored out of 2 and the term total is scaled to 20%: 0 = no submission or a
paraphrase of the abstract; 1 = a real effort to understand the paper and weigh its pros and
cons; 2 = an insightful comment. Full instructions on `current/critiques.html`.

> **Design note.** This started as four 5% critiques on a ten-question conference-review
> template (security problem · threat model · contribution · are the claims justified ·
> baselines · metrics · limiting assumptions · adaptive attack · missing experiment · next
> research question). It was changed on 2026-09-18 to a weekly critique matching CS 578 and
> Trustworthy ML. The two security-specific fields — threat model and adaptive attack — were
> kept because the final exam (Q2, Q5) and the project proposal both build on them. If you
> ever want the long form back, it is the ten questions above, at 1.5–2 pages, four times a
> term.

### 5.3 Final Research Project (40%)

Individually or in teams of two; a solo project is held to the same standard. Preferred arc:
**Problem → Threat Model → Attack or Failure → Mechanism → Evaluation.**

| Due | Milestone | Weight |
|---|---|---:|
| 09/30 | Team sign-up (−2% if not on the sheet) | — |
| 10/19 | **Checkpoint Presentation 1** — 10 min + 5 min Q&A; problem, related work, explicit threat model, next steps | 10% |
| 11/16 | **Checkpoint Presentation 2** — 10 min + 5 min Q&A; experiment design, preliminary results, next steps | 10% |
| 12/02 | **Final Presentation** — 15 min + 5 min Q&A, in class. Last class of the term | 20% |
| 12/11 | **Final report** (6–8 pages, report template) | *(included above)* |

The 20% covers the final presentation and the write-up together. The limitations section is
graded. The class session before each presentation (10/14, 11/11, 11/30) is cancelled for
preparation. Full instructions on `current/project.html`.

**Extra credit, +5%:** submitting the final report to a workshop or conference.

### 5.4 Online Final Exam (25%)

Cumulative, covering Parts I–V (09/23 – 11/30). Canvas, online only, **open-note and
open-paper**; **no generative AI tools**. Window 12/07 12:00 am – 12/09 11:59 pm `[TBD: confirm
against registrar]`, 3 hours once begun.

Six scenario-based questions, 100 points: agent architecture 15 · threat modeling 20 · attack
analysis 15 · defense design 20 · security evaluation 20 · human oversight 10. Each graded on a
four-band rubric (Excellent / Proficient / Developing / Insufficient). The exam tests security
reasoning, not recall. Full design in `SAIS-FINAL-EXAM.md`.

---

## 6. Required Materials

**No required textbook.** All required readings are research papers, linked from
`current/syllabus.html`: two required papers and one optional paper per lecture. They come from top-tier security and ML venues (IEEE S&P, USENIX Security, CCS,
NDSS, ESORICS; NeurIPS, ICML, ICLR) plus ACL, CHI, UIST and FAccT where the work belongs there;
only **3 of 42 entries are preprints**, in subareas with no published equivalent — see
`SAIS-PROPOSAL.md` §3 for the venue rule. The venue is *not* printed on the course page; it is
the selection criterion, not something students need to read. Preprints and proceedings are free; the CHI and
Human Factors papers are reachable through the OSU library.

Background for students new to agents — trimmed to two on 2026-09-18, because the longer list
duplicated papers that are already optional readings on the schedule:

- *A Survey on LLM-Based Autonomous Agents* — arXiv:2308.11432
- OWASP Agentic AI — Threats and Mitigations — https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/

**Technology.** A computer with internet access for Canvas and the online final exam. No
compute is required by the course itself; project teams needing GPUs should talk to the
instructor early.

---

## 7. Course Content and Schedule

The authoritative, dated schedule is `current/syllabus.html`. Summary:

| Part | Sessions | Topics |
|---|---|---|
| **I. Foundations of Agentic AI Systems** | 09/23, 09/28 | LLMs vs. agents, the agent loop, reasoning and planning, tool use; retrieval, memory, reflection, single- vs. multi-agent, delegated action |
| **II. Threat Modeling** | 09/30, 10/05 | Assets, adversaries, trust boundaries, untrusted observations, agent privileges; delegated authority, persistent state, security properties, unsafe actions vs. incorrect outputs |
| **III. Attacks** | 10/07, 10/12, 10/21, 10/26, 10/28 | Prompt injection (direct, indirect, environmental); tools, privileges, and authorization; memory, state, and persistent compromise; multi-agent security |
| **IV. Defenses** | 11/02, 11/04 | Architectural defenses — isolation, mediation, information flow; model-level and runtime defenses, firewalls, containment |
| **V. Evaluation, Oversight, Frontier** | 11/09, 11/18, 11/23 | Evaluating agent security; human oversight and agentic-system literacy; frontier problems |
| **Project presentations** | 10/19, 11/16, 12/02 | Checkpoint 1, Checkpoint 2, Final |
| **Finals week** | 12/07 – 12/11 | Online final exam; final research paper due 12/11 |

**No class:** 10/14 (Checkpoint 1 prep), 11/11 (Veterans Day, also Checkpoint 2 prep),
11/25 (Thanksgiving Break), 11/30 (Final presentation prep).

That leaves **14 lecture sessions** for ten topics, which is why Tools/Privileges, Memory,
Multi-Agent Security, and Evaluation each get one session rather than two. If the three
project presentations ever come out, those four topics are the first to expand again.

The 11/23 frontier-problems reading list is re-selected each offering from papers published in
the previous 12 months and is deliberately not fixed in this document. See `SAIS-PROPOSAL.md`
§3.

---

## 8. Course Policies

### Expectations

This is a graduate research seminar. The reading is the course. Expect 2–3 hours per paper
once you are used to the format; you may need to skim cited papers to judge whether a
contribution is real. Come prepared to argue with the authors — it is their job to convince
you, not yours to accept them.

### Academic Integrity

The University's Code of Academic Integrity applies (https://beav.es/codeofconduct), modified
as follows.

**Don'ts**
- Do **not** share your critique or write-up with others before the deadline.
- Do **not** copy and paste someone else's text, figures, or code into yours.
- Do **not** submit a critique that is a paraphrase of the paper's abstract, an existing public
  review, or a model-generated summary.

**Do's**
- **Brainstorm** your ideas with other students.
- **Discuss** and argue about the papers with other students — that is the point of the course.
- **Collaborate** with your project partner on the design, experiments, and write-up.

**Must:** write down the names of students who helped you. It will not affect your score. You
will learn from this practice how to credit others for their contributions.

### Use of Generative AI

This is a course about AI agents, so let us be precise about using them.

- **Permitted** for the final research project — code, experiment scaffolding, literature
  search, copy-editing — and for understanding background material.
- **Not permitted** to produce the substance of your paper critiques, or any part of the
  final exam.
- **Disclosure is mandatory** whenever such a tool is used on a graded artifact. In the
  submission itself, state (1) which tool, (2) what kind of interaction — brainstorming,
  drafting, debugging, editing — and (3) which portion of the work it contributed to.
  Undisclosed use is an academic integrity violation.
- You remain fully responsible for every claim in anything you submit, including claims a tool
  produced.

Written against the EECS guidance:
https://engineering.oregonstate.edu/EECS/MyEECS/EECS-guidance-drafting-ai-use-policies

### Late Work

- **Paper critiques:** no late submissions, ever. A missed critique is a zero.
- **Project:** presentations are in class, so lateness does not arise. The 12/11 report deadline
  is stated as **firm** on `current/project.html`, with "talk to me before 12/11" as the escape
  hatch. `[TBD]` whether to add an explicit penalty schedule.
- **Final exam:** the window is the window.

### Attendance

`[TBD]` Attendance is not graded (there is no participation grade), but the student-led
discussion format only works if people are there. Decide whether to say anything stronger.

---

## 9. Required University Statements

Copy verbatim from `current/index.html`, which carries the current approved wording:

- **Statement Regarding Students with Disabilities** (DAS, 541-737-4098,
  https://ds.oregonstate.edu/, disability.services@oregonstate.edu)
- **Reach Out for Success** (https://counseling.oregonstate.edu/reach-out; Suicide & Crisis
  Lifeline 988)
- **Academic Calendar and Student Bill of Rights**
  (https://registrar.oregonstate.edu/osu-academic-calendar;
  https://asosu.oregonstate.edu/advocacy/rights)

Re-check these against the Registrar's current required-statements page before each offering;
the wording is updated periodically.

---

## 10. Open Items Before This Document Ships

- [ ] Meeting time and room.
- [ ] Office hours.
- [ ] Confirm the final exam window against the registrar's finals schedule.
- [ ] Decide the late policy for project milestones (§8).
- [ ] Decide whether to state a grade scale (§5).
- [ ] Decide whether to say anything about attendance (§8).
- [ ] Course number: keep CS 599 (special topics), or pursue a permanent number. AI 539 is
      *not* cross-listed to this course.
- [ ] Create the Google Sheet for team and discussion sign-up; link it from Canvas.
- [ ] Refresh the 11/30 reading list from the previous 12 months.
- [ ] Re-verify the required university statements against the Registrar's page.
- [ ] Final consistency pass: grep this file and all four pages in `current/` for every date,
      weight, and deadline, and reconcile.
