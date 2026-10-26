# 04 · What we reuse from HealthLens (and what we don't)

Nadi is a **new AI-agent capability** developed for the Championship. It is not HealthLens renamed. To keep eligibility clean and the pitch honest, this document makes the reuse boundary explicit.

## The rule

**Reuse is allowed if** it is (a) MIT-licensed, (b) a general-purpose building block, and (c) not tied to a HealthLens-specific business, product surface, or commercial deployment.

**Reuse is not allowed** if it would carry HealthLens's brand, its commercial posture, its production deployment, or its user-base identity into this submission.

## The reuse list

### ✅ Agent architecture (core — this *is* Nadi's differentiator)

| From HealthLens | To Nadi | Rationale |
|-----------------|---------|-----------|
| `healthlens_agent/team.py` | `prototype/nadi_agent/team.py` | Planner / Executor / Critic / Guardian skeleton — this is the entire product |
| `healthlens_agent/safety.py` | `prototype/nadi_agent/guardian.py` | Declarative safety gate — re-implemented with Nadi's own policy file |
| `healthlens_agent/audit.py` | `prototype/nadi_agent/audit.py` | Runtime audit — the "transcript" the demo shows |
| `healthlens_agent/pipeline.py` | `prototype/nadi_agent/orchestrator.py` | The sequential-then-branching loop |
| `healthlens_agent/benchmark.py` | `prototype/nadi_agent/benchmark.py` | The 30-prompt safety test harness |

These are the *conceptual* pieces of HealthLens that turned out to be the strongest ideas. They are what Nadi is built on.

### ✅ Knowledge & citation plumbing

| From HealthLens | To Nadi | Rationale |
|-----------------|---------|-----------|
| `skills/evidence_grading/` | `prototype/nadi_agent/citations.py` | L1/L2/L3 evidence grading → Nadi's confidence layer |
| `data/publishable/tcm_structured/` (2 files) | `prototype/data/ancient_texts/` | Two curated entries (Food Therapy, Shen Nong Ben Cao Jing) — cited, provenance-linked |
| `app/core/axis_scorers.py` (subset) | `prototype/nadi_agent/fusion.py` | 8-axis wellbeing scoring, trimmed |

### ✅ Test methodology

| From HealthLens | To Nadi |
|-----------------|---------|
| `healthlens_agent/tests/test_safety.py` | `prototype/tests/test_guardian.py` — same adversarial prompt style |
| `healthlens_agent/tests/test_benchmark.py` | `prototype/tests/test_benchmark.py` — same scoring logic |

## The exclusion list

### ❌ Brand & identity

- HealthLens name, logo, tagline — not reused
- healthlens.cc domain, deployments, CI/CD assets — not reused
- Chinese marketing materials, SEO assets, GEO content — not reused

### ❌ Commercial surfaces

- Payment integrations (Creem, 虎皮椒) — not reused
- Subscription / freemium / referral models — not reused
- Marketing copy, landing pages, share links — not reused

### ❌ Scale artefacts

- 701-title Chinese classical bibliography — not reused (too large, dilutes story)
- 174-test backend test suite — not reused wholesale (only agent-related)
- Alembic migrations, RDS schemas, Docker Compose, Prometheus config — not reused
- RBAC, JWT, admin console — not reused (the demo has no auth)

### ❌ Clinical claim apparatus

- Regional claims policy (`claims_policy/*.yaml`) — not reused
- GDPR / data residency engine — *conceptually* referenced, but not the same code
- FHIR exporter — not reused

## What this means for the pitch

Two things to say, honestly:

1. **"The four-agent architecture is inspired by work we did on HealthLens, our open-source MIT project. Nadi is the Championship-facing form of that idea, scoped to personal health."**
2. **"Everything about Nadi — its name, its brand, its demo, its knowledge library, its policy file — is new. The reuse is architectural only."**

The first sentence is transparent. The second sentence makes clear that Nadi is not a re-skinned HealthLens submission.

## Intellectual property handling

- HealthLens is MIT. Code reuse is legally clean.
- Nadi's own code is MIT-licensed and committed alongside this repo.
- The ancient-text entries used are public-domain Chinese classical works (Shen Nong Ben Cao Jing c. 1–2nd century CE; Shiliao Bencao c. 8th century CE). No copyright claim.
- Structured extractions carry provenance metadata (source text, chapter, edition).

See [`../compliance/ip-disclosure.md`](../compliance/ip-disclosure.md) for the formal disclosure.
