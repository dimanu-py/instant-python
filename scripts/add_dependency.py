#!/usr/bin/env python3
import subprocess


def main() -> None:
	dependency = input("Dependency to install: ")
	is_dev = input(f"Do you want to install {dependency} as a dev dependency? (y/n): ")
	add_to_group = input(
		f"Do you want to install the {dependency} inside a group? (y/n): "
	)

	flag = ""
	if is_dev.lower() == "y":
		flag = "--dev"
	if add_to_group.lower() == "y":
		group_name = input("Group name: ")
		flag = f"--group {group_name}"

	cmd = f"uv add {flag} {dependency}".strip()
	subprocess.run(cmd, shell=True, check=True)


if __name__ == "__main__":
	main()