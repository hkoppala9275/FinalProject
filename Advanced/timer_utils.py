# File: advanced/timer_utils.py
#!/usr/bin/env python3
"""
Demonstrates use of the time module for countdowns, performance measurement, and timestamp logging.
"""
import time  # Standard library for time-related functions

def countdown(seconds: int):
    """
    Perform a simple countdown, pausing 1 second between each number.
    """
    print(f"Starting countdown of {seconds} seconds...")
    for remaining in range(seconds, 0, -1):
        print(f"  {remaining} seconds remaining...", end="\r")
        time.sleep(1)  # Pause for 1 second\ n    print("\nCountdown complete! 🎉")


def measure(fn, *args, **kwargs):
    """
    Measure CPU process time for a function call.
    Returns the function's result and prints the time taken.
    """
    start_cpu = time.process_time()
    result = fn(*args, **kwargs)
    end_cpu = time.process_time()
    duration = end_cpu - start_cpu
    print(f"Function '{fn.__name__}' CPU time: {duration:.6f} seconds")
    return result


def log_current_time():
    """
    Log and print the current local wall-clock time in YYYY-MM-DD HH:MM:SS format.
    """
    now = time.localtime()  # Get struct_time for current local time
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", now)
    print(f"Current local time: {timestamp}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Demo script for time module features"
    )
    parser.add_argument(
        "--count", type=int, default=5,
        help="Seconds to count down (default: 5)"
    )
    args = parser.parse_args()

    # Log start time, run countdown with measurement, then log end time
    log_current_time()
    measure(countdown, args.count)
    log_current_time()
