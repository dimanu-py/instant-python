import subprocess

from instant_python.installer.dependency_manager import DependencyManager
from instant_python.question_prompter.question.boolean_question import BooleanQuestion
from instant_python.question_prompter.question.free_text_question import FreeTextQuestion


class UvManager(DependencyManager):
    def __init__(self, project_directory: str) -> None:
        self._project_directory = project_directory
        self._uv = "~/.local/bin/uv"

    def install(self) -> None:
        print(">>> Installing uv...")
        subprocess.run(
            "curl -LsSf https://astral.sh/uv/install.sh | sh",
            shell=True,
            check=True,
            stdout=subprocess.DEVNULL,
        )
        print(">>> uv installed successfully")

    def install_python(self, version: str) -> None:
        command = f"{self._uv} python install {version}"
        print(f">>> Installing Python {version}...")
        subprocess.run(
            command,
            shell=True,
            check=True,
            cwd=self._project_directory,
            stdout=subprocess.DEVNULL,
        )
        print(f">>> Python {version} installed successfully")

    def install_dependencies(self, dependencies: list[str]) -> None:
        self._create_virtual_environment()
        for dependency_name in dependencies:
            self._install_dependency(dependency_name)

    def _install_dependency(self, dependency_name: str) -> None:
        is_dev = BooleanQuestion(
            key="is_dev",
            message=f"Do you want to install {dependency_name} as a dev dependency?",
            default=False,
        ).ask()["is_dev"]
        add_to_group = BooleanQuestion(
            key="add_to_group",
            message=f"Do you want to install the {dependency_name} inside a group?",
            default=False,
        ).ask()["add_to_group"]

        flag = self._generate_flag(add_to_group, is_dev)

        command = f"{self._uv} add {flag} {dependency_name}"
        subprocess.run(
            command,
            shell=True,
            check=True,
            cwd=self._project_directory,
            stdout=subprocess.DEVNULL,
        )
        print(f">>> {dependency_name} installed successfully")

    @staticmethod
    def _generate_flag(add_to_group: bool, is_dev: bool) -> str:
        flag = ""
        if is_dev:
            flag = "--dev"
        if add_to_group:
            group_name = FreeTextQuestion(
                key="group_name", message="Enter the name of the group"
            ).ask()["group_name"]
            flag = f"--group {group_name}"
        return flag

    def _create_virtual_environment(self) -> None:
        command = f"{self._uv} sync"
        subprocess.run(
            command,
            shell=True,
            check=True,
            cwd=self._project_directory,
            stdout=subprocess.DEVNULL,
        )
