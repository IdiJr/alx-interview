#!/usr/bin/python3
"""reads the stdin line by line and computes metrics"""

import sys


def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


lines_processed = 0
total_size = 0
status_codes = {'200': 0,
                '301': 0,
                '400': 0,
                '401': 0,
                '403': 0,
                '404': 0,
                '405': 0,
                '500': 0}

try:
    for line in sys.stdin:
        parts = line.split()

        if len(parts) >= 9:
            status_code = parts[-2]
            file_size = int(parts[-1])

            # Check if status code is valid
            if status_code in status_codes:
                status_codes[status_code] += 1
                total_size += file_size
                lines_processed += 1

            # Print statistics after every 10 lines
            if lines_processed == 10:
                print_stats(total_size, status_codes)
                lines_processed = 0

except (ValueError, IndexError):
    # Skip lines that do not match the specified format
    pass

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print_stats(total_size, status_codes)
