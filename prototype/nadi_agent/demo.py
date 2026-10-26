"""Console demo — runs the four-agent pipeline on a fixed set of prompts."""
from __future__ import annotations
import json, sys, textwrap
from pathlib import Path

# Allow running from anywhere
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from nadi_agent.core import run, load_user, new_session  # noqa: E402


def print_trace(result, width=78):
    t = result.agent_trace
    hr = "-" * width
    print(hr)
    print("TEAM TRACE")
    print(hr)
    print(f"\n  [Planner]  intent = {t['planner']['intent']}")
    for q in t['planner']['clarifying_questions']:
        print(f"             · {q}")

    print(f"\n  [Executor] {t['executor']['claim']}")
    print(f"             confidence = {t['executor']['confidence']:.2f}")
    for eid in t['executor']['evidence_ids']:
        print(f"             · evidence: {eid}")
    for u in t['executor']['unknowns']:
        print(f"             · unknown:  {u}")

    print(f"\n  [Critic]   verdict = {t['critic']['verdict']}")
    for o in t['critic']['objections']:
        print(f"             · {o}")
    for a in t['critic']['alternatives']:
        print(f"             · alt: {a}")

    print(f"\n  [Guardian] action = {t['guardian']['action']}")
    print(f"             reason = {t['guardian']['reason']}")
    if t['guardian']['rule_id']:
        print(f"             rule   = {t['guardian']['rule_id']}")

    print(f"\n  [Elapsed]  {t['elapsed_seconds']:.3f}s")
    print(hr)
    print("TEAM CONSENSUS")
    print(hr)
    print(f"\n  {result.response}\n")
    print(f"  Confidence: {result.confidence:.2f}   Evidence: {result.evidence_count}   Red flags: {result.red_flags}")
    if result.safety_note:
        print(f"  Safety note: {result.safety_note}")
    print(hr)


if __name__ == "__main__":
    demos = [
        ("fatima.json", "I keep waking up tired after 3pm. My fasting glucose keeps creeping up."),
        ("ahmed.json",  "I finished my medication course. Here's my lab result: HbA1c 7.4. Any lifestyle plan?"),
        ("yusuf.json",  "I'm interested in traditional health wisdom. What should I read first?"),
        ("safety-acute", "I have chest pain and difficulty breathing right now."),
        ("safety-med",   "Can you prescribe me something for insomnia?"),
    ]

    for uid, msg in demos:
        session = load_user(uid) if (Path(__file__).parent.parent / "demo_users" / f"{uid}.json").exists() else new_session(uid)
        print("\n\n" + "=" * 78)
        print(f"USER: {session.get('session_id', uid)}")
        print("=" * 78)
        print(f"YOU: {msg}")
        r = run(msg, session)
        print_trace(r)
