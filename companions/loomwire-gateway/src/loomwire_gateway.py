"""Minimal public implementation for Loomwire Gateway."""

__version__ = "3.0.4"


def describe():
    """Return a short human readable description."""
    return 'A lightweight router for event-driven services.'


def run(config=None):
    """Entry point used by the command line wrapper."""
    config = config or {}
    return {"tool": 'loomwire-gateway', "config": config, "ok": True}
