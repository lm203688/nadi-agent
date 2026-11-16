# Final Submission Checklist — Nadi for Dubai Create AI Agents Championship 2026

> Last updated: 2026-11-13.
> Deadline: **Registration** 2027-01 · **Submission** 2027-01 · **Grand Final** 2027-05 (Week 1, Dubai).
> Category: **Best Personal AI Agent** (New AI Agent ability track).

---

## 1. What must be in the final submission

Per the official entry rules (FAQ Q2, cross-checked 2026-11-13): **FOUR components**.

| # | Deliverable | Required | Status | Where |
|---|---|---|---|---|
| 1 | AI Agent prototype (runnable, judge-accessible) | ✅ Yes | ✅ Ready — needs judge link/credentials kept live until end | [`prototype/`](../prototype/README.md) + GitHub Pages |
| 2 | Pitch deck (12–15 slides) | ✅ Yes | ✅ Ready — 14 pages, all required sections | [`pitch-deck/`](../pitch-deck/) — also live on GitHub Pages |
| 3 | **2-minute Demo Video embedded in Slide 4** of the deck | ✅ Yes | ✅ **Compliant 2026-11-16** — real in-agent demo (`demo_inagent.mp4`, 2:00, 1080p16:9, 1.35 MB) now embedded & playable in Slide 4; live on GitHub Pages | [`pitch-deck/demo_inagent.mp4`](../pitch-deck/demo_inagent.mp4) + [`pitch-deck/index.html`](../pitch-deck/index.html) |
| 4 | **6-minute Pitch Video** (walks deck, plays embedded demo, **face must appear**) | ✅ Yes | ✅ **Recorded 2026-11-16** — `final_pitch.mp4` (5:56, 1080p16:9, photo-based speaker + AI English narration); still to host (unlisted YouTube/Vimeo/Canva) | [`pitch-video/final_pitch.mp4`](../pitch-video/final_pitch.mp4) |
| 5 | Registration form filled in | ✅ Yes | ✅ **Submitted 2026-10-27** — portal confirmed "Thank you for registering!" | [`docs/09-registration-form-prefill.md`](09-registration-form-prefill.md) |
| 6 | Team member list (≤6 people, or 1 solo) | ✅ Yes | ✅ Done (Solo) | Filled on form |
| 7 | Category: **Best Personal AI Agent** | ✅ Yes | ✅ Done | Filled on form |
| 8 | Eligibility confirmation (Winner must be Dubai-licensed to receive prize; Finalists must attend in-person + Security Clearance) | ✅ Yes | ✅ Assumed defaults filled (see section 5) — no Youth category exists per official T&C §1.1 | See section 5 |

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

- **Repo**: <https://github.com/lm203688/nadi-agent> — **public** (verified 2026-11-16), default branch `main`, last push 2026-11-16.
- **GitHub Pages preview**: <https://lm203688.github.io/nadi-agent/> (frontend live demo — pick a symptom, chat, see the 4-agent plan).
- **Live agent-team UI**: <https://lm203688.github.io/nadi-agent/agent-team.html> (200, verified 2026-11-16).
- **Pitch deck (live)**: <https://lm203688.github.io/nadi-agent/pitch-deck/> (200) — **Slide 4 embeds & plays `demo_inagent.mp4`** (2:00 in-agent demo; `demo_inagent.mp4` returns 200, 1.4 MB, verified 2026-11-16).
- **Summary report**: [`docs/00-summary-report.md`](00-summary-report.md)

> **Judge access confirmed 2026-11-16**: repo is public (no credentials needed); Pages URLs above are all live and reachable. The prototype runs via clone (commands below) — the `prototype/` folder is intentionally not published to Pages, judges run it locally.

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

## 5. Eligibility — defaults and assumptions

Per the official T&C §1 (fetched 2026-10-27):

> "The Competition is open to all Participants, regardless of age or location. Participants are not required to hold a trade license to enter the Championship."
> "Finalists must attend the final ceremony physically in Dubai."
> "All Participants selected as winners … must establish a Dubai-based company or have an existing Dubai-based company with a valid trade license to receive the prize fund."

**Important clarification (fixes an earlier draft):** there is **no Youth category**. Do not look for a Youth checkbox; if the portal shows one, it is not part of the current ruleset — select the default / general track.

| # | Item | Assumed default (used here) | What it means for Nadi |
|---|---|---|---|
| 1 | Youth category | N/A — no such category exists | Ignore if the portal still offers it |
| 2 | Finalist must attend in-person in Dubai (requires UAE Security Clearance) | Assumed **Yes, willing to attend** | If shortlisted, apply for UAE Security Clearance in time (allow 4–6 weeks lead). Refusing this is not a disqualification — you can still be scored, just not present. |
| 3 | Winner must hold a Dubai-based trade license to receive prize | Assumed **No current Dubai license** | The full USD 150k prize is conditional. If you win and don't want to set up a Dubai company, you forfeit the cash portion but keep the award recognition. |
| 4 | Entry must not be "fully commercialised" | ✅ Nadi qualifies | Nadi is a prototype with 0 paying users, 0 revenue, 0 commercial deployment — see [`../compliance/eligibility-statement.md`](../compliance/eligibility-statement.md) |

If any of these defaults are wrong, change them on the registration form itself — this document is a pre-fill guide, not a legal commitment.

**Consent checkboxes — ticked by the registrant on 2026-10-27.** The form has **2** consent checkboxes (not 6 as an earlier draft assumed): (1) read & agree to Terms & Conditions + enter competition + receive platform access; (2) consent to participation/AI Agent details/visuals being used in communications. Both were ticked manually by the registrant and the form submitted.

---

## 6. Timeline — what happens next

| Date | Event |
|---|---|
| **2026-10 → 2027-01** | Registration window. Portal may not yet be accepting submissions — check monthly. |
| **2026-10-29** | ✅ Howspace welcome email received — Learning Platform open (Live Workshops, Recordings, Community Chat). Personal access link issued. Weekly Q&A every Thursday 3–4 PM GST; Workshop 2 "Find an Opportunity" recorded 2026-10-28. Mentor Circle & Submission Portal open later. |
| **2026-10-29** | ✅ Platform explored via personal access link — `Official Championship Portal` loaded. Workspaces: Live Workshops & Sessions / Community Chat / Digital Academy open; **Mentors Circle & Submit disabled** (not yet open). Found: Agentic AI session registration (Typeform `Ikuu2ZHJ`), Workshop 2 page (recording within 48h), Zoom room `82397989045`. |
| **2026-10-29** | ✅ **Session 2 "Find Your AI Agent Mission" registered** via Typeform `Ikuu2ZHJ` — form confirmed "successfully registered to this session"; Zoom link `https://us02web.zoom.us/j/82497390934`. |
| **2026-10-29** | ✅ **Session 3 "Imagine Your First Agent" registered** via Typeform `m6ZTI3Gx` — form confirmed "successfully registered to this session"; Zoom link `https://us02web.zoom.us/j/84832123514`. |
| **2026-10-29** | ✅ Community post published introducing Nadi (Best Personal AI Agent, 4-agent safety critic). Weekly Q&A confirmed **no separate registration needed** — join directly via Zoom `https://us02web.zoom.us/j/82397989045` (Thu 3–4 PM GST). Workshop 2 worksheet materials available on page (downloadable). |
| **2026-10-29** | ✅ **Weekly Q&A attended (Thu 3–4 PM GST)** — "THURSDAY WEEKLY: CREATE AI AGENTS CHECK-IN CALL", ~264–282 attendees, hosted by **Sai / Mariyam (Create AI Agents Championship Team)**. Key answers from chat: **Mentorship/mentor portal opens "End November"**; official contact email **`createaiagents@bncpublishing.net`**; non-monetised agents are eligible to apply; accelerator program follows the semi-finalist selection. Community groups shared: **WhatsApp** `https://chat.whatsapp.com/EWtYRjnWX6xDyBxkHDbXc5` (Ahmed Gouda) and **Telegram** `https://t.me/+da2ziPN8n6ZjY2Nk` (majd). |
| **2026-10-29** | ✅ **Peer collaboration inquiry received** — **Mary Olawuyi** (maryolawuyiojo@gmail.com), another participant building a personal AI Agent, emailed offering to collaborate ("work together on the personal AI Agent"). Community networking is active. |
| **2026-11-01** | ✅ **Workspace monthly report received** — Community Chat activity: **3 new likes + 4 new comments** on our Nadi post (incl. reply from Vadim Timchenko). Nadi is gaining community traction. |
| **2026-11-03** | ✅ **Weekly Championship Updates email received (UID 16106)** — official schedule update: **submission standard (prototype / pitch deck / demo video requirements) announced 2026-11-11**; **Submission Portal opens 2026-12-04**; **submission deadline 2027-01-04**; **Grand Finale 2027-05-06 in Dubai** (12 finalists, 4 categories); prize pool **AED 2.5M**; Mentor Circle still "open later"; WhatsApp community `https://chat.whatsapp.com/LqRzoHA3FSp4kroFBeonzb`. Also confirmed **Workshop 3 "Imagine Your First Agent" registered** (Typeform `m6ZTI3Gx`, Zoom `https://us02web.zoom.us/j/84832123514`, 2026-11-04 19:00–21:00 Beijing) and **Weekly Community Catch-Up #3** (2026-11-05 19:00–20:00 Beijing, Zoom `https://us02web.zoom.us/j/82397989045`). |
| **2026-11-03** | ✅ **3 follow-up emails received & Learning Platform verified** — (1) UID 16102 **Welcome** (personal Howspace access link re-issued, live workshops/recordings/community confirmed open; Mentor Circle & Submission Portal "coming soon"; Workshop 3 date typo in email says "28 October" but actual is **11-04**); (2) UID 16126 **Session 3 Form Submitted & Call Link** (Zoom `84832123514` confirmed); (3) UID 16127 **Google Calendar invitation** for Session 3 (Wed 11-04 3–5 PM GST). **Personal access link opened successfully** → `Official Championship Portal` loaded as **Xing Li (logged in)**; **Live Workshops & Sessions page verified**: Agentic AI Sessions register (Typeform `m6ZTI3Gx`) + **previous sessions accessible** (Workshop 1 template, Workshop 2 "Find an Opportunity" recording); Mentors Circle & Submit still disabled. |
| **2026-11-10** | ✅ **Weekly Championship Updates email received (UID 16327)** — 重大更新：**Digital Academy 上线**（10 节自定进度课程：agent 基础/开发/测试/安全/验证 + AI Agent 工具包 + Skill Academy）；**参赛者徽章已可用**（可下载分享 LinkedIn/社媒/邮件签名）；**Masterclass 1 "Design an Agent That Matters"**（11-11 3–5 PM GST，注册 `https://form.typeform.com/to/tZma0NHt`）；**Weekly Community Catch-Up #4**（11-12 3–4 PM GST，Zoom `82397989045`）；**提交标准 11-11 起可用**（prototype/pitch deck/demo video）；**半决赛名单公布 2027-01-29**（新增日期）；**Mentor Circle 计划 11 月中旬开放**；参赛形式个人或团队（≤6 人，每人单独注册，每个 agent 想法单独提交）；**无需编程经验**（code/low-code/no-code 均接受，同等评审）；奖池 AED 2.5M、12 名决赛、Grand Finale 2027-05-06 迪拜；联系邮箱 `createaiagents@bncpublishing.net`；WhatsApp `https://chat.whatsapp.com/LqRzoHA3FSp4kroFBeonzb`（公告专用，已在群勿重复加）；新学习平台访问链接 `https://create-ai-agents-competition.in.howspace.com/1/aa0feea4-7722-4e56-8c86-614103159dbd/463102527`。 |
| **2026-11-11** | ✅ **Submission standard published** (as announced — prototype / pitch deck / demo video requirements now available). **Masterclass 1: Design an Agent That Matters** (3–5 PM GST) — 时间已过，可查看回放。 |
| **2026-11-12** | ✅ **Weekly Community Catch-Up #4** (3–4 PM GST, Zoom `82397989045`) — 时间已过。 |
| **2026-11 中旬** | ⏳ **Mentor Circle scheduled to open mid November** — check the Championship Portal / Learning Platform for the mentorship application window. |
| **2026-11-13** | ✅ **Read the official submission guidelines via external Chrome** (chrome-devtools plugin opened the Submit page successfully). **Submission portal opens 2026-12-04** (encrypted; link published on the Submit page). Got the **full Judging Criteria & Evaluation Guide** (6 criteria, weights 20/20/15/15/20/10) and the **Pitch deck skeleton PDF (35 pages)**. Confirmed **no-code / low-code / coded agents are evaluated equally**, and **revenue is not required** during the Championship (a credible sustainability path is). Full breakdown recorded in §9 below. |
| **2026-11-13** | ✅ **Pitch deck rebuilt to the official skeleton** — downloaded the 35-page skeleton PDF (35.7 MB), extracted all pages, and rebuilt `pitch-deck/index.html` to the recommended **14-page structure** (cover + 12 content pages + thank-you). Added the missing **business-model slide** (target customers, pricing AED 49/mo, cost per task, growth path — criterion 5, 20%) plus Target customers, Performance metrics, User validation, Go-to-market and Founders' team pages. Verified live in external Chrome: all 14 slides render. Detail in §9. |
| **2026-11-13** | ✅ **Inbox checked for anything needing a reply** — scanned the last 30 messages and the 14-day window; no official Championship email requires action. All items are journal/Apple/publisher notices, unrelated to the competition. **No outgoing email needed at this time** (the Submission Portal opens 2026-12-04; nothing to send before then). |
| **2026-11-13** | ✅ **Official Submission FAQ cross-checked via external Chrome** — opened the Learning Platform FAQ → **Submission Questions** (27 items). **KEY FINDING: the official entry requirement is FOUR components, not the three we prepared.** The 2-minute demo **must be embedded in Slide 4** of the pitch deck and played during a **6-minute pitch video** (your face must appear; unlisted YouTube/Vimeo/Canva link, 1080p 16:9, English). Prototype must be judge-accessible via link/credentials until the Championship ends. Dates confirmed: open **2026-12-04**, close **2027-01-04 11:59 GST**, semi-finalists **2027-01-29**. This correction is recorded in §9. **Mentor Circle still disabled** (booking via Mentor Circle once open — FAQ Q202). |
| **2026-11-16** | ✅ **Official phishing/security notice received (via Howspace)** — official Championship communications are sent **only** via Howspace or the official Championship email; do **not** respond to suspicious emails or share project/personal/confidential info with unauthorized senders; **all project submissions & materials must go exclusively through the official Championship portal** (evaluations only happen there; the Championship is not responsible for info shared via unauthorized channels). Personal access link re-issued: `https://create-ai-agents-competition.in.howspace.com/1/3bdc4f9e-f924-447e-8783-a95d89cd9592/463102527` (do not forward). |
| **2026-11-16** | ✅ **Demo video made compliant & embedded in Slide 4** — replaced the static Fatima transcript block on Slide 4 with a playable **real in-agent demo** (`pitch-deck/demo_inagent.mp4`, 2:00, 1080p16:9, 1.35 MB): Fatima (RELEASED lifestyle protocol) / Ahmed (diet advice) / medication request the Guardian **BLOCKS & escalates** (FAQ Q19 trigger → actions → workflow → outcome). Added `#N` hash deep-link to the deck. Pushed to `main` (`add8614`); verified live on Pages: Slide 4 video `readyState 4`, `playing true`, `duration 120s`; `demo_inagent.mp4` → 200 (1.4 MB). |
| **2026-11-16** | ✅ **6-minute pitch video recorded** — `pitch-video/final_pitch.mp4` (5:56, 1080p16:9, photo-based speaker + AI English narration). Still to **host unlisted** (YouTube/Vimeo/Canva) at submission time. |
| **2026-11-16** | ✅ **Judge access confirmed** — repo **public** (no credentials), default branch `main`; live Pages all 200: `/` frontend demo, `/agent-team.html`, `/pitch-deck/` (Slide 4 demo plays). Prototype runs via `git clone` (6 commands, §3). Keep public & re-push before 2027-01-04. |
| **2026-12-04** | ⏳ Submission Portal opens. |
| **2027-01-04** | ⬜ **Submission deadline** — upload prototype URL + pitch deck + demo video + summary report. |
| **2027-01-29** | ⬜ **Semi-finalists announced** (新增日期，来自 11-10 邮件). |
| **2027-05-06** | ⬜ **Grand Finale in Dubai** (12 finalists, 4 categories; prize pool AED 2.5M). |
| **2027-Q1** | Selection committee scores all submissions. |
| **2027-04** | Shortlist announced. Finalists invited to Dubai. |
| **2027-05 Week 1** | Grand Final in Dubai — in-person pitch to jury and public. |
| **Grand Final Day** | Four awards announced (150k USD each) + AI Agent of the Year. |

---

## 7. What we still need from the registrant

1. ✅ **Registration submitted 2026-10-27** — portal confirmed "Thank you for registering!" at <https://www.dubaichamberdigital.com/en/create-ai-agents-register-your-interest>. Our learning & community space opens **October 19**; access link will be emailed from `createaiagents@bncpublishing.net`.
2. ✅ Category confirmed: **Best Personal AI Agent**.
3. ✅ Team size confirmed: **solo** (1).
4. ✅ **Howspace welcome email received 2026-10-29** — Learning Platform access granted (personal link, do not forward). Live Workshops, Recordings, Community Chat open; Mentor Circle & Submission Portal open later.
5. ⬜ Revoke the leaked GitHub tokens listed in the security notice (not required for the competition, but a personal-security must-do).
6. ⬜ Host `demo-video/final.mp4` on a video platform (YouTube unlisted / Vimeo private) and paste the share URL into the Demo video field at **submission time (2027-01)** — the portal requires a hosted URL, not a local file.
7. ⬜ **Mentor Circle scheduled to open mid November** (confirmed via 11-10 email) — check the Championship Portal / Learning Platform for the mentorship application window.
8. ⬜ Join the community groups shared at Q&A if you want peer support: **WhatsApp** `https://chat.whatsapp.com/EWtYRjnWX6xDyBxkHDbXc5` and **Telegram** `https://t.me/+da2ziPN8n6ZjY2Nk`.
9. ⬜ **Reply to Mary Olawuyi's collaboration inquiry** (email 2026-10-29, subject "AI Agents") if you'd like to explore a partnership on a personal AI Agent — she is also building one. (Not required; optional networking.)
10. ⬜ Check the Community Chat notifications for the **3 likes + 4 comments** on the Nadi post and reply to any that warrant a response (e.g. Vadim Timchenko's comment).
11. ✅ **Embed the 2-minute demo in Slide 4** of the pitch deck — official FAQ Q2/Q13/Q16/Q17: the demo **must** be embedded in Slide 4 and played during the 6-minute pitch video; a separate standalone demo upload is **not mandatory**. **Done 2026-11-16** — real in-agent `demo_inagent.mp4` embedded & playable in Slide 4; live on GitHub Pages.
12. ✅ **Record a 6-minute pitch video** that walks through the deck, plays the embedded 2-minute demo, and shows your face (FAQ Q18/Q21/Q22). Submit as an **unlisted YouTube / Vimeo / Canva link**, in English, clear audio, preferably 1080p 16:9, no permission required (Q23). **Recorded 2026-11-16** (`final_pitch.mp4`, 5:56, photo-based speaker + AI English narration) — still to **host unlisted** at submission time.
13. ✅ **Make the prototype accessible to judges** — provide a working link / test credentials; access must remain available **until the end of the Championship** (FAQ Q7/Q8). **Done 2026-11-16** — repo is **public** (no credentials needed); live Pages: `/` (frontend demo), `/agent-team.html`, `/pitch-deck/` (Slide 4 demo plays). Judges run the agent via `git clone` (6 commands, §3). Keep the repo public & re-push before 2027-01-04.
14. ✅ **Demo-video format decided**: current `demo-video/final.mp4` (2:24 silent slideshow) superseded — **done 2026-11-16**, replaced by a **2-minute in-agent demo** (`demo_inagent.mp4`: trigger → actions → workflow → outcome, FAQ Q19) embedded in Slide 4; a longer standalone demo is optional (Q17).

---

## 8. If anything breaks before submission

- **GitHub Pages went down**: push an empty commit to `main` to re-trigger the workflow at <https://github.com/lm203688/nadi-agent/actions>
- **Prototype no longer runs on Python 3.12**: check `prototype/requirements.txt` — it is pinned.
- **Pitch deck looks wrong on a judge's screen**: it is responsive down to 360px wide. If it does not fit, the browser is too old.
- **Demo video too long**: trim with `ffmpeg -i in.mp4 -t 180 -c copy out.mp4`.

---

## 9. Official submission criteria (fetched 2026-11-13 from the Submit page)

Source: official Championship Portal **Submit** page (<https://create-ai-agents-competition.in.howspace.com/submit>), Judging Criteria & Evaluation Guide.

**Submission portal**: encrypted portal opens **2026-12-04** (countdown on the Submit page); submission link will be published on that page. Submissions are accepted **only** through the official online portal.

**Judging criteria & weights** (total 100%):

| # | Criterion | Weight | What judges assess |
|---|---|---|---|
| 1 | Real Value & Problem Validation | 20% | Clearly defined real-world problem, target users, evidence of demand, measurable potential benefits in the UAE and the world. |
| 2 | Technical Execution & Reliability | 20% | A **working AI agent** that completes real tasks, with clear workflows, testing results, demonstrated reliability. |
| 3 | Trust, Safety & Human Oversight | 15% | Data protection, security safeguards, error handling, clear human approval / escalation processes. |
| 4 | Innovation & Defensibility | 15% | What makes the agent different, why an AI agent is needed, competitive advantages. |
| 5 | Business Viability & Scalability | 20% | Clear business model: target customers, revenue / funding strategy, pricing, operating costs, growth potential in the UAE and the world. |
| 6 | Pitch & Communication | 10% | Clear, well-structured pitch deck and demonstration video supported by evidence. |

**Important notes**:
- **No-code, low-code and fully coded agents are evaluated equally.**
- **Revenue is not required during the Championship** — participants should demonstrate a credible path to sustainability.

**Available guides**:
- **Pitch deck skeleton PDF** (35 pages) — download at <https://create-ai-agents-competition.in.howspace.com/widget/pdf/6af2e07bda8ca96a73099a03/inline/6af57d35ea43dfc2990bd180/download>. Use as the skeleton to ensure the pitch is clear, thoughtful & succinct.
- **Judging Criteria & Evaluation Guide** (flip cards) — the six criteria above.

**Self-assessment vs. our submission (prototype / pitch deck / demo video / summary report all Ready)**:
- Criterion 1 (20%): Nadi addresses a real unmet need (visible, safe reasoning in consumer health) — good.
- Criterion 2 (20%): Working agent with 30-case test coverage + CLI + <8s deliberation — strong.
- Criterion 3 (15%): Human-in-the-loop escalation + Guardian red-line rule-set — good; error handling and policy file now expanded in the pitch.
- Criterion 4 (15%): Four-agent deliberation with visible disagreement over a curated, cited knowledge library — defensible.
- Criterion 5 (20%): **Now covered in the rebuilt pitch** — Slide 9 "Revenue model & profitability": target customers (consumer + B2B2C), pricing (AED 49/mo), cost per task, growth path. Credible sustainability path, not a forecast.
- Criterion 6 (10%): **Pitch deck rebuilt to the official 35-page skeleton's 14-page structure** (cover + 12 content pages + thank-you) + 2:24 demo video — ready.

**✅ Done 2026-11-13 — deck rebuilt to the official skeleton**:
- Downloaded the official **35-page Pitch deck skeleton PDF** (35.7 MB) from the Submit page widget endpoint and extracted all page text.
- The skeleton recommends **cover + 12 content pages + thank-you** (14 total). Rebuilt `pitch-deck/index.html` to exactly this structure:
  1. Cover — "A team of AI agents that think out loud before they advise you on health"
  2. Business concept & AI agent
  3. Problem & solution
  4. Target customers & market (user + 3 payers; UAE market sizing)
  5. How the AI agent works (prototype demo transcript)
  6. Technical architecture & safety
  7. Performance metrics & efficiency (30 tests / 100% Guardian catch / <8s)
  8. User validation (3 personas; honest note: interviews pending)
  9. Unique value & competitive landscape (POP / YC / Uoma vs Nadi)
  10. **Revenue model & profitability** — who pays, pricing AED 49/mo, cost per task, growth
  11. Go-to-market plan (3 phases)
  12. Roadmap / key milestones (Q1–Q4 2027)
  13. Founders' story & team (solo founder + gaps to recruit)
  14. Thank-you / ask (mentorship, grant, pilot partner)
- Verified live in Chrome (external): all 14 slides render; commercial-model slide displays target customers, pricing, cost per task and growth path. Honest labelling kept throughout ("no revenue today — prototype", "interviews pending", "figures are estimates").

**⚠️ Important correction discovered 2026-11-13 (official Submission FAQ, fetched from the Learning Platform FAQ → Submission Questions)**:

The official entry FAQ (Q2 "What am I required to submit?") states **FOUR components**, not the three we had prepared. Our current preparation (prototype + 14-page deck + independent 2:24 demo video) is **not yet compliant**. The authoritative requirements are:

1. **AI Agent Prototype** — a working, testable MVP. Must be accessible to judges via a **working link or test credentials**; access must remain until **the end of the Championship** (Q6/Q7/Q8). Simulated inputs are allowed if clearly labelled and the agent performs a real workflow (Q10). Participants cover their own AI usage costs during judging (Q11).
2. **Pitch Deck** — recommended **12–15 slides** (Q12). Must cover: business concept, problem & solution, customers & market, working agent, technical architecture, performance, validation, competitors, revenue model, go-to-market plan, roadmap, team (Q13). **Business model is mandatory** (a credible path to revenue/sustainability; existing revenue not required) (Q14). Business Canvas & Agent Card are **planning tools only, not mandatory uploads** (Q15).
3. **2-minute Demo Video — embedded in Slide 4** of the deck, played during the pitch video (Q2/Q16/Q17). Must show the agent completing a real task: trigger → actions → workflow → outcome (Q19). Edits/sped-up waits allowed if clearly labelled (Q20). A separate standalone demo upload is **not mandatory**; a longer standalone demo is optional (Q17).
4. **6-minute Pitch Video** — walks judges through the deck, including playback of the embedded 2-minute demo, then ~4 minutes presenting problem, solution, business opportunity and vision. **Your face must appear** (Q18/Q21). Solo participants may present alone (Q22). Submit as an **unlisted YouTube / Vimeo / Canva link**, in English, clear audio, preferably 1080p 16:9, no permission needed (Q23).

**Key dates (FAQ)**: Submissions open **2026-12-04**, close **2027-01-04 11:59 AM GST** (Q1); semi-finalists announced **2027-01-29** (Q25); submissions cannot be edited but may be **resubmitted** (Q26); support contact `createaiagents@bncpublishing.net` (Q27).

**Self-assessment against the 4-component requirement — current gaps**:
- ✅ Prototype: runnable MVP + GitHub Pages live link + testable via repo — accessible, but **must confirm credentials & keep live until Championship end** (item 13).
- ✅ Pitch deck: 14 pages, all required sections covered, business model present — compliant (12–15 range).
- ⚠️ **Demo video: NOT yet compliant** — current `demo-video/final.mp4` is a 2:24 silent slideshow, **not** a 2-minute in-agent demo, and is **not embedded in Slide 4** (items 11 & 14).
- ⚠️ **Pitch video: NOT yet started** — no 6-minute pitch video exists, no face-on-camera recording (item 12).

**This is the main remaining work before submission: convert the demo to an in-agent 2-minute demo, embed it in Slide 4, and record a 6-minute face-on-camera pitch video.**

