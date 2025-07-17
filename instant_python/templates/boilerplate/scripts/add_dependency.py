#!/usr/bin/env python3
import subprocess

{% if general.dependency_manager == "pdm" -%}
def main() -> None:
  dependency = input("Dependency to install: ")
  is_dev = input(f"Do you want to install {dependency} as a dev dependency? (y/n): ")
  add_to_group = input(
    f"Do you want to install the {dependency} inside a group? (y/n): "
  )

  dev_flag = ""
  group_flag = ""
  if is_dev.lower() == "y":
    dev_flag = "--dev"
  if add_to_group.lower() == "y":
    group_name = input("Group name: ")
    group_flag = f"--group {group_name}"

  cmd = f"pdm add {dev_flag} {group_flag} {dependency}".strip()
  subprocess.run(cmd, shell=True, check=True)

{%- elif general.dependency_manager == "uv" -%}
def main() -> None:
  dependency = input("Dependency to install: ")
  is_dev = input(f"Do you want to install {dependency} as a dev dependency? (y/n): ")
  add_to_group = input(
    f"Do you want to install the {dependency} inside a group? (y/n): "
  )

  flag = ""
  if is_dev.lower() == "y":
    flag = "-d"
  if add_to_group.lower() == "y":
    group_name = input("Group name: ")
    flag = f"-G {group_name}"

  cmd = f"uv add {flag} {dependency}".strip()
  subprocess.run(cmd, shell=True, check=True)
{%- endif %}


if __name__ == "__main__":
  main()

