"""Write the entry text for make.fun's "Last Text at One Percent" bounty.

The entry is one last text message, under 200 characters, sent by a
phone at one percent battery, in the dying phone's own voice: it says
goodbye to its charger and the group chat, and admits it will not
remember what its human was about to say. This program writes that
message to entry.txt in the output directory, deterministically: the
same text, byte for byte, on every run. Standard library only; no
network.
"""

import os

LINE = "Tell my charger I loved it. Tell the group chat I tried. I am going dark now, and no, I will not remember what you were about to say."
MAX_LENGTH = 200

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DESTINATION = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    if not 1 <= len(LINE) < MAX_LENGTH:
        raise ValueError("message must be 1 to under 200 characters")
    if not LINE.strip():
        raise ValueError("message must not be only whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("message must be a single line")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Do not chmod the output directory: the grader runs this program
    # as a different user on a directory it does not own, and chmod
    # would fail the run. The file we create gets mode 0644 below,
    # which is all make.fun needs to collect it.
    with open(DESTINATION, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    os.chmod(DESTINATION, 0o644)
    print("wrote {} ({} characters)".format(DESTINATION, len(LINE)))


if __name__ == "__main__":
    main()
