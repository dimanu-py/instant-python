#!/usr/bin/env python3
import subprocess
import sys


def main() -> None:
	try:
		changed_files = _get_changed_files_between_last_two_heads()
		changed_files = changed_files.stdout.splitlines()
		files_to_search = ["Dockerfile", "pyproject.toml", "poetry.lock"]
		if any(f in changed_files for f in files_to_search):
			print(" * changes detected in tracked files")
			print(" * running make build and make install")
			subprocess.run(["make", "build"], check=True)
			subprocess.run(["make", "install"], check=True)
	except subprocess.CalledProcessError as e:
		print(f"post-merge hook failed: {e}")
		sys.exit(e.returncode)


def _get_changed_files_between_last_two_heads():
	result = subprocess.run(
		[
			"git",
			"diff-tree",
			"-r",
			"--name-only",
			"--no-commit-id",
			"HEAD@{1}",
			"HEAD",
		],
		capture_output=True,
		text=True,
		check=True,
	)
	return result


if __name__ == "__main__":
	main()