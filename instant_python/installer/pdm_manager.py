import subprocess

from instant_python.installer.dependency_manager import DependencyManager
from instant_python.question_prompter.question.boolean_question import BooleanQuestion
from instant_python.question_prompter.question.free_text_question import FreeTextQuestion


class PdmManager(DependencyManager):
    def __init__(self, project_directory: str) -> None:
        self._project_directory = project_directory
        self._pdm = "~/.local/bin/pdm"

    def install(self) -> None:
        print(">>> Installing pdm...")
        subprocess.run(
            "curl -sSL https://pdm-project.org/install-pdm.py | python3 -",
            shell=True,
            check=True,
        )
        print(">>> pdm installed successfully")

    def install_python(self, version: str) -> None:
        command = f"{self._pdm} python install {version}"
        print(f">>> Installing Python {version}...")
        subprocess.run(
            command,
            shell=True,
            check=True,
            cwd=self._project_directory,
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

        command = f"{self._pdm} add {flag} {dependency_name}"
        subprocess.run(
            command,
            shell=True,
            check=True,
            cwd=self._project_directory,
        )

    @staticmethod
    def _generate_flag(add_to_group: bool, is_dev: bool) -> str:
        dev_flag = "--dev" if is_dev else ""
        group_flag = ""
        if add_to_group:
            group_name = FreeTextQuestion(
                key="group_name", message="Enter the name of the group"
            ).ask()["group_name"]
            group_flag += f"--group {group_name}"
        return f"{dev_flag} {group_flag}"

    def _create_virtual_environment(self) -> None:
        command = f"{self._pdm} install"
        subprocess.run(
            command,
            shell=True,
            check=True,
            cwd=self._project_directory,
            stdout=subprocess.DEVNULL,
        )
