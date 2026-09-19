# Online Final Exam — CS 599, Secure Agentic AI Systems

**Course development document — not published on the course website.**
Fall 2027 · 25% of the course grade · Instructor: Sanghyun Hong

> This file replaces the former `current/exam.html`, which was removed from the site on
> 2026-09-18. The public pages now mention the exam only in the grading list and in the
> finals-week row of `current/syllabus.html`. If you decide to publish exam details later,
> rebuild the page from this file and re-add a `Final Exam` nav item to all four pages.

---

## 1. Logistics

| | |
|---|---|
| **Where** | Canvas. Online only — there is no in-person exam session. |
| **Window** | Opens **Mon. 12/07, 12:00 am**; closes **Wed. 12/09, 11:59 pm**. |
| **Duration** | **3 hours** once begun. Students choose when to start within the window. |
| **Materials** | **Open-note, open-paper.** Any course reading, their own notes, their own critiques. |
| **Not allowed** | Generative AI tools of any kind; any communication with another person about the exam. |
| **Coverage** | Cumulative — Parts I–V, 09/23 through 11/30. |

**Open confirmation:** the 12/07–12/09 window is my choice, not the registrar's. Check it
against the official finals schedule for the term before publishing.

---

## 2. Design Rationale

The exam tests **security reasoning**, not recall. Every question presents a system, an
attack, a defense, or an experiment the student has not seen before, and asks them to reason
about it using the framework the course builds. No question asks which dataset a paper used,
how many tools AgentDojo ships, or what an acronym stands for.

**Why open-note:** because looking things up will not help. The questions are designed so the
answer is not in any paper — it is in the transfer from the papers to a new system. A student
who read the papers and thought about them finishes comfortably; a student opening a PDF for
the first time runs out of time.

This is also why the exam can be online and unproctored without much loss. The failure mode
to design against is not the open book, it is the language model, which is why generative AI
is excluded and why Q2/Q4/Q6 are anchored to a specific artifact supplied in the prompt.

---

## 3. Structure — six questions, 100 points

### Q1 — Agent Architecture (15 pts)

Given an unfamiliar agent architecture:

- identify the system components and how control and data flow between them;
- identify the trust boundaries;
- identify the high-value assets;
- state the security assumptions the design relies on.

### Q2 — Threat Modeling (20 pts)

Given an agent application:

- define realistic adversary capabilities and knowledge;
- enumerate the attack surfaces;
- construct at least two concrete attack paths from entry point to impact.

### Q3 — Attack Analysis (15 pts)

Given a hypothetical attack:

- explain why it succeeds;
- name the security assumption it violates;
- describe variants that would survive an obvious patch.

### Q4 — Defense Design (20 pts)

Design an architectural or runtime defense for a given system, and discuss:

- the enforcement point, and why it belongs there;
- the security benefit, stated as a property;
- limitations — what it does not stop;
- false positives and utility impact.

### Q5 — Security Evaluation (20 pts)

Critique an experimental design. Identify:

- missing baselines;
- weak or convenient assumptions;
- inappropriate metrics;
- the missing adaptive attack;
- and propose one experiment that would settle the question.

### Q6 — Human Oversight (10 pts)

Given a trace of agent actions:

- determine what a human supervisor should have been shown;
- identify the point at which intervention became appropriate;
- argue whether more transparency would actually have helped, or merely produced more to ignore.

---

## 4. Grading Rubric

Every question is graded on the same four-band scale, scaled to that question's point value.
There is no single right answer to any of these; there are defensible answers and
indefensible ones.

| Band | Share | Description |
|---|---:|---|
| **Excellent** | 90–100% | Reasoning is correct, specific to the system given, and complete. Assumptions are stated. The answer anticipates the obvious objection and addresses it. Tradeoffs are named rather than avoided. |
| **Proficient** | 75–89% | Reasoning is sound and grounded in the specific system, but incomplete — a trust boundary is missed, a limitation is glossed over, or a tradeoff is asserted without support. |
| **Developing** | 50–74% | Course concepts recalled correctly but applied generically. The answer would read the same for a different system. Attack paths are named but not traced end to end. |
| **Insufficient** | 0–49% | Restates course material without applying it, misidentifies the trust boundaries, or proposes a defense that does not address the stated threat model. |

### What earns credit

- **Specificity.** "Sanitize the tool output" is not a defense. "Mediate tool outputs through
  a parser that strips imperative content before they enter the planning context, enforced at
  the tool-return boundary" is a defense you can then poke holes in.
- **Stated assumptions.** If a question is underspecified, say what you are assuming and
  answer under that assumption. This earns credit; guessing silently does not.
- **Honest tradeoffs.** Every defense in this course costs utility. An answer claiming
  otherwise is wrong.
- **Brevity.** Length is not a proxy for quality. A precise half page beats three vague ones,
  and there is a time limit.

---

## 5. Student-Facing Preparation Advice

To be posted on Canvas rather than on the website:

- Reread your own paper critiques. The threat-model field and the adaptive-attack field are
  the exam (Q2 and Q5).
- Pick an agentic system you use and threat-model it from scratch, on paper, without looking
  anything up.
- For each defense in Part IV, write down in one sentence what it does *not* stop.
- A practice question with a worked answer is posted on Canvas on 11/16.

---

## 6. To Do Before the First Offering

- [ ] Confirm the exam window against the registrar's finals schedule.
- [ ] Write the practice question + worked answer (due on Canvas 11/16).
- [ ] Source six unseen artifacts — one architecture (Q1), one application (Q2), one attack
      (Q3), one system to defend (Q4), one experimental design (Q5), one action trace (Q6).
      Prefer real products and real papers published *after* the reading list was fixed, so
      nothing is a recall exercise.
- [ ] Decide Canvas delivery: single timed quiz with essay questions vs. a released PDF with
      a Canvas upload. The 3-hour limit is easier to enforce with the former.
- [ ] Write the answer key at the same time as the questions. If an answer key is hard to
      write, the question is underspecified.
