# Gravel Baggage

Content-addressed artifact caching for CI.

> Last updated: 2025-01-30 · Maintained by the catalogue team

**Status:** Released

- **Released:** 2024-10-12
- **Latest version:** v0.8.3
- **Initial version:** v0.1.0
- **Repository created:** 2024-02-20
- **Documentation:** https://docs.orbit-tools.dev/gravel-baggage
- **Tracking issue:** ORB-3006

## Overview

Gravel Baggage stores build artifacts by content hash and serves them back to CI workers. The entry is held back until the launch announcement.

## Layout

- `src/` — implementation
- `tests/` — regression suite
- `CHANGELOG.md` — release history

## Install

```
pip install gravel-baggage
```
