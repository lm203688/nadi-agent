"""Nadi Agent — package entry. Exposes the public API."""
from .core import (
    Consensus,
    PlannerPlan,
    ExecutorProposal,
    CriticCritique,
    GuardianGate,
    run,
    plan,
    execute,
    critique,
    guard,
    load_user,
    new_session,
    POLICY_VERSION,
)

__all__ = [
    "Consensus", "PlannerPlan", "ExecutorProposal", "CriticCritique", "GuardianGate",
    "run", "plan", "execute", "critique", "guard",
    "load_user", "new_session",
    "POLICY_VERSION",
]

__version__ = "0.1.0-championship"
