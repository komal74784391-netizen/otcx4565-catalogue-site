"""Minimal public implementation for ChronoLanes."""

__version__ = "1.6.2"


def describe():
    """Return a short human readable description."""
    return 'Deterministic scheduling for small data teams.'


def run(config=None):
    """Entry point used by the command line wrapper."""
    config = config or {}
    return {"tool": 'chronolanes-scheduler', "config": config, "ok": True}
