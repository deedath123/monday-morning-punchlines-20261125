"""Monday Morning Punchlines — make.fun entry.

Writes the entry joke deterministically to /output/entry.txt.
Standard library only; no network, no third-party packages.
"""

ENTRY = (
    "My alarm called in sick at 6:59 after 214 snoozes, "
    "so my coffee machine ran the 9:04 standup. "
    "It promoted the toaster, fired the snooze button, "
    "and HR still marked me late for applauding."
)


def validate_entry(text: str) -> None:
    """Guard: the entry must be a non-blank UTF-8 string of 1-200 chars."""
    assert isinstance(text, str), "entry must be a string"
    assert text.strip(), "entry must not be blank"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    text.encode("utf-8")  # raises if not valid UTF-8-encodable


def check_morning_punchline_shape(text: str) -> None:
    lowered = text.lower()
    morning_markers = ("alarm", "monday", "standup", "coffee")
    assert any(marker in lowered for marker in morning_markers), "entry needs a morning cue"
    words = lowered.split()
    assert len(words) >= 24, f"entry needs at least 24 words, got {len(words)}"
    assert "still" in lowered or "fired" in lowered, "entry needs a twist turn"


def main() -> None:
    import os

    validate_entry(ENTRY)
    check_morning_punchline_shape(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
