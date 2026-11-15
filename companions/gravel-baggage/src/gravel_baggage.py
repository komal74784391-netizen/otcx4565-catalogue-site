"""Minimal public implementation for Gravel Baggage."""

__version__ = "0.8.3"


def describe():
    """Return a short human readable description."""
    return 'Content-addressed artifact caching for CI.'


def run(config=None):
    """Entry point used by the command line wrapper."""
    config = config or {}
    return {"tool": 'gravel-baggage', "config": config, "ok": True}
