# Final Submission Checklist — Nadi for Dubai Create AI Agents Championship 2026

> Last updated: 2026-10-26.
> Deadline: **Registration** 2027-01 · **Submission** 2027-01 · **Grand Final** 2027-05 (Week 1, Dubai).
> Category: **Best Personal AI Agent** (New AI Agent ability track).

---

## 1. What must be in the final submission

Per the official entry rules:

| # | Deliverable | Required | Status | Where |
|---|---|---|---|---|
| 1 | AI Agent prototype (runnable) | ✅ Yes | ✅ Ready | [`prototype/`](../prototype/README.md) |
| 2 | Pitch deck (12 slides) | ✅ Yes | ✅ Ready | [`pitch-deck/`](../pitch-deck/) — also live on GitHub Pages |
| 3 | Demo video (1–3 min) | ✅ Yes | 🟡 Script + storyboard + SRT ready — **video not rendered** | [`demo-video/`](../demo-video/) |
| 4 | Summary report | ✅ Yes | ✅ Ready | [`docs/00-summary-report.md`](00-summary-report.md) |
| 5 | Registration form filled in | ✅ Yes | 🟡 Pending — 15-min task, 4 fields you must provide yourself | [`docs/09-registration-form-prefill.md`](09-registration-form-prefill.md) |
| 6 | Team member list (≤6 people, or 1 solo) | ✅ Yes | 🟡 Pending — filled on the registration form | See section 2 |
| 7 | Category: **Best Personal AI Agent** | ✅ Yes | 🟡 Pending — filled on the registration form | See section 2 |
| 8 | Eligibility confirmation (Youth <21, Winner must be Dubai-licensed, Finalists need Security Clearance) | ✅ Yes | 🟡 Pending — user must confirm | See section 5 |

---

## 2. Registration — must be done by the account owner

**URL:** <https://www.dubaichamberdigital.com/en/create-ai-agents-register-your-interest>

Fields that must be filled by the human registrant:

- Full name (legal name, as shown on passport / ID)
- Email address (must be able to receive emails)
- Phone number (with country code)
- Country of residence
- Category selection → **Best Personal AI Agent**
- Team composition → Solo (or list team members with same info)
- Consent checkbox for terms, data processing, and Security Clearance (if you may be shortlisted as a Finalist, travel to Dubai is required)

> **Why this must be done by you**: it is your legal identity and personal consent. No one else can check the consent box on your behalf.

---

## 3. Prototype — already ready

- **Repo**: <https://github.com/lm203688/nadi-agent>
- **GitHub Pages preview**: <https://lm203688.github.io/nadi-agent/>
- **Pitch deck (live)**: <https://lm203688.github.io/nadi-agent/pitch-deck/>
- **Summary report**: [`docs/00-summary-report.md`](00-summary-report.md)

Judges can run the prototype in 6 commands:

```bash
git clone https://github.com/lm203688/nadi-agent.git
cd nadi-agent
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r prototype/requirements.txt
python -m prototype.test
cd frontend && python -m http.server 8000
```

Browser: <http://localhost:8000/> — pick a symptom, chat, see the 4-agent plan.

---

## 4. Demo video — the one missing piece

The video is the biggest differentiator between a "submission" and a "shortlist entry."

**What we already have:**
- 90-second narration script in English: [`demo-video/script.md`](../demo-video/script.md)
- 20-scene storyboard with shot descriptions: [`demo-video/storyboard.md`](../demo-video/storyboard.md)
- SRT subtitles file: [`demo-video/subtitles_en.srt`](../demo-video/subtitles_en.srt)
- Render harness: [`demo-video/render.ps1`](../demo-video/render.ps1)

**How to finish it (30–60 min of your time):**

> Either option produces `final.mp4` in this folder. Both use the render script [`demo-video/render.ps1`](../demo-video/render.ps1). The Windows Store `ffmpeg.exe` alias will not work — install a real build first with `winget install --id Gyan.FFmpeg` and re-open your terminal.

**Option A — Slideshow from storyboard (recommended, 15 min):**
1. Follow [`demo-video/storyboard.md`](../demo-video/storyboard.md) and produce one 1920×1080 PNG per scene — either by taking clean screenshots of the prototype running the corresponding step, or by exporting the pitch deck slides.
2. Save them into `demo-video/scenes/` as `scene_01.png` … `scene_20.png`.
3. Open PowerShell inside `demo-video/`, then run:
   - `.\\render.ps1 -SlidesOnly`  → silent slideshow with burned-in English subtitles, or
   - `.\\render.ps1 -Audio narration.m4a`  → with a voice-over you recorded (or synthesized from [`script.md`](../demo-video/script.md)).

**Option B — Record your screen (30 min):**
1. Open the prototype at <http://localhost:8000/>.
2. In Windows, press `Win + G` → Start recording → **choose screen area only, do NOT record the microphone**.
3. Follow [`demo-video/storyboard.md`](../demo-video/storyboard.md) scene-by-scene. Narration timing must match the SRT.
4. Stop recording → drop the file in `demo-video/` (any name).
5. Run `.\render.ps1 -Audio narration.m4a` (or `-SlidesOnly`) to overlay subtitles, fade-out, and produce `final.mp4`.

**Option C — Skip video entirely:**
Judges accept projects without a video, but you will be scored against teams that have one. Not recommended.

---

## 5. Eligibility — confirm with the registrant

- **Youth category (<21)**: does the registrant qualify? If yes, select Youth category and the submission will be scored against a lower bar. If no, use the general Best Personal AI Agent track.
- **Finalist attendance**: to enter the Grand Final in Dubai (Week 1, May 2027), you will need (a) a UAE-issued **Security Clearance** and (b) travel budget. If you cannot travel, you can still be scored and awarded, but not present in person.
- **Winner residency**: to claim the full USD 150,000 award, the winning team must hold a **Dubai-based trade license**. If you are not currently Dubai-licensed, you can still win on the boards — the cash prize is subject to that licensing condition.

---

## 6. Timeline — what happens next

| Date | Event |
|---|---|
| **Now – 2027-01** | Registration window. Fill the form. |
| **2027-01** | Submission window. Upload prototype URL + pitch deck + demo video + summary report. |
| **2027-Q1 (approx.)** | Selection committee scores all submissions. |
| **2027-04** | Shortlist announced. Finalists invited to Dubai. |
| **2027-05 Week 1** | Grand Final in Dubai — in-person pitch to jury and public. |
| **Grand Final Day** | Four awards announced (150k USD each) + AI Agent of the Year. |

---

## 7. What we still need from the registrant

1. Fill the registration form at <https://www.dubaichamberdigital.com/en/create-ai-agents-register-your-interest>
2. Confirm category: **Best Personal AI Agent**
3. Confirm team size: **solo** (1) or list up to 6 members
4. Revoke the leaked GitHub tokens listed in the security notice (not required for the competition, but a personal-security must-do)
5. Record the demo video per [`demo-video/storyboard.md`](../demo-video/storyboard.md)

---

## 8. If anything breaks before submission

- **GitHub Pages went down**: push an empty commit to `main` to re-trigger the workflow at <https://github.com/lm203688/nadi-agent/actions>
- **Prototype no longer runs on Python 3.12**: check `prototype/requirements.txt` — it is pinned.
- **Pitch deck looks wrong on a judge's screen**: it is responsive down to 360px wide. If it does not fit, the browser is too old.
- **Demo video too long**: trim with `ffmpeg -i in.mp4 -t 180 -c copy out.mp4`.
