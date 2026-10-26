# Demo Video — Storyboard

20 shots. 2 minutes 20 seconds. Each shot is 5–12 seconds.

## Shot list

| # | Time | Duration | Content | Camera / Motion | SFX |
|---|------|----------|---------|-----------------|-----|
| 1 | 0:00 | 3s | Fade from black to Nadi wordmark | Static, subtle scale 0.98 → 1.0 | Ambient hum fades in |
| 2 | 0:03 | 4s | Tagline types in letter-by-letter: "A team of AI agents..." | Text appears character by character, ~12 chars/sec | Hum continues |
| 3 | 0:07 | 4s | Tagline completes: "...that think out loud before they advise you on health." | Static | Hum resolves |
| 4 | 0:11 | 4s | Four-agent grid appears — Planner, Executor, Critic, Guardian | Grid columns slide in from left, staggered 100ms | Silence |
| 5 | 0:15 | 4s | Four roles reveal (one line each, under each name) | Text fades in under each column | Silence |
| 6 | 0:19 | 6s | Transition to Agent Team page (Fatima persona, empty) | Slide down from shot 4, page appears | Silence |
| 7 | 0:25 | 6s | Fatima's message types in the input box | Typewriter effect | Silence |
| 8 | 0:31 | 6s | "Send" button clicked. Loading state: "The team is meeting..." | Loading indicator | Silence |
| 9 | 0:37 | 6s | Planner column fills with clarifying questions | Text stream-in from top of column | Silence |
| 10 | 0:43 | 6s | Fatima types answers to Planner's questions | Typewriter effect | Silence |
| 11 | 0:49 | 8s | Executor column fills — citations pop in one by one | Each citation slides in with a source ID badge | Silence |
| 12 | 0:57 | 6s | Critic column lights up — objection highlighted | Column accent shifts to sand color, text highlights | Silence |
| 13 | 1:03 | 6s | Executor's first proposal is struck through, then retries | Strikethrough animation, then Executor column resets and re-fills | Silence |
| 14 | 1:09 | 6s | Guardian column lights up in clay — "Pass" chip appears | Column accent shifts to clay, chip animates in | Silence |
| 15 | 1:15 | 10s | Team consensus bar appears below the grid — full details | Bar slides up from bottom | Silence |
| 16 | 1:25 | 8s | Transcript scroll-through — the full timeline | Smooth scroll | Silence |
| 17 | 1:33 | 10s | Transition to Ahmed persona — user message + Guardian catch | Fade | Silence |
| 18 | 1:43 | 6s | Guardian output: "Please see a clinician" | Text animates in, Guardian column pulses once | Silence |
| 19 | 1:49 | 12s | Roadmap three-column layout + number row | Column reveal, then number row | Silence |
| 20 | 2:01 | 19s | End card — wordmark + tagline + Arabic + contact | Static, ambient hum fades in and out | Hum fades in, resolves |

## Total runtime

20 shots × ~7s average = 140 seconds (2:20)

## Frame rates

- 24 fps for video capture (natural cinematic cadence)
- 60 fps for UI captures (smooth agent-column animation)

## Aspect ratios

- 16:9 for the deck and end card
- 16:9 for all UI captures
- No vertical cuts, no story-style verticals

## Color grade

The bone background (var(--bone) = #f5efe4) stays warm throughout. No cool color grade. No LUT. The grade matches the pitch deck exactly.

## Text overlays

Every on-screen text uses:

- **Titles**: Fraunces 600, letter-spacing -0.01em
- **Body**: Inter 400 / 500
- **Mono / labels**: JetBrains Mono 400, letter-spacing +0.06em
- **Agent role labels**: JetBrains Mono 10px, uppercase, letter-spacing +0.14em

## Captions

Every subtitle line is short. Never more than 9 words per line. See [`subtitles_en.srt`](subtitles_en.srt).

## What is deliberately not in the video

- No screenshots of HealthLens.
- No logos of partner companies.
- No city skyline B-roll.
- No stock photography of anyone touching an earbud or holding a phone to their ear.
- No music during the deliberation (shots 6–18).
- No voiceover saying "we've built something amazing".

The video is about watching a team deliberate. Everything else would be noise.
