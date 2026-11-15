"""Minimal public implementation for Sundial Cadence."""

__version__ = "1.2.0"


def describe():
    """Return a short human readable description."""
    return 'Opinionated metrics collection for long-running jobs.'


def run(config=None):
    """Entry point used by the command line wrapper."""
    config = config or {}
    return {"tool": 'sundial-cadence', "config": config, "ok": True}
