"""Write one one-line joke about working beside an AI coding agent.

The joke is fixed text: the program only copies it to entry.txt, so the
graded output is byte-identical on every run.
"""

import os
import sys

JOKE = "I asked the agent to fix the bug. It fixed the bug, broke two features, and left a comment saying 'you're welcome.'"


def main():
    if len(sys.argv) > 1:
        out_dir = sys.argv[1]
    else:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
