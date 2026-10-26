# Data Governance — Nadi

## Summary

Nadi is designed to be a **privacy-preserving personal-health companion**. The prototype stage is deliberate in what it stores, what it computes, and what it never does.

## What Nadi collects

**In the prototype (this submission)**: nothing. Every persona in `prototype/demo_users/` is fictional and locally seeded. No user data crosses a network boundary. No logs leave the machine.

**In a future production deployment (post-championship, if any)**: only data the user explicitly opts in to share:

- Free-text check-ins (session-scoped, deletable)
- Structured health data the user pastes or imports (e.g. a lab result, a wearable export)
- Preference data (dietary, cultural, communication style)

## What Nadi does not collect

- Any biometric identifier (face, voice, fingerprints) — the multi-modal tongue / image feature, when developed, is on-device only
- Any payment data
- Any geolocation (beyond city-level opt-in for climate-related health advice)
- Any account data (no password, no email — the prototype has no auth)

## Storage model

- **Prototype**: local JSON files only. Session state in memory.
- **Future production (Build phase, if selected)**: user-owned storage model. Every byte of a user's data is owned by that user and can be deleted at any time.

## Retention

- **Prototype**: session-scoped; cleared on reload
- **Future production**: rolling 30-day window for conversational context; 90-day rolling window for trend analysis; indefinite for user-declared preferences. All subject to user override.

## Data never leaves

- **No training on PHI.** User data is never used to train or fine-tune any model without explicit, informed, revocable consent per model and per data category.
- **No cross-user inference.** One user's data is never used to inform another user's recommendations.

## Regional handling

Nadi does not make claims about regional data residency in the prototype stage. In the Build phase, if the product is expanded for the Middle East market, Nadi will target UAE PDPL compliance.

## User rights

Every user, in a future production deployment, will have:

- Right to view all data Nadi holds about them
- Right to export all data Nadi holds about them (JSON format)
- Right to delete all data Nadi holds about them
- Right to opt out of any data category individually
- Right to request a copy of their data's use history

## Safety policy

The Guardian agent is a **runtime supervisor** that applies a declarative policy file (`prototype/nadi_agent/policy.yaml`). The policy file is included in this repository and is version-controlled. Any change to the policy file is documented in the change log.

## Consent flow (future production)

Before any data is collected, a future production Nadi will present:

1. A plain-language explanation of what data is being collected and why
2. An itemised list of what will and will not happen to that data
3. A clear accept/decline for each category
4. A visible "delete my data" button, always, not buried in settings

## Data breach protocol

The prototype has no network surface and no stored credentials, so a breach is not applicable at this stage. In a future production deployment, the protocol will include:

- 24-hour notification to affected users
- 72-hour notification to UAE Data Office (PDPL) if applicable
- Public post-mortem within 14 days
