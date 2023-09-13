import pytest
from src.pattern_to_text import (
    pattern_to_words,
    extend_pattern,
    format_output,
    main,
    validate_args,
    InvalidPatternError,
    InvalidIntegerError,
    InsufficientArgumentsError,
)


def test_validate_args():
    validate_args(["pattern_to_text.py", "SST", "5", "2"])
    with pytest.raises(InsufficientArgumentsError):
        validate_args(["pattern_to_text.py", "SST"])

    with pytest.raises(InvalidPatternError):
        validate_args(["pattern_to_text.py", "SSZ", "5", "2"])

    with pytest.raises(InvalidIntegerError):
        validate_args(["pattern_to_text.py", "SST", "5", "abc"])


def test_extend_pattern():
    assert extend_pattern("SST", 0) == ""
    assert extend_pattern("SST", 1) == "S"
    assert extend_pattern("SST", 2) == "SS"
    assert extend_pattern("SST", 3) == "SST"
    assert extend_pattern("SST", 5) == "SSTSS"
    assert extend_pattern("SST", 6) == "SSTSST"
    assert extend_pattern("SST", 7) == "SSTSSTS"


def test_pattern_to_words():
    assert pattern_to_words("SST") == ["Soft", "Soft", "Tough"]
    assert pattern_to_words("ST") == ["Soft", "Tough"]
    assert pattern_to_words("S") == ["Soft"]
    assert pattern_to_words("T") == ["Tough"]
    assert pattern_to_words("") == []


def test_format_output():
    assert format_output(["Soft", "Soft", "Tough"]) == "Soft, Soft and Tough."
    assert format_output(["Soft", "Soft"]) == "Soft and Soft."
    assert format_output(["Soft"]) == "Soft."
    assert format_output(["Tough"]) == "Tough."
    assert format_output([]) == ""


def test_main(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["pattern_to_text.py", "SST", "5", "2"])

    main()
    captured = capsys.readouterr()

    lines = captured.out.strip().split("\n")
    assert lines[0] == "Soft, Soft, Tough, Soft and Soft."
    assert lines[1] == "Soft and Soft."

    monkeypatch.setattr("sys.argv", ["pattern_to_text.py", "SSZ", "5", "2"])

    with pytest.raises(InvalidPatternError):
        main()
