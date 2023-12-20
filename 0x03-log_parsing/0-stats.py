#!/usr/bin/python3
"""reads the stdin line by line and computes metrics"""

import sys


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
        parts = line.split(' ')

        if len(parts) > 2:
            status_code = parts[-2]
            file_size = int(parts[-1])

            # Check if status code is valid
            if status_code in status_codes:
                status_codes[status_code] += 1
                total_size += file_size
                lines_processed += 1

            # Print statistics after every 10 lines
            if lines_processed == 10:
                print('File size: {:d}'.format(total_size))
                sorted_keys = sorted(status_codes.keys())
                for key in sorted_keys:
                    value = status_codes[key]
                    if value != 0:
                        print('{}: {}'.format(key, value))
                lines_processed = 0

except (ValueError, IndexError):
    # Skip lines that do not match the specified format
    pass

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    pass
finally:
    print('File size: {:d}'.format(total_size))
    sorted_keys = sorted(status_codes.keys())
    for key in sorted_keys:
        value = status_codes[key]
        if value != 0:
            print('{}: {}'.format(key, value))
