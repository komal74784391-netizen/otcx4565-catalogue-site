from sundial_cadence import describe, run


def test_describe_returns_text():
    assert isinstance(describe(), str)


def test_run_accepts_empty_config():
    result = run()
    assert result["ok"] is True
