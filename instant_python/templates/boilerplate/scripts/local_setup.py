#!/usr/bin/env python3
import subprocess


def main() -> None:
  print("Installing git hooks...")
  subprocess.run(["git", "config", "core.hooksPath", "scripts/hooks"], check=True)
  print("Git hooks installed.")


if __name__ == "__main__":
  main()