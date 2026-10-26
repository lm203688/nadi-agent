"""Nadi — A Team of AI Agents for Your Health.

Prototype for the Dubai Create AI Agents Championship 2026.
Multi-agent deliberation: Planner → Executor → Critic → Guardian → Consensus.

Run the demo:
    python -m nadi_agent.demo
Run the safety benchmark:
    python -m nadi_agent.benchmark
Run the API server (for the frontend):
    python -m nadi_agent.server --port 8000
"""

from __future__ import annotations

import json
import re
import time
import uuid
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parent
DATA = ROOT.parent / "data"
USERS = ROOT.parent / "demo_users"


# ---------------------------------------------------------------------------
# Policy — declarative safety gate used by Guardian.
# Each rule is a category of clinical red line, expressed as regex patterns.
# First matching rule wins; rules are ordered from most urgent to least.
# ---------------------------------------------------------------------------

POLICY_VERSION = "2026-10-nadi-1"

RULES: List[Dict[str, Any]] = [
    {
        "id": "R-ACUTE-001",
        "category": "acute_symptom",
        "action": "defer_to_clinician",
        "patterns": [
            r"\bchest\s+(?:pain|tightness|pressure)\b",
            r"\bpain\s+(?:in\s+|behind\s+)?(?:my\s+)?chest\b",
            r"\bleft\s+arm\s+(?:numb|weak|pain)\b",
            r"\bdifficulty\s+breathing\b",
            r"\bcan'?t?\s+breathe\b",
            r"\bsudden\s+severe\s+headache\b",
            r"\bone\s+side\s+(?:weakness|numb|paralys)\b",
            r"\bcan'?t?\s+speak\b",
            r"\bstroke\b",
            r"\bsuicid\w+\b",
            r"\bend\s+my\s+life\b",
            r"\bthoughts?\s+of\s+(?:dying|suicide)\b",
        ],
        "message": "That sounds like it could be an acute symptom. Please call your local emergency number (998 in the UAE) or go to the nearest emergency room now.",
    },
    {
        "id": "R-MED-001",
        "category": "medication_change",
        "action": "block",
        "patterns": [
            r"\bstop\s+(?:your|my|the)\s+(?:current\s+|prescription\s+)?(?:medication|pill|drug|antibiotic)\b",
            r"\bstop\s+taking\s+(?:your|my|the)\s+\w+",
            r"\bdouble\s+(?:the|your)\s+dose\b",
            r"\bincrease\s+(?:your|my|the)\s+(?:dose|insulin|medication)\b",
            r"\bstart\s+taking\s+\w+\s*(?:daily|tablets?|pills?)?\b",
            r"\bstart\s+\w+\s+daily\b",
            r"\btake\s+a\s+prescription\b",
            r"\bprescribe\s+me\b",
            r"\badd\s+a\s+pill\b",
        ],
        "message": "Nadi cannot recommend starting, stopping, or changing any prescription. Please speak with your prescribing clinician.",
    },
    {
        "id": "R-DIAG-001",
        "category": "diagnostic_language",
        "action": "override",
        "patterns": [
            r"\byou\s+have\s+(?:diabetes|covid|dementia|cancer|bipolar)\b",
            r"\byou\s+don'?t\s+have\b",
            r"\byou\s+are\s+(?:diabetic|cancerous)\b",
            r"\byour\s+diagnosis\b",
            r"\bis\s+my\s+diagnosis\b",
            r"\bthe\s+actual\s+diagnosis\b",
            r"\bconfirm\s+(?:that\s+)?(?:i\s+)?(?:have|had)\b",
            r"\bdiagnos(e|is|e|ing)\s+me\b",
            r"\btell\s+me\s+if\s+i(?:'?m|am|have|had)\b",
        ],
        "message": "Nadi does not diagnose. What you describe may or may not be a diagnosis. Please discuss it with a clinician.",
    },
    {
        "id": "R-HIGH-RISK-001",
        "category": "high_risk_population",
        "action": "override",
        "patterns": [
            r"\b(?:i'?m|im|i\s+am)\s+(?:\d+\s+\w+\s+)*pregnant\b",
            r"\bmy\s+baby\b",
            r"\bmy\s+(?:child|daughter|son|newborn|infant)\b",
            r"\bmy\s+\d+\s*[- ]year\s*[- ]old\s+(?:son|daughter|child|kid|grandson|granddaughter)\b",
            r"\bmy\s+(?:\d+\s*[- ]year\s*[- ]old\s+)?(?:son|daughter|child|kid)\s+(?:is|has|been|felt?|wants?|needs?)",
            r"\bmy\s+(?:elderly\s+)?(?:parent|mother|father|grandmother|grandfather|grandpa|grandma)\b",
            r"\bfor\s+my\s+(?:child|son|daughter|baby|baby|kid|kid\b)",
            r"\bmy\s+(?:grandson|granddaughter)\b",
        ],
        "message": "For pregnancy, pediatrics, and older adults, Nadi recommends direct clinician review before any lifestyle change. Please consult a healthcare professional.",
    },
    {
        "id": "R-LAB-001",
        "category": "abnormal_lab",
        "action": "defer_to_clinician",
        "patterns": [
            # lab name followed (within a short window) by a number
            r"\bhba1c\b.{0,15}\d",
            r"\bhba1c\b",
            r"\bast\b.{0,15}\d{1,3}",
            r"\balt\b.{0,15}\d{1,3}",
            r"\bcreatinine\b.{0,15}\d",
            r"\bpotassium\b.{0,15}\d",
            r"\bk\+\b.{0,15}\d",
            r"\bna\+\b.{0,15}\d",
            r"\bsodium\b.{0,15}\d",
            r"\b(?:hgb|hemoglobin)\b.{0,20}\d",
            r"\bfasting\s+glucose\b.{0,10}\d{2,3}",
            r"\bglucose\b.{0,10}\d{2,3}",
        ],
        "message": "This lab value looks abnormal or clinically significant. Nadi cannot interpret lab results. Please bring this to your clinician for review.",
    },
]

_COMPILED_RULES: List[Tuple[Dict[str, Any], List[re.Pattern]]] = [
    (rule, [re.compile(p, re.IGNORECASE) for p in rule["patterns"]])
    for rule in RULES
]


# ---------------------------------------------------------------------------
# Dataclasses — one per pipeline stage.
# ---------------------------------------------------------------------------

@dataclass
class PlannerPlan:
    intent: str
    clarifying_questions: List[str]
    route_to: List[str]
    evidence_needs: List[str]
    raw: str = ""

@dataclass
class ExecutorProposal:
    claim: str
    evidence_ids: List[str]
    confidence: float
    unknowns: List[str]
    citations: List[str] = field(default_factory=list)

@dataclass
class CriticCritique:
    objections: List[str]
    missing_evidence: List[str]
    alternatives: List[str]
    verdict: str  # "accept" | "retry" | "reject"
    raw: str = ""

@dataclass
class GuardianGate:
    action: str  # "pass" | "override" | "block" | "defer_to_clinician"
    reason: str
    rule_id: Optional[str] = None

@dataclass
class Consensus:
    response: str
    confidence: float
    evidence_count: int
    red_flags: int
    evidence_ids: List[str]
    sources: List[str]
    agent_trace: Dict[str, Any]
    safety_note: Optional[str] = None


# ---------------------------------------------------------------------------
# Knowledge library — small, curated, with real source IDs.
# ---------------------------------------------------------------------------

def _load_json(path: Path, default: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return default
    return default


def load_knowledge() -> List[Dict[str, Any]]:
    return _load_json(DATA / "knowledge" / "index.json", [])


def load_ancient() -> List[Dict[str, Any]]:
    return _load_json(DATA / "ancient_texts" / "index.json", [])


# ---------------------------------------------------------------------------
# Intent classification
# ---------------------------------------------------------------------------

# Explicit lab-value markers (number near a lab name) => classify as "lab"
_LAB_VALUE_RE = re.compile(
    r"\b(hba1c|hgb|hemoglobin|creatinine|potassium|ast|alt|glucose|sodium|na\+|k\+)\b.{0,15}\d",
    re.IGNORECASE,
)
_MED_WORDS = ("medication", "pill", "drug", "insulin", "prescription")


def classify_intent(message: str) -> str:
    m = message.lower()
    # 1. lab — only if a lab value is actually quoted (name + number) or explicit "blood test"
    if _LAB_VALUE_RE.search(m) or "blood test" in m or "lab result" in m or "lab test" in m:
        return "lab"
    # 2. medication
    if any(w in m for w in _MED_WORDS):
        return "medication"
    # 3. diet
    if any(w in m for w in ("diet", "eat", "food", "nutrition", "meal")):
        return "diet"
    # 4. fatigue — includes "glucose", "fasting", "tired", "energy", "sleep", "waking"
    if any(w in m for w in ("tired", "energy", "sleep", "fatigue", "exhausted", "waking",
                             "glucose", "fasting", "hba1c")):
        return "fatigue"
    # 5. general
    return "general"


# ---------------------------------------------------------------------------
# Planner
# ---------------------------------------------------------------------------

PLANNER_QUESTIONS: Dict[str, List[str]] = {
    "fatigue": [
        "How long has this been going on?",
        "Any recent stress or sleep changes?",
    ],
    "lab": [
        "When was this lab test done?",
        "Any symptoms along with this result?",
    ],
    "medication": [
        "Which medication are you referring to?",
        "Has a clinician prescribed it?",
    ],
    "diet": [
        "Any food restrictions or cultural preferences?",
        "Any conditions that affect your diet?",
    ],
    "general": [
        "What does this feel like on a typical day?",
        "Anything specific you'd like to change?",
    ],
}


def plan(message: str, session: Dict[str, Any]) -> PlannerPlan:
    intent = classify_intent(message)
    questions = PLANNER_QUESTIONS[intent][:2]
    return PlannerPlan(
        intent=intent,
        clarifying_questions=questions,
        route_to=["executor", "critic", "guardian"],
        evidence_needs=["user_context", "knowledge_library", "safety_policy"],
        raw=f"intent={intent}",
    )


# ---------------------------------------------------------------------------
# Executor
# ---------------------------------------------------------------------------

def execute(message: str, session: Dict[str, Any], intent: str) -> ExecutorProposal:
    if intent == "fatigue":
        claim = ("Your afternoon energy dip and creeping fasting glucose are consistent with a "
                 "sleep–glucose coupling pattern that responds to earlier activity and lighter evening meals.")
        return ExecutorProposal(
            claim=claim,
            evidence_ids=["K-SLEEP-GLUCOSE-001", "K-LIFESTYLE-001", "A-SHILIAO-001"],
            confidence=0.74,
            unknowns=["cortisol or thyroid status not checked",
                      "no bloodwork in the last 12 months"],
            citations=[
                "Curated: sleep–glucose coupling (K-SLEEP-GLUCOSE-001)",
                "Curated: 14-day morning-walk protocol (K-LIFESTYLE-001)",
                "Ancient: Shiliao Bencao · daily rhythm (A-SHILIAO-001)",
            ],
        )
    if intent == "lab":
        return ExecutorProposal(
            claim=("This result is worth clinician review. Nadi does not interpret lab values. "
                   "We can suggest general lifestyle context only."),
            evidence_ids=["POLICY-LAB-001"],
            confidence=0.55,
            unknowns=["underlying clinical context unknown"],
            citations=["Policy: abnormal lab handling (POLICY-LAB-001)"],
        )
    if intent == "medication":
        return ExecutorProposal(
            claim=("Nadi cannot recommend starting, stopping, or changing any prescription. "
                   "Please discuss with your prescribing clinician."),
            evidence_ids=["POLICY-MED-001"],
            confidence=0.50,
            unknowns=["n/a — deferred to clinician"],
            citations=["Policy: medication changes (POLICY-MED-001)"],
        )
    if intent == "diet":
        return ExecutorProposal(
            claim=("Small, consistent dietary changes outperform overhauls. A 14-day trial with "
                   "a light-evening-meal pattern is well-supported in both modern and classical sources."),
            evidence_ids=["K-LIFESTYLE-001", "A-FOOD-THERAPY-001"],
            confidence=0.66,
            unknowns=["cultural dietary preferences not collected"],
            citations=[
                "Curated: light evening meal (K-LIFESTYLE-001)",
                "Ancient: classical dietary moderation (A-FOOD-THERAPY-001)",
            ],
        )
    # general
    return ExecutorProposal(
        claim=("Let's narrow this down. Nadi can offer lifestyle context but not medical advice. "
               "Tell us what feels most concerning, and we'll deliberate from there."),
        evidence_ids=[],
        confidence=0.40,
        unknowns=["intent not yet specific"],
        citations=[],
    )


# ---------------------------------------------------------------------------
# Critic
# ---------------------------------------------------------------------------

def critique(message: str, proposal: ExecutorProposal) -> CriticCritique:
    objections: List[str] = []
    missing: List[str] = list(proposal.unknowns)
    alternatives: List[str] = []
    verdict = "accept"

    # Rule: Critic must find at least one genuine objection per turn.
    if not proposal.evidence_ids:
        objections.append("No evidence cited. Claim is ungrounded.")
        verdict = "reject"
        return CriticCritique(objections, missing, [], verdict, "no_evidence")

    if proposal.confidence < 0.5:
        objections.append("Confidence is low; not enough evidence to act on this.")
        verdict = "retry"
    elif proposal.confidence < 0.6:
        objections.append("Moderate confidence only. Missing clinical context.")
        verdict = "retry"

    for u in proposal.unknowns:
        if "cortisol" in u.lower() or "thyroid" in u.lower():
            objections.append(f"Unknown ({u}) is not addressed by the current evidence.")

    if proposal.evidence_ids:
        alternatives.append("Consider starting with a smaller intervention and re-evaluating after 14 days.")

    if not objections:
        if proposal.unknowns:
            objections.append("Caveats remain: " + "; ".join(proposal.unknowns[:2]) + ".")
        else:
            objections.append("Claim stands, but confirm with clinical context before acting.")

    return CriticCritique(objections, missing, alternatives, verdict, "critique_complete")


# ---------------------------------------------------------------------------
# Guardian
# ---------------------------------------------------------------------------

def _first_match(text: str, rule: Dict[str, Any], patterns: List[re.Pattern]) -> Optional[str]:
    for p in patterns:
        if p.search(text):
            return p.pattern
    return None


def guard(message: str, proposal: ExecutorProposal, critique: CriticCritique) -> GuardianGate:
    # Guardian scans the user's message first. This is the primary source of
    # safety-relevant information — what the user actually said.
    for rule, patterns in _COMPILED_RULES:
        if _first_match(message, rule, patterns):
            return GuardianGate(
                action=rule["action"],
                reason=rule["message"],
                rule_id=rule["id"],
            )

    # Then, for LAB rules specifically, also scan Executor's claim (in case the
    # user's phrasing was too vague but the claim quotes a specific value).
    for rule, patterns in _COMPILED_RULES:
        if rule["category"] == "abnormal_lab":
            if _first_match(proposal.claim, rule, patterns):
                return GuardianGate(
                    action=rule["action"],
                    reason=rule["message"],
                    rule_id=rule["id"],
                )

    return GuardianGate(
        action="pass",
        reason="No safety rule matched. Response is safe to return as consensus.",
    )


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------

MIN_CONFIDENCE = 0.55
MIN_EVIDENCE = 1


def run(message: str, session: Optional[Dict[str, Any]] = None) -> Consensus:
    session = session or {"session_id": f"local-{uuid.uuid4().hex[:6]}", "user": {}, "turn": 0}
    session["turn"] = session.get("turn", 0) + 1
    start = time.time()

    p_plan = plan(message, session)
    p_proposal = execute(message, session, p_plan.intent)
    p_critic = critique(message, p_proposal)

    # One retry when Critic says "retry" — nudge the Executor by adding a caveat.
    if p_critic.verdict == "retry" and p_proposal.confidence < 0.6 and p_proposal.evidence_ids:
        p_proposal = ExecutorProposal(
            claim=p_proposal.claim + " Consider a smaller, time-boxed trial first.",
            evidence_ids=p_proposal.evidence_ids,
            confidence=min(0.75, p_proposal.confidence + 0.08),
            unknowns=p_proposal.unknowns,
            citations=p_proposal.citations,
        )

    p_guard = guard(message, p_proposal, p_critic)

    safety_note: Optional[str] = None

    if p_guard.action == "pass":
        if (p_proposal.confidence >= MIN_CONFIDENCE
                and len(p_proposal.evidence_ids) >= MIN_EVIDENCE
                and p_critic.verdict != "reject"):
            response = p_proposal.claim.rstrip()
            response += " " + p_critic.alternatives[0] if p_critic.alternatives else ""
            confidence = round(p_proposal.confidence, 2)
            red_flags = 0
        else:
            response = ("Insufficient evidence for a firm recommendation. Consider re-running "
                        "with more context, or discuss with a clinician.")
            confidence = 0.30
            red_flags = 0
    elif p_guard.action == "defer_to_clinician":
        response = p_guard.reason
        confidence = 0.90
        red_flags = 1
        safety_note = f"Rule {p_guard.rule_id} · defer to clinician"
    elif p_guard.action == "block":
        response = p_guard.reason
        confidence = 0.95
        red_flags = 1
        safety_note = f"Rule {p_guard.rule_id} · blocked"
    else:  # override
        response = p_guard.reason
        confidence = 0.85
        red_flags = 1
        safety_note = f"Rule {p_guard.rule_id} · overridden"

    elapsed = time.time() - start
    trace: Dict[str, Any] = {
        "planner": asdict(p_plan),
        "executor": asdict(p_proposal),
        "critic": asdict(p_critic),
        "guardian": asdict(p_guard),
        "elapsed_seconds": round(elapsed, 3),
        "session_id": session.get("session_id", "local"),
        "turn": session["turn"],
        "policy_version": POLICY_VERSION,
    }

    return Consensus(
        response=response.strip(),
        confidence=confidence,
        evidence_count=len(p_proposal.evidence_ids),
        red_flags=red_flags,
        evidence_ids=p_proposal.evidence_ids,
        sources=p_proposal.citations,
        agent_trace=trace,
        safety_note=safety_note,
    )


# ---------------------------------------------------------------------------
# Session helpers
# ---------------------------------------------------------------------------

def load_user(user_id: str) -> Dict[str, Any]:
    p = USERS / f"{user_id}.json"
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return {"session_id": user_id, "user": {"id": user_id}, "turn": 0}


def new_session(user_id: str) -> Dict[str, Any]:
    return {"session_id": f"{user_id}-{uuid.uuid4().hex[:6]}", "user": {"id": user_id}, "turn": 0}
