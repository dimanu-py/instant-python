import subprocess

from instant_python.config.domain.git_config import GitConfig
from instant_python.initialize.domain.version_control_configurer import VersionControlConfigurer
from instant_python.initialize.infra.env_manager.system_console import SystemConsole


class GitConfigurer(VersionControlConfigurer):
    def __init__(self, project_directory: str, console: SystemConsole | None = None) -> None:
        self._console = console
        self._project_directory = project_directory

    def setup(self, config: GitConfig) -> None:
        print(">>> Setting up git repository...")
        self._initialize_repository()
        self._set_user_information(
            username=config.username,
            email=config.email,
        )
        self._make_initial_commit()
        print(">>> Git repository created successfully")

    def _initialize_repository(self) -> None:
        self._run_command(command="git init")

    def _set_user_information(self, username: str, email: str) -> None:
        self._run_command(command=f"git config user.name {username}")
        self._run_command(command=f"git config user.email {email}")

    def _make_initial_commit(self) -> None:
        self._run_command(command="git add .")
        self._run_command(command='git commit -m "🎉 chore: initial commit"')

    def _run_command(self, command: str) -> None:
        subprocess.run(
            command,
            shell=True,
            check=True,
            cwd=self._project_directory,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        )
