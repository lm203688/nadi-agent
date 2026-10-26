# Nadi — A Team of AI Agents for Your Health

> **Entry for the Dubai Create AI Agents Championship (2026)**
> Track: **Best Personal AI Agent**

Every health app has a chatbot. Nadi has a **team**.

A Planner asks the right questions. An Executor pulls from your wearables and a curated ancient-text library. A Critic challenges every recommendation. A Guardian intercepts anything that could harm you. You watch all four work in real time — because your health is too important for a single voice.

---

## At a glance

| Item | Detail |
|------|--------|
| Product | Nadi — a multi-agent reasoning platform for personal health decisions |
| Tagline | *A team of AI agents that think out loud before they advise you on health.* |
| Track | Best Personal AI Agent |
| Eligibility | New AI-agent capability, prototype stage, not commercially released |
| Submission deadline | December 2026 |
| Grand Final | First week of May 2027 |

## Where to start

Read these in order:

1. [`docs/00-summary-report.md`](docs/00-summary-report.md) — one-page summary for judges (start here)
2. [`docs/01-strategy.md`](docs/01-strategy.md) — why this product, why this track, why now
3. [`docs/02-product.md`](docs/02-product.md) — the user journey and the four-agent ritual
4. [`docs/03-architecture.md`](docs/03-architecture.md) — how the team is built
5. [`docs/05-eligibility.md`](docs/05-eligibility.md) — how we fit the "new capability" rule
6. [`docs/06-pitch-deck-outline.md`](docs/06-pitch-deck-outline.md) — the 12-slide structure of [`pitch-deck/index.html`](pitch-deck/index.html)
7. [`docs/07-demo-script.md`](docs/07-demo-script.md) — the two-minute demo, frame by frame

## Layout

```
healthlens-agent-compete/
├── README.md                   ← you are here
├── docs/                       ← strategy, product, architecture, eligibility, plan
├── compliance/                 ← eligibility statement, IP disclosure, data governance
├── branding/                   ← logo, palette, wordmark
├── pitch-deck/                 ← the 12-slide HTML deck for judges
├── demo-video/                 ← script, storyboard, subtitles
├── prototype/                  ← runnable agent team (multi-agent loop)
├── frontend/                   ← three-page demo (home, agent-team, history)
└── scripts/                    ← helper utilities
```

## Try it live

Once deployed to GitHub Pages:

| Page | URL |
|------|-----|
| Frontend · Home | https://lm203688.github.io/nadi-agent/ |
| Frontend · Agent Team (interactive) | https://lm203688.github.io/nadi-agent/agent-team.html |
| Frontend · History (audit trail) | https://lm203688.github.io/nadi-agent/history.html |
| Pitch deck (12-slide, ←/→ to navigate) | https://lm203688.github.io/nadi-agent/pitch-deck/ |

## Run the prototype locally

Requires Python 3.10+ (standard library only, no dependencies).

```bash
cd prototype

# Run the safety benchmark — 30 adversarial prompts, all pass
python -m nadi_agent.benchmark

# See the five demonstration scenarios
python -m nadi_agent.demo

# Start the HTTP API for the frontend
python -m nadi_agent.server --port 8000
```

## Serve the frontend locally

```bash
cd frontend
python -m http.server 8080
# then open http://localhost:8080/
```

## Status

| Deliverable | Status |
|-------------|--------|
| Strategy docs (docs/01–09) | ✅ Ready |
| Compliance docs | ✅ Ready |
| Brand assets | ✅ Ready |
| Pitch deck (HTML) | ✅ Ready |
| Demo video script + subtitles | ✅ Ready |
| Agent team prototype | ✅ Runnable · 30/30 benchmark |
| Frontend demo | ✅ Three pages |

## Prototype note

The Guardian in this repository is a **rule-based engine** for demonstration purposes. It is intentionally small, inspectable, and audit-friendly so judges can read the code and reproduce every safety decision. A production build would swap this for a classifier-based guardrail with clinical review, but the current prototype is sufficient to show that Guardian is *code, not a prompt* — and therefore cannot be bypassed by user phrasing.

## Legal

Nadi is submitted as a **new AI-agent capability** developed for this championship. It is not a commercialised product and no revenue has been generated from it. See [`compliance/`](compliance/) for full eligibility and IP disclosure.
