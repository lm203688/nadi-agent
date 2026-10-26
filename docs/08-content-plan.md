# 08 · Content & Timeline Plan

The Championship runs from October 7, 2026 (registration) to the Grand Final in the first week of May 2027. This document is the plan for the Nadi submission across that window.

## The calendar

### Phase 1 — Registration (October 2026)

**Goal**: register, complete the introductory workshops, publish version 1 of the submission.

| Week | Official event | Nadi action |
|------|----------------|-------------|
| 10-07 | Registration opens | Register on `dubaichamberdigital.com`; confirm team roster |
| 10-14 | Workshop 1 (agentic AI fundamentals) | Attend, take notes, iterate on `docs/01-strategy.md` |
| 10-21 | Workshop 2 (agent architecture) | Attend, review architecture diagram |
| 10-28 | Workshop 3 (build & demo) | Attend, review demo video script |
| 11-04 | — | Submission v1 complete: prototype + deck + video v1 + compliance |

### Phase 2 — Digital Academy (November 2026)

**Goal**: complete all four advanced courses and four applied workshops. Take mentorship seriously.

- **Course 1**: Agent orchestration patterns
- **Course 2**: Safety and alignment in agentic systems
- **Course 3**: Product-market fit for AI products
- **Course 4**: Fundraising and commercialisation

- **Workshop 1**: Live demo rehearsal
- **Workshop 2**: Adversarial testing of your agent
- **Workshop 3**: Business model canvas for AI-native products
- **Workshop 4**: Pitch to a jury panel

At the end of November, we should have:

- v2 of the safety policy, hardened from adversarial workshop
- v2 of the pitch deck, revised after jury-panel workshop
- v2 of the demo video, with mentorship feedback
- Expanded knowledge library (15 → 40 entries)

### Phase 3 — Submission freeze (December 2026)

- **12-01**: Freeze code and documentation
- **12-05**: Run full test suite; fix any failures
- **12-10**: Register final submission on the portal
- **12-15**: Buffer for portal bugs and re-submissions

### Phase 4 — Build phase (January–April 2027)

Assuming shortlist:

- 01-2027: Receive shortlist feedback; open issue tracker for iteration
- 02-2027: Closed pilot with 5–10 users
- 03-2027: Pilot with 20–50 users; iterate on Guardian
- 04-2027: Polish, freeze, prepare for Grand Final

### Phase 5 — Grand Final (first week of May 2027)

- Live demo, on stage
- Live Q&A with jury
- Decision

## Content inventory

The complete set of assets to prepare:

| Asset | Location | Owner | Status |
|-------|----------|-------|--------|
| Strategy docs (9 files) | `docs/` | Solo founder | ✅ Ready |
| Eligibility statement | `compliance/eligibility-statement.md` | Solo founder | ✅ Ready |
| IP disclosure | `compliance/ip-disclosure.md` | Solo founder | ✅ Ready |
| Data governance | `compliance/data-governance.md` | Solo founder | ✅ Ready |
| Logo + palette + wordmark | `branding/` | Solo founder | ✅ Ready |
| Pitch deck (12 slides) | `pitch-deck/index.html` | Solo founder | ✅ Ready |
| Demo video script | `demo-video/script.md` | Solo founder | ✅ Ready |
| Demo video storyboard | `demo-video/storyboard.md` | Solo founder | ✅ Ready |
| Demo video subtitles | `demo-video/subtitles_en.srt` | Solo founder | ✅ Ready |
| Prototype (agent team) | `prototype/` | Solo founder | ✅ Ready |
| Frontend demo (3 pages) | `frontend/` | Solo founder | ✅ Ready |
| Demo video (rendered) | TBD | Solo founder | ⏳ To be produced |
| Mentorship notes | `docs/mentorship/` | Solo founder | ⏳ Nov 2026 |
| Adversarial test results | `prototype/tests/results/` | Solo founder | ⏳ Nov 2026 |

## Communication plan

- **Weekly**: internal progress note in `docs/notes/`
- **Bi-weekly**: version bump + commit
- **On-demand**: after each workshop, a short write-up in `docs/mentorship/`

## Risk buffer

- The December 12, 2026 deadline has a **7-day buffer** built in (freeze on 12-01)
- If Digital Academy mentorship points to a fundamental product change, we have the January–April Build phase to absorb it
- If the prototype is not shippable by December, we submit with a "prototype v0.9" tag and a clear roadmap to v1.0 in Q1 2027 — this is standard practice in agentic-AI competitions and judges understand
