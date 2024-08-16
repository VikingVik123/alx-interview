#!/usr/bin/python3
import sys
import signal

line_count = 0
file_count = 0
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
    }

def print_stats():
    """
    method 2 print d stats
    """
    print(f"File size: {file_count}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """
    Handle keyboard interruption
    """
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()

        if len(parts) < 7 or not parts[-1].isdigit() or not parts[-2].isdigit():
            continue

        ip_address = parts[0]
        date = parts[3] + " " + parts[4]
        method = parts[5][1:]
        path = parts[6]
        protocol = parts[7][:-1]
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        if method == "GET" and path == "/projects/260" and protocol == "HTTP/1.1":
            file_size += file_size

            if status_code in status_codes:
                status_codes[status_code] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_stats()

except Exception as e:
    print(f"An error occurred: {e}")
print_stats()