#!/usr/bin/env python3
import subprocess


def main() -> None:
	dependency = input("Dependency to remove: ")
	is_dev = input(f"Is {dependency} a dev dependency? (y/n): ")
	belongs_to_group = input(f"Does {dependency} belong to a group? (y/n): ")

	flag = ""
	if is_dev.lower() == "y":
		flag = "--dev"
	if belongs_to_group.lower() == "y":
		group_name = input("Group name: ")
		flag = f"--group {group_name}"

	cmd = f"uv remove {flag} {dependency}".strip()
	subprocess.run(cmd, shell=True, check=True)


if __name__ == "__main__":
	main()
