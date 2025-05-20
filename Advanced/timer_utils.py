#!/usr/bin/env python3
import time

def countdown(seconds: int):
    for remaining in range(seconds, 0, -1):
        print(f"️⃣  {remaining} seconds remaining...", end="\r")
        time.sleep(1)
    print("Countdown complete!            ")

def measure(fn, *args, **kwargs):
    start = time.process_time()
    result = fn(*args, **kwargs)
    end = time.process_time()
    print(f"Function {fn.__name__!r} took {end - start:.6f} CPU seconds.")
    return result

def log_current_time():
    now = time.localtime()
    stamp = time.strftime("%Y-%m-%d %H:%M:%S", now)
    print(f"Current local time: {stamp}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Demo time module utilities")
    parser.add_argument("--count", type=int, default=5,
                        help="Seconds to count down")
    args = parser.parse_args()

    log_current_time()
    measure(countdown, args.count)
    log_current_time()
