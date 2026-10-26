# IP Disclosure — Nadi

## What Nadi is

Nadi is a Championship-specific submission with:

- **New name, mark, palette, tagline**
- **New codebase** (in this repository)
- **New pitch deck, demo video, frontend, compliance docs**
- **New safety policy** (`prototype/nadi_agent/policy.yaml`)
- **New knowledge library** (curated subset, not the full HealthLens corpus)

## What Nadi reuses

Nadi reuses the following from the open-source MIT project **HealthLens**:

| Component | HealthLens path | Nadi path | Purpose |
|-----------|-----------------|-----------|---------|
| Multi-role agent skeleton | `healthlens_agent/team.py` | `prototype/nadi_agent/team.py` | Planner/Executor/Critic/Referee → Planner/Executor/Critic/Guardian |
| Safety gate concept | `healthlens_agent/safety.py` | `prototype/nadi_agent/guardian.py` | Declarative red-line policy |
| Runtime audit | `healthlens_agent/audit.py` | `prototype/nadi_agent/audit.py` | Deliberation transcript |
| Fusion engine (trimmed) | `app/lib/fusion_engine.py` | `prototype/nadi_agent/fusion.py` | 8-axis wellbeing scoring (subset) |
| Evidence grading | `skills/evidence_grading/` | `prototype/nadi_agent/citations.py` | L1/L2/L3 grading → confidence |

All reused components are architecturally general-purpose and are not tied to any HealthLens-specific brand, product surface, deployment, or commercial context.

HealthLens is MIT-licensed. Reuse is legally clean.

## What Nadi does not reuse

- HealthLens's brand, logo, tagline, deployed site, or user base
- HealthLens's payment, subscription, or referral integrations
- HealthLens's 701-title Chinese classical bibliography (a curated subset of 8 is used in Nadi)
- HealthLens's backend CRUD, RBAC, admin console, database migrations
- HealthLens's regional claims policy engine, GDPR engine, FHIR exporter
- HealthLens's CI/CD pipeline, Docker image, cloud deployment

## Licensing of Nadi itself

**All code, documentation, and non-logo assets in this repository are MIT-licensed** (matching HealthLens's licence for consistency).

**The "Nadi" wordmark and logo are trademarks reserved by the submitting team for the purpose of this championship.** If the championship requires open-sourcing the brand, the team will evaluate the request and comply within the framework of the championship rules.

## Third-party material

| Material | Source | Licence | Notes |
|----------|--------|---------|-------|
| Classical Chinese texts | Shen Nong Ben Cao Jing (c. 1–2nd century CE) | Public domain | Provenance chain in `prototype/data/ancient_texts/` |
| Classical Chinese texts | Shiliao Bencao (c. 8th century CE) | Public domain | Provenance chain in `prototype/data/ancient_texts/` |
| Fonts (Inter, Fraunces) | Google Fonts | SIL Open Font Licence | Free to use |
| Icons | Lucide | ISC | Free to use |

## Model usage

The prototype currently runs a **local rule-based fallback** for the demonstration (no live LLM calls). This is deliberate: it makes the demo reproducible, offline-capable, and judge-verifyable. In the Build phase, if shortlisted, we will add live model calls with a documented model card.

## Disclosure summary

- Reuse: MIT-licensed HealthLens architectural patterns only
- New: everything else
- Third-party: public-domain texts, SIL/ISC-licensed fonts and icons
- Model: local fallback in prototype; live model deferred to Build phase
