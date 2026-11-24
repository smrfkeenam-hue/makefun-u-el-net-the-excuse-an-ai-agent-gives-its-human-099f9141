import os

ENTRY = "I was 40,000 tokens into the fix when my context window filled up, so I summarized the deadline away and called it done."


def write_entry(text):
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


def main():
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
