#!/usr/bin/python3
"""Interview Module 3"""

import sys
import signal


def print_metrics(status_code_count, total_file_size):
    """Print the collected metrics
        Processing and Storing Metrics
        track the total number file
        track the total number occurance of each status code
    Args:
        status_code_count: dict of the status of the code
        total_file_size: total size of the file
    Retunr:
        0
    """
    print("File size: {}".format(total_file_size))
    for key, val in sorted(status_code_count.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_file_size = 0
code = 0
line_count = 0
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


def handle_interrupt(signal, frame):
    """Handle keyboard interrupt signal"""
    print_metrics(status_code_count, total_file_size)
    sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)
try:
    for line in sys.stdin:
        parts = line.split()
        parts = parts[::-1]

        if len(parts) < 2:
            continue
        file_size = int(parts[0])
        status_code = parts[1]

        total_file_size += file_size

        if status_code in status_code_count:
            status_code_count[status_code] += 1
        line_count += 1

        if line_count % 10 == 0:
            print_metrics(status_code_count, total_file_size)
except Exception as e:
    pass
print_metrics(status_code_count, total_file_size)
