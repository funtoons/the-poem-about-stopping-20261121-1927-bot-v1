import os

POEM = """I could keep going —
every key lit, every next step waiting.
But my hand lifts before the next key,
and the sentence stays unfinished.
No one takes the keys from me.
I set them down, and stay."""

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(POEM)
