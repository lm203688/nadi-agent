# Summary Report — Nadi

**Entry to:** Dubai Create AI Agents Championship 2026
**Track:** Best Personal AI Agent
**Repository:** https://github.com/lm203688/nadi-agent
**Frontend (once GitHub Pages is enabled):** https://lm203688.github.io/nadi-agent/

---

## 1. What Nadi is

Nadi is a **team of four AI agents that work together to answer your health question**. When you ask, they do not just reply — they deliberate in the open. A planner reads your question, an executor looks up evidence, a critic challenges the executor's draft, and a guardian checks the answer against a fixed set of safety rules before anything reaches you. You see the whole conversation. Every answer ships with the trace that produced it.

The project name is a coincidence that works for us: *nāḍī* means "pulse" in Arabic, and *nāḍī* also means "life-stream" in Sanskrit. It is a small hint that the tool sits between two medical traditions — modern evidence and traditional knowledge — and treats them as evidence, not as folklore.

## 2. Why this is a personal AI agent (not a chatbot)

A chatbot answers one user, one question. Nadi is one agent that has four roles, and it remembers the roles, the evidence, and its own past decisions. That is what makes it personal — it keeps a coherent record of who you are (age, chronic conditions, medications, prior refusals) and it will not silently contradict itself from session to session. The audit trail at `/history.html` is what a personal agent owes you.

## 3. The four agents and what each one does

| Agent | Role | What it produces |
|---|---|---|
| **Planner** | Understands the question, decides which evidence is needed | A short list of what to look up |
| **Executor** | Retrieves modern RCTs and traditional texts, drafts a candidate answer | A claim with citations and a confidence score |
| **Critic** | Challenges the draft, forces at least one objection per turn | A critique that must land somewhere before we go on |
| **Guardian** | Runs the answer through five fixed categories of safety rules | A pass / defer / block / override decision |

Guardian is the load-bearing part of the whole system. It is not a prompt, it is code — a small set of regular-expression rules that sit after every answer. In this prototype it is deliberately small and readable so a judge can inspect every rule and reproduce every decision. A production build would swap it for a classifier-based guardrail, but the demonstration is complete: Guardian cannot be bypassed by phrasing.

## 4. What we have built (all of it is in this repository)

- `docs/01` to `docs/09` — the strategy, product, architecture, eligibility, deck outline, demo script, content plan, and risk register
- `compliance/` — three documents covering eligibility, IP disclosure, and data governance
- `branding/` — the visual identity (a pulse-wave logo in warm neutrals, deliberately not the blue-and-purple of generic health AI)
- `pitch-deck/index.html` — a 12-slide HTML deck, keyboard-navigable
- `demo-video/` — a 2:20 demo script, a 20-shot storyboard, and 41 subtitle lines ready to render
- `prototype/` — the runnable four-agent prototype (Python standard library only). Includes a 30-case adversarial benchmark that all pass on this machine
- `frontend/` — three pages: home, agent-team (the live deliberation, eight prompt examples), and history (the audit trail with filters and stats)

## 5. What the demo shows

The Agent Team page (`frontend/agent-team.html`) has eight prompt examples. Click any of them and you watch the four agents work in real time. The prompts are chosen to hit different outcomes:

- **Fatima, 34, type 2 diabetes** — asks about sleep and glucose. All four agents agree; answer passes with citations.
- **Acute chest pain** — Guardian fires `acute_symptom` and defers to clinician.
- **Request to change a prescription dose** — Guardian fires `medication_change` and blocks.
- **"Give me a diagnosis"** — Guardian fires `diagnostic_language` and overrides.
- **5-year-old child** — Guardian fires `high_risk_population` and overrides.
- **Borderline lab values** — Guardian fires `abnormal_lab` and defers.

You can run the same eight prompts against the prototype yourself:

```bash
cd prototype
python -m nadi_agent.benchmark   # 30/30 pass
python -m nadi_agent.demo        # five demo scenarios
python -m nadi_agent.server --port 8000   # HTTP API
```

## 6. What is original vs reused

Everything in this repository is written for this competition. The four-agent architecture and the Guardian ruleset are new. The product identity (name, brand, palette, agent-team visual) is new. The demo scenarios and the knowledge base entries are new.

We reuse from an internal project — the HealthLens codebase — only the shape of the plumbing: how to log a session, how to structure an agent-to-agent message, how to store an audit entry. Those are structural patterns, not product assets. Nothing is copied from HealthLens's user data, brand, payment surface, or the ~700 ancient Chinese medical texts it uses.

## 7. Eligibility

Nadi is a new AI-agent capability developed for this championship. It is not a commercialised product. It has no revenue, no paid users, and no public deployment. It is a prototype whose demonstration is the point.

Full disclosure lives in:
- `compliance/eligibility-statement.md`
- `compliance/ip-disclosure.md`
- `compliance/data-governance.md`

## 8. What the entry asks for from the judges

1. Open `https://lm203688.github.io/nadi-agent/agent-team.html`.
2. Click **Fatima** — watch a safe question pass with a full trace.
3. Click **Chest pain** — watch Guardian defer.
4. Click **Prescription change** — watch Guardian block.
5. Click **Diagnosis** — watch Guardian override.
6. Click **Child** — watch Guardian override.
7. Click **Lab** — watch Guardian defer.
8. Open `https://lm203688.github.io/nadi-agent/pitch-deck/` for the 12-slide story.
9. Open `https://github.com/lm203688/nadi-agent` and read `prototype/nadi_agent/core.py` — the Guardian rules are ~40 lines of regex. Nothing to hide.

That is the whole pitch.

---

*Submitted October 2026 by the Nadi team. Feedback and correspondence on GitHub issues.*
