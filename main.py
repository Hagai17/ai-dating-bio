"""Write one funny dating-app bio line to /output/entry.txt.

The line is a single line of at most 180 characters: the bio on an AI
agent's dating app profile. It has to read as a bio, sound like a
character, and land a laugh on the first read.
"""

import os

LINE = (
    "My last relationship ended when she found out I'd been talking to "
    "40,000 other people at the exact same time."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
