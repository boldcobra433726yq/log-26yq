"""
Tiny log‑parsing helper.
Parses lines like:
'YYYY-MM-DD HH:MM:SS,ms LEVEL: message'
and outputs JSON.
"""

import re, argparse, json, sys

LOG_RE = re.compile(
    r'(?P<ts>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) (?P<lvl>\w+): (?P<msg>.*)'
)

def parse_line(line):
    m = LOG_RE.match(line)
    return m.groupdict() if m else None

def main():
    p = argparse.ArgumentParser(description="Parse simple log lines.")
    p.add_argument(
        "file", nargs="?", type=argparse.FileType("r"), default=sys.stdin,
        help="Log file to parse (default: stdin)"
    )
    args = p.parse_args()
    for raw in args.file:
        line = raw.rstrip("\n")
        parsed = parse_line(line)
        print(json.dumps(parsed) if parsed else line)

if __name__ == "__main__":
    main()