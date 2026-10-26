# Registration Form — Fill-in Checklist for Nadi

> Open the form at: <https://www.dubaichamberdigital.com/en/create-ai-agents-register-your-interest>
> Then walk down this list top-to-bottom. Values I've pre-filled are in **[bold]**. Values you must supply yourself are marked `[YOU]`.

The form is built with Liferay's DDM (dynamic form) and renders client-side. The visible fields typically include:

---

## Personal / Team Lead

| Field | Value |
|---|---|
| First Name | `[YOU]` — your legal name as it appears on your passport / ID |
| Last Name | `[YOU]` — same source |
| Email | `[YOU]` — a personal email you can check (the organizers send submission-window emails here) |
| Mobile Number | `[YOU]` — with country code, e.g. `+971…` for UAE or `+86…` for China |
| Country / Country of Residence | `[YOU]` — pick your actual residence |
| LinkedIn (optional) | **[https://www.linkedin.com/in/lm203688](https://www.linkedin.com/in/lm203688)** ← update to your real URL |
| GitHub (optional) | **[https://github.com/lm203688/nadi-agent](https://github.com/lm203688/nadi-agent)** |

---

## Team

| Field | Value |
|---|---|
| Team name | **[Nadi]** (same as the product) |
| Team size | **[1 — Solo participant]** *(if you add teammates later, expand to 2–6)* |
| Team members (only if >1) | *(names + emails of each co-founder)* |

---

## Category & Track

| Field | Value |
|---|---|
| Main category | **[Best Personal AI Agent]** |
| Sub-track | **[New AI Agent ability]** |
| Youth category (<21 years old)? | **[No]** *(only check "Yes" if you qualify)* |

---

## Project

| Field | Value |
|---|---|
| Project name | **[Nadi]** |
| One-line description | **[Nadi is a 4-agent personal health assistant that helps lay users understand symptoms, decide whether to seek care, and act safely at home. Planner · Executor · Critic · Guardian. Runs on-device.]** |
| Prototype URL | **[https://lm203688.github.io/nadi-agent/](https://lm203688.github.io/nadi-agent/)** |
| Pitch deck URL | **[https://lm203688.github.io/nadi-agent/pitch-deck/](https://lm203688.github.io/nadi-agent/pitch-deck/)** |
| Summary report URL | **[https://github.com/lm203688/nadi-agent/blob/main/docs/00-summary-report.md](https://github.com/lm203688/nadi-agent/blob/main/docs/00-summary-report.md)** |
| Demo video URL | `[YOU]` — render `demo-video/final.mp4` locally and upload it to a link the judges can open (Google Drive public link / Streamable / direct link on the submission portal). Instructions: see [`demo-video/`](../demo-video/) and [`docs/11-final-submission-checklist.md`](11-final-submission-checklist.md). |
| Summary report (attached) | **[Attach `docs/00-summary-report.md`](../docs/00-summary-report.md)** *(the form accepts a text/pasted summary or file upload — if only pasting is allowed, paste the file's contents)* |

---

## Consents — `[YOU]` MUST tick these yourself

- ☐ I have read and accept the **Terms & Conditions** of the Create AI Agents Championship.
- ☐ I confirm that the AI Agent submitted is my **original work** and does not infringe any third-party IP.
- ☐ I confirm the Agent does not include **political, religious, or immoral content** and complies with UAE laws and regulations.
- ☐ I understand that if I become a Finalist I must **attend the final ceremony in Dubai in person** (may require UAE Security Clearance).
- ☐ I understand that to receive the prize fund I will need a **Dubai-based trade license** if I am not already licensed.
- ☐ I grant DCDE a **non-exclusive, royalty-free license** to use my Agent for promotional purposes.

---

## Submit

1. Double-check every `[YOU]` field above is filled.
2. Check every ☐ above.
3. Click **Submit**.
4. Save the confirmation email / reference number.

---

## What happens next

- You'll receive a confirmation email from DCDE.
- Between **2026-10-26 → 2027-01** you have time to iterate on the Agent, upload the demo video, and refine the pitch.
- When the submission window opens in **2027-01**, you upload the final prototype URL, pitch deck, demo video, and summary report through the portal.

---

## Quick copy-paste blocks

### One-line description (for short fields)
```
Nadi is a 4-agent personal health assistant: Planner, Executor, Critic, and Guardian — helping lay users understand symptoms, decide whether to seek care, and act safely at home. Runs on-device.
```

### Longer pitch blurb (for medium fields, ~200 chars)
```
Nadi is a personal health AI Agent built from four cooperating sub-agents — Planner, Executor, Critic, and Guardian. It answers health questions with citations, tells you when to self-manage vs. seek care, and refuses unsafe actions via a deterministic rule engine. Runs 100% on-device; designed for Dubai's multilingual, multigenerational public.
```

### Long-form summary (for the "describe your project" field, if 1000+ chars)
```
Nadi is a personal health AI Agent for lay users who want clear, safe, and honest answers to everyday health questions. It combines four cooperating sub-agents — Planner (breaks the question into steps), Executor (fetches and grounds each step with citations), Critic (checks the reasoning for red flags), and Guardian (a deterministic rule engine that refuses unsafe advice, flags emergencies, and always tells users to seek care when indicated). The Agent runs 100% on-device with no cloud calls, which makes it deployable on Dubai's public-sector infrastructure without new privacy or data-flow approvals.

Live demo: https://lm203688.github.io/nadi-agent/
Pitch deck: https://lm203688.github.io/nadi-agent/pitch-deck/
Source:     https://github.com/lm203688/nadi-agent

The demo walks through a symptom-triage use case (migraine) and shows the Guardian agent refusing to recommend medication for an allergy history the user mentioned three turns earlier — a behaviour impossible with a single-shot chatbot.

Built solo by the registrant. Original work. No third-party IP beyond Apache-2.0 and MIT open-source dependencies (see repo LICENSE files).
```
