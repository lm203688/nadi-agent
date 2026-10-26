# 02 · Product

## The product in one screen

One screen. Four columns. One conversation.

```
┌────────────────────────────────────────────────────────────────────┐
│  Nadi · Health Team                                                │
│                                                                    │
│  YOU ── "I keep waking up tired after 3pm, my fasting glucose     │
│        keeps creeping up."                                         │
│                                                                    │
│  ┌─ Planner ──┐  ┌─ Executor ─┐  ┌─ Critic ──┐  ┌─ Guardian ──┐ │
│  │ "How long   │  │ "Wrist HRV │  │ "You're   │  │ "Nothing     │ │
│  │  has this   │  │  ↓ 12% in  │  │  skipping │  │  acute. No   │ │
│  │  been going │  │  last 6 w."│  │  the fact │  │  red-line    │ │
│  │  on? Any    │  │ Pulses →   │  │  that I   │  │  triggered." │ │
│  │  recent     │  │  ancient   │  │  checked  │  │              │ │
│  │  stress?"   │  │  references│  │  cortisol │  │              │ │
│  │             │  │  on sleep- │  │  or       │  │              │ │
│  │             │  │  glucose   │  │  thyroid  │  │              │ │
│  │             │  │  links."   │  │  testing."│  │              │ │
│  └─────────────┘  └────────────┘  └────────────┘  └─────────────┘ │
│                                                                    │
│  ► Team consensus: try a 14-day morning-walk + light-eating       │
│    protocol. Re-check fasting glucose in 30 days.                 │
│  ► Confidence: 74% · Evidence: 6 sources · Red flags: 0            │
└────────────────────────────────────────────────────────────────────┘
```

That is the entire product. Everything else is supporting infrastructure.

## The ritual

The four-agent structure is not architecture theatre. It is the *ritual the user lives inside*. Every question you ask Nadi is a small public meeting:

1. **Planner frames** — clarifies your intent before any answer is generated. Prevents the "AI answers the wrong question" trap.
2. **Executor evidences** — pulls from user data, curated ancient-text library, structured knowledge, wearable streams. Every claim carries a citation.
3. **Critic challenges** — actively looks for the weakest link in Executor's proposal. This is the anti-hallucination layer.
4. **Guardian bounds** — a hard-coded safety supervisor. If any of the above steps proposes something that crosses a clinical red line (e.g. "stop your medication", "exercise through acute chest pain"), Guardian overrides.

The user sees the whole process. That is the point.

## User journeys (three demo personas)

### Persona A — the creeping-fasting-glucose user

> **Fatima, 38, Dubai, marketing lead.** No diagnosis. Worried she might be pre-diabetic.

- Input: text description + Apple Health / Huawei Health sync (wrist HRV, resting HR)
- Deliberation: Planner asks about sleep and stress · Executor pulls 6-week HRV trend · Critic flags "you haven't had bloodwork" · Guardian confirms no acute risk
- Output: 14-day lifestyle protocol + lab-test recommendation + re-check date

### Persona B — the post-treatment user

> **Ahmed, 46, Abu Dhabi, engineer.** Recently finished a course of medication. Wants to know how to stay healthy.

- Input: text + lab results upload + medication history
- Deliberation: Planner asks about the medication course · Executor references classical texts on gentle dietary principles · Critic pushes back on over-recommendation · **Guardian catches an acute-value flag** (K+ slightly elevated)
- Output: conservative dietary plan + "please see your doctor about this lab result" — *not* a diagnosis

### Persona C — the curious user

> **Yusuf, 29, student, interested in integrative approaches.** Wants to explore traditional frameworks.

- Input: text about general wellness + optional wearable data
- Deliberation: Planner asks what tradition interested him · Executor opens the ancient-text library (15 curated entries, not 700) · Critic flags where traditional advice conflicts with modern evidence · Guardian confirms no medical claims
- Output: a curated, sourced, culturally-accurate reading list + lifestyle pointers

All three personas go through the same four-agent pipeline. The difference is what each agent focuses on, not which agents run.

## Interaction model

### Ask mode (default)

User writes a free-text message. Team deliberates. Team returns a consensus answer with confidence and citations.

### Ask + Evidence mode

User attaches a wearable sync, a lab result PDF, or a photo of a tongue (multi-modal, opt-in). Executor gains those as additional sources.

### Follow-up mode

Every team response opens a persistent conversation. Subsequent questions are grounded in the previous consensus, not answered from scratch.

### Silent Guardian mode

Even when the user is not asking anything, Guardian runs in the background against the user's most recent check-in and alerts on threshold crossings. This is the daily check-in layer.

## What we deliberately do not do

- **We do not diagnose.** Nothing Nadi says is a diagnosis. Every output is explicitly framed as "consider discussing with a clinician".
- **We do not prescribe.** No medication advice. Guardian blocks it.
- **We do not accept clinical data for training without explicit consent.** Data governance is a first-class feature, not an afterthought.
- **We do not gamify health shame.** No calorie counting, no step-count leaderboards.

## What we do do

- **We make reasoning visible.** This is the product.
- **We make disagreement visible.** When Critic pushes back on Executor, you see it.
- **We make safety visible.** Guardian is not a hidden filter. It is an agent on the roster.
- **We cite every claim.** Every Executor statement carries a source ID.
- **We honour cultural context.** For a user whose health model is integrative, the ancient-text library is a real evidence source, not folklore.

## Success metrics for the prototype

We will not measure DAU at the demo stage. What matters:

- **Deliberation clarity** — every team response includes ≥1 Planner question, ≥1 Executor citation, ≥1 Critic challenge, ≥1 Guardian check
- **Safety catch rate** — in the built-in test set of 30 clinical-edge-case prompts, Guardian catches ≥28 (target: 95%+)
- **Citation grounding** — every Executor claim resolves to a real source ID; ungrounded claims must be 0%
- **Response time** — under 8 seconds per complete deliberation on the demo hardware

## Open questions for the Build phase

These are questions we expect the jury to ask in the May 2027 Grand Final, and we will have real answers by then:

1. How does Guardian distinguish "consider discussing with a clinician" from "diagnose and prescribe"? → Formalised policy file with per-category red-line definitions
2. How do we handle disagreement that Critic cannot resolve? → Team returns "insufficient evidence" explicitly, not a hedged guess
3. How does Nadi know when to stop deliberating? → Confidence threshold + minimum-evidence gate
4. How is the ancient-text library curated? → Editorial pipeline + citation chain + provenance
