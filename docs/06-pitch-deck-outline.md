# 06 · Pitch Deck Outline (12 slides)

Deliverable: [`../pitch-deck/index.html`](../pitch-deck/index.html). One HTML file, keyboard-navigable, works offline.

Design principles:

- **English primary**, no clutter
- **One idea per slide.** The judge should be able to paraphrase the whole deck in three sentences after one read.
- **Deliberation is the visual motif.** The four-agent grid appears on 6 of the 12 slides.
- **No stock photos.** Every visual is either a diagram, a data element, or a screenshot of the prototype.

## Slide 1 — Cover

- Wordmark: **Nadi**
- Tagline: *A team of AI agents that think out loud before they advise you on health.*
- Subtitle: *For the Dubai Create AI Agents Championship · Best Personal AI Agent*
- Small mark in the corner: *Nadi · October 2026*

## Slide 2 — The Problem

**"Every health app talks. None of them argue."**

Three facts:

- The consumer health-AI category is crowded. Every funded product in 2026 looks like a chatbot.
- Chatbots are one voice. Your health is too important for one voice.
- Users can't tell whether an AI is thinking hard or just agreeing.

## Slide 3 — The Insight

**"The winning health agent isn't the one that answers best. It's the one whose reasoning you can see."**

- Reasoning is a *product feature*, not a technical detail
- Visibility is a *safety* feature
- Multi-agent deliberation is the current best-in-class way to deliver both

## Slide 4 — The Solution

**"Nadi is a team of four agents."**

Diagram of Planner / Executor / Critic / Guardian, each with a one-line role.

> **You watch the team meet before they advise you.**

## Slide 5 — How It Works (the ritual)

A single user message → the four-agent pipeline → a consensus answer.

The four columns of deliberation, in order, with sample lines from each agent.

At the bottom: *"Confidence 74% · 6 sources · 0 red flags"* — the visible safety signature.

## Slide 6 — Why This Wins (against the field)

A single comparison table.

| | POP (2025 winner) | YC health agents | Uoma | **Nadi** |
|---|---|---|---|---|
| Core ritual | Pop the pill | Protocol reminders | Narrative therapy | **Team deliberation** |
| Reasoning visibility | High | Low | Low | **Very high** |
| Cultural depth | Universal | Universal | Universal | **Multi-source evidence** |
| Safety posture | Adherence | Consumer | Therapy | **Guardian agent** |

## Slide 7 — The Technology (short, honest)

- Small, focused agent team (Planner, Executor, Critic, Guardian)
- Declarative safety policy, tested against 30 adversarial prompts
- Curated knowledge library (15 articles, 8 ancient-text entries) — not 100 million web pages
- Local-first, session-scoped state
- Runs in under 8 seconds per deliberation on consumer hardware

No hype. No "we use the latest LLM". Just "we made a team that shows its work".

## Slide 8 — The Demonstration

- Screenshot of the agent-team page
- Live demo video is linked on the submission page
- 90-second preview video embedded (or link to it)

## Slide 9 — Safety & Ethics

**"Nadi does not diagnose. Nadi does not prescribe. Nadi never lies about what it knows."**

- Guardian blocks acute-symptom misdiagnosis, medication changes, diagnostic language
- Every claim cites an evidence ID; ungrounded claims are blocked at the pipeline level
- Confidence is displayed; insufficient evidence returns "insufficient evidence", not a hedged guess
- Data is session-scoped, local-first, no training on user PHI without explicit consent

## Slide 10 — Where We Are Today

- **Prototype running**: multi-agent team with Planner, Executor, Critic, Guardian
- **Knowledge library**: 15 curated entries, 8 ancient-text entries (all public domain)
- **Safety test suite**: 30 adversarial prompts, Guardian catch rate tracked in CI
- **Frontend**: 3-page demo (Home, Agent Team, History)
- **Status**: prototype, not commercially released, no users

## Slide 11 — The Roadmap (2027)

- Q1 2027: Grand Final, mentorship, expand knowledge library to 60 entries
- Q2 2027: Closed pilot with 20 users, iterate on safety policy
- Q3 2027: Wearable integrations (Apple Health import, Huawei Health), Arabic UX
- Q4 2027: Public beta, decision point on commercialisation

## Slide 12 — The Ask

- Mentorship and Digital Academy access
- The AED 550,000 grant, if Nadi is a category winner
- A pilot partner in Dubai's health ecosystem to move from prototype to evidence

**Contact**: *(fill in at registration)*

---

## Design notes

- **Fonts**: Inter (body) + Fraunces (display) — the pairing used by Stripe and The Pudding, both clean
- **Palette**: see [`../branding/palette.md`](../branding/palette.md)
- **Animations**: none. Judges should be able to screenshot any slide.
- **Export**: `python -m http.server 8000 --directory pitch-deck` for preview; print-to-PDF for a still-image fallback
