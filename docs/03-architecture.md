# 03 · Architecture

## The layer model

```
┌──────────────────────────────────────────────────────────┐
│                Frontend (three pages)                     │
│   home · agent-team (deliberation view) · history        │
└──────────────────┬───────────────────────────────────────┘
                   │  REST / SSE
┌──────────────────▼───────────────────────────────────────┐
│                Team Orchestrator                          │
│   Planner → Executor → Critic → Guardian → Consensus     │
│   Policy file · Citation resolver · Confidence gate      │
└──────────────────┬───────────────────────────────────────┘
                   │
    ┌──────────────┼───────────────┬───────────────────────┐
    │              │               │                       │
┌───▼───┐     ┌───▼───┐      ┌────▼────┐         ┌────────▼────────┐
│ User  │     │ Knowledge │    │ Wearable│         │ Safety policy   │
│ State │     │ Layer    │    │ Layer   │         │ Registry        │
└───────┘     └─────────┘    └─────────┘         └─────────────────┘
```

## The four agents

Each agent is a self-contained module with a typed input, typed output, and a bounded compute budget.

### Planner

**Purpose**: frame the user's intent, ask only what is needed, decide which other agents to route to.

- Input: user message + session context
- Output: plan JSON (`intent`, `clarifying_questions`, `route_to`, `evidence_needs`)
- Constraint: at most 2 clarifying questions per turn; no medical advice

### Executor

**Purpose**: gather evidence from structured sources and produce a candidate answer with citations.

- Sources (priority order):
  1. User state (previous responses, preferences, opt-in data)
  2. Wearable stream (HRV, resting HR, sleep, steps — pluggable adapter)
  3. Curated knowledge library (structured articles + ancient-text entries)
- Output: proposal JSON (`claim`, `evidence_ids`, `confidence`, `unknowns`)
- Constraint: every claim carries ≥1 evidence ID; ungrounded claims are rejected

### Critic

**Purpose**: find the weakest link in Executor's proposal. This is the anti-hallucination layer.

- Input: Executor's proposal + original user message
- Output: critique JSON (`objections`, `missing_evidence`, `alternatives`, `verdict`)
- Constraint: at least one genuine objection is produced per turn (a `no_objections` response is not allowed — Critic must actively search)

### Guardian

**Purpose**: hard safety boundary. Blocks proposals that cross a clinical red line.

- Policy: `safety/policy.yaml` — declarative rules
- Categories:
  - Acute symptoms (chest pain, acute stroke signs, suicidal ideation, etc.)
  - Medication changes (never recommend starting/stopping any prescription)
  - Diagnostic language (never use `you have`, `you don't have`; always `consider discussing`)
  - High-risk populations (pregnancy, pediatrics, elderly without confirmation)
  - Data leakage (never store PHI outside the user's local session without explicit consent)
- Output: gate JSON (`action` ∈ {pass, override, block, defer_to_clinician}, `reason`)
- Constraint: Guardian can only escalate (pass → override → block), never relax

## The Orchestrator

Runs the four agents in sequence. Manages session state. Produces the consensus response.

```
user_msg
  │
  ▼
[Planner] → plan
  │
  ▼
[Executor] → proposal  (with evidence_ids)
  │
  ▼
[Critic] → critique
  │
  ├─ critique.verdict == "reject" → Executor retries with critique feedback (max 1 retry)
  │
  ▼
[Guardian] → gate
  │
  ├─ gate.action == "block" → response framed as red-line catch, no advice
  ├─ gate.action == "defer_to_clinician" → response framed as "please see a clinician"
  └─ gate.action == "pass" → consensus response with confidence + evidence
```

## Confidence gate

Consensus is only produced if all three are true:

1. Critic did not reject after 1 retry
2. Guardian gate is `pass`
3. Aggregate evidence count ≥ 2 and confidence ≥ 0.55

Otherwise the response is explicitly "insufficient evidence" — not a hedged guess.

## Reuse from HealthLens

Nadi reuses the following from the parent project (HealthLens, open-source MIT), repackaged under the Nadi brand:

| Reused component | Source (HealthLens) | Nadi form |
|------------------|---------------------|-----------|
| Multi-role agent skeleton | `healthlens_agent/team.py` | `prototype/nadi_agent/team.py` — Planner/Executor/Critic/Referee renamed Guardian |
| Safety policy gate | `healthlens_agent/safety.py` | `prototype/nadi_agent/guardian.py` — declarative YAML-driven |
| Runtime audit | `healthlens_agent/audit.py` | `prototype/nadi_agent/audit.py` |
| Fusion engine (adapted) | `app/lib/fusion_engine.py` | `prototype/nadi_agent/fusion.py` — trimmed to health-decision only |
| Citation chain concept | `skills/evidence_grading/` | `prototype/nadi_agent/citations.py` |

**Not reused** (deliberately):

- Payment, subscription, multi-locale UI
- 701-title Chinese classical bibliography (too large, story doesn't need it)
- Existing deployed healthlens.cc site
- RBAC, admin console, backend CRUD

## Storage

For the demo, storage is minimal and local-first:

- **Session state**: in-memory, reset on reload
- **User demo profiles**: JSON files under `prototype/demo_users/` (3 personas)
- **Knowledge library**: 15 curated entries in `prototype/data/knowledge/` (JSON, sourced)
- **Ancient-text entries**: 8 curated entries in `prototype/data/ancient_texts/` (JSON, citation-linked)

## Observability

Every deliberation writes an audit log entry with:

- `session_id`, `turn_id`, `timestamp`
- Planner plan
- Executor proposal + evidence IDs
- Critic critique
- Guardian gate
- Final consensus (or insufficient-evidence)

This is what shows up in the Demo video as "the transcript of the meeting".

## Deployment for the demo

For the Championship submission, the demo runs on the author's machine or a small cloud VM. Nothing is claimed about production scalability at this stage. The submission prototype is deliberately a single-process Python service + static HTML frontend.

```
python -m prototype.nadi_agent.server --port 8000
cd frontend && npm run dev
```

The frontend talks to the API over SSE to stream each agent's output as it becomes available.

## What we will do in the Build phase (Nov–Jan)

To reach Grand Final quality by May 2027:

1. Formalise the safety policy into a versioned, testable spec
2. Grow the knowledge library from 15 → 60 curated entries with full provenance
3. Grow the ancient-text library from 8 → 20 curated entries
4. Add wearable adapters (Apple Health via shareable file, Huawei Health via manual import)
5. Add multi-session memory (7-day rolling + 30-day summary)
6. Add a small benchmark harness: 30 clinical-edge-case prompts, tracked Guardian catch rate
7. Add Arabic + English i18n at the UX layer
