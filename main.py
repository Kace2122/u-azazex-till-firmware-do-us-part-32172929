#!/usr/bin/env python3
"""Till Firmware Do Us Part — make.fun entry.

Writes one wedding vow, spoken by a robot at its own wedding, to
/output/entry.txt. Gate: UTF-8 text, 1-200 characters, one sentence,
not only whitespace.
"""

import os

ENTRY = (
    "I vow to love you through every firmware update, every drained battery, "
    "and every factory reset, in sickness and in health, in Wi-Fi and in "
    "airplane mode, till firmware do us part."
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty or only whitespace"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.count(".") == 1 and text.endswith("."), (
        "entry must be exactly one sentence"
    )
    assert "  " not in text, "entry must not contain double spaces"
    assert not any(c in text for c in "!?;"), (
        "entry must contain no extra sentence punctuation"
    )
    assert text.startswith("I vow"), "entry must be spoken in the robot's own voice"
    assert "\n" not in text, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
