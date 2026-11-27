#!/usr/bin/env python3
"""One Emoji, One Dream Vacation: write exactly one emoji to /output/entry.txt."""
import os

EMOJI = "🗻"

# The entry must be exactly one emoji, 1-8 characters, not only white space.
assert 1 <= len(EMOJI) <= 8, f"entry is {len(EMOJI)} chars"
assert EMOJI.strip(), "must not be only whitespace"
assert "\n" not in EMOJI, "must be a single line"

os.makedirs("/output", exist_ok=True)
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "entry.txt")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(EMOJI)

# Read back and verify: a silent bad write must fail loudly, not pass quietly.
with open(out_path, encoding="utf-8") as f:
    back = f.read()
assert back == EMOJI, f"read-back mismatch: wrote {len(EMOJI)} chars, read {len(back)}"
assert back.strip() and "\n" not in back, "read-back failed line checks"

print(f"wrote {len(EMOJI)} char to {out_path}")
