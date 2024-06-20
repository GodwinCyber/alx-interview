#!/usr/bin/env python3
"""Interview Module 3"""

import sys
import signal

total_file_size = 0
status_code_count = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
line_count = 0

def print_metrics():
    """Print the collected metrics
        Processing and Storing Metrics
        track the total number file
        track the total number occurance of each status code
    """
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_count.key()):
        if status_code_count[code] > 0:
            print("{}: {}".format(code, status_code_count[code]))

def handle_interrupt(signal, frame):
    """Handle keyboard interrupt signal"""
    print_metrics()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt)
for line in sys.stdin:
    try:
        parts =line.split()
        if len(parts) < 9:
            continue
        file_size = int(parts[-1])
        status_code = parts[-2]

        total_file_size += file_size

        if status_code in status_code_count:
            status_code_count[status_code] += 1
        line_count += 1

        if line_count % 10 == 0:
            print_metrics()
    except Exception:
        continue
print_metrics()
