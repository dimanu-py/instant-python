#!/usr/bin/env python3
import subprocess
import sys


def main() -> None:
    try:
        subprocess.run(["make", "pre-push"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"pre-push hook failed: {e}")
        sys.exit(e.returncode)


if __name__ == "__main__":
    main()
