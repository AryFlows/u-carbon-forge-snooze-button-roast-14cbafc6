"""Frost Overtime Alarm — one-line snooze-button roast.

Writes a single roast of an alarm clock that rings at 6 AM on a
Saturday to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Stdlib only.
"""

import os

LINE = "You had one job: wake me for work. It's 6 AM on a Saturday and you're ringing like overtime is a personality trait."


def main():
    if not 1 <= len(LINE) <= 200 or "\n" in LINE:
        raise SystemExit("line fails the 1-200 char single-line gate")
    if LINE != LINE.strip() or not LINE.strip():
        raise SystemExit("line must not be blank or padded")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
