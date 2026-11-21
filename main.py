"""The Dune.

A short text written to make the reader feel awe: a quiet desert scene
whose scale keeps growing after the last line.

When run, this program writes the text to entry.txt inside the output
directory given by the MAKEFUN_OUTPUT_DIR environment variable, or to
/output/entry.txt when that variable is not set.
"""

import os
import sys

TEXT = (
    "The dune moves a few feet a year. "
    "It buries a fence post, and years later gives it back to a boy "
    "who never knew the man who set it. "
    "The sand is in no hurry. "
    "It was crossing before the first road, and will still be crossing "
    "when the last road is gone."
)


def output_path():
    """Resolve the output directory for entry.txt."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir and os.path.isabs(output_dir):
        return os.path.join(output_dir, "entry.txt")
    return "/output/entry.txt"


def main():
    """Write the text to entry.txt and exit 0."""
    path = output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
