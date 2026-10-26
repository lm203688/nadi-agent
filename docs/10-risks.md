# 09 · Risk Register

## R1 · Eligibility — HealthLens overlap is read as "already commercialised"

**Severity**: Critical
**Likelihood**: Medium
**Mitigation**:
- Explicit eligibility statement (`compliance/eligibility-statement.md`)
- Fresh brand, no HealthLens URLs, no screenshots, no user data
- Scope Nadi smaller than HealthLens (single question, not a platform)
- If challenged, the answer is: "Nadi is one capability derived from an open-source MIT project. That is not a commercialised product."

**Early warning signal**: reviewer asks "is this the same product as HealthLens?" at submission review

## R2 · Four-agent team is perceived as theatre, not substance

**Severity**: High
**Likelihood**: Medium
**Mitigation**:
- Every agent has a distinct, testable behaviour
- Guardian is a real safety gate, tested against 30 adversarial prompts
- Critic is required to produce at least one genuine objection per turn (not a rubber stamp)
- Demo shows Critic rejecting Executor's first proposal and forcing a retry

**Early warning signal**: judges ask "why does Critic not just skip to consensus?"

## R3 · Safety posture is challenged (medical AI risk)

**Severity**: High
**Likelihood**: Medium
**Mitigation**:
- Guardian is prominent, not hidden
- No diagnostic language, no prescription advice, ever
- Every output is framed as "consider discussing with a clinician"
- Data governance document is included in the submission
- Confidence is displayed with every response

**Early warning signal**: a jury member asks "what if someone relies on this for a real diagnosis?"

## R4 · Multi-modal complexity (image upload, wearable sync) creates demo failures

**Severity**: Medium
**Likelihood**: Medium
**Mitigation**:
- Demo is text-first; multi-modal is shown but not required
- Wearable data is imported as a JSON file, not a live API call
- All three personas have pre-seeded data files

**Early warning signal**: the demo takes more than 30 seconds to load user data

## R5 · Ancient-text library is judged as culturally shallow or unverified

**Severity**: Medium
**Likelihood**: Medium–High
**Mitigation**:
- Every entry is public domain (Shen Nong Ben Cao Jing, Shiliao Bencao)
- Every entry carries provenance (chapter, edition, translation source)
- Critic explicitly flags where traditional advice conflicts with modern evidence
- Guardian blocks diagnostic claims sourced from ancient texts

**Early warning signal**: "how do you verify these classical texts?"

## R6 · Arabic localisation is not required but could help

**Severity**: Low
**Likelihood**: Not applicable as a risk
**Mitigation**:
- v1: English only, no Arabic — judges are bilingual and the pitch is not Arabic-only
- v2 (Build phase, if shortlisted): add Arabic + RTL to Home and Agent Team pages
- The pitch deck contains one Arabic quote (the tagline in Arabic script) as a courtesy

**Early warning signal**: judges ask "will this ship in Arabic?"

## R7 · Technical failure on Grand Final day

**Severity**: Critical
**Likelihood**: Low
**Mitigation**:
- The demo is designed to work fully offline; no cloud dependency
- A 60-second pre-recorded fallback video is prepared
- Two devices carry the same setup (primary laptop + backup laptop)
- Dry-run the demo at least 5 times in the two weeks before Grand Final

**Early warning signal**: prototype requires more than 15 seconds to boot

## R8 · Timing slips; submission misses the December deadline

**Severity**: Critical
**Likelihood**: Low
**Mitigation**:
- Freeze on 2026-12-01, buffer of 7 days before the December close
- Weekly content-plan checkpoints
- If any phase slips, cut scope (do not cut compliance or demo quality)

**Early warning signal**: two consecutive weeks without a new commit

## R9 · Solo-founder bottleneck

**Severity**: High
**Likelihood**: Medium
**Mitigation**:
- Team size for the Championship allows up to 6 members
- Invite 1–2 domain experts during Phase 2 (a clinical reviewer for safety policy, a design reviewer for UX)
- Do not hire; do not add complexity; ask for volunteer mentorship

**Early warning signal**: two deliverables delayed simultaneously

## R10 · Judges favour already-shipped consumer health products over prototypes

**Severity**: Medium
**Likelihood**: Low–Medium
**Mitigation**:
- The Championship explicitly favours new capability over established products
- Position Nadi as the *only* entry with visible multi-agent reasoning
- Every competing consumer health AI that is fully shipped is disqualifyingly "already commercialised"

**Early warning signal**: N/A — this risk is structural and unaddressable except through the pitch

## The one risk that could kill the submission

If the judges read "Nadi" as a rebrand of HealthLens, the eligibility is lost. The mitigation is documentation-heavy: eligibility statement, IP disclosure, fresh branding, no HealthLens references in the demo. Everything in this repository is designed to make the case that Nadi is new.

## The one risk that could cost us the win (not the submission)

If the four-agent structure is not demonstrated as *real* reasoning rather than theatre, we lose on substance. The Critic rejection + Executor retry in the demo is the pivot moment. If we cut that from the demo video, the pitch collapses to a chatbot.
