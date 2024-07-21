#!/usr/bin/python3
"""Parsing an access log file to print stats"""

import re


r = re.compile(r'^((1?\d?\d|2[0-4]\d|25[0-5])(\.| - )){4}'
               r'\[\d.+\d\] "GET /projects/260 HTTP/1\.1" '
               r'(?P<status_code>[2-5]0[0-5]) (?P<file_size>\d+)$')

total_size = 0
codes = {}


def print_stats():
    """print the current stats in stdout"""
    print("File size: {}".format(total_size))
    for code, num in sorted(codes.items()):
        print("{}: {}".format(code, num))


def main():
    """Start reading logs from stdin forever"""
    global total_size
    while True:
        for _ in range(10):
            match = r.match(input())
            if not match:
                continue
            d = match.groupdict()
            code = d["status_code"]
            codes[code] = codes.get(code, 0) + 1
            total_size += int(d["file_size"])
        print_stats()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_stats()
        raise
    except EOFError:
        print_stats()
        exit()
