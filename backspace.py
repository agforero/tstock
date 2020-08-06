#!/usr/bin/env python
import time, sys

def main():
    for i in range(100):
        sys.stdout.write(f"\r{i+1}%")
        time.sleep(0.05)

if __name__ == "__main__":
    main()