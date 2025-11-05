import subprocess

from instant_python.config.domain.git_config import GitConfig
from instant_python.initialize.domain.version_control_configurer import VersionControlConfigurer
from instant_python.initialize.infra.env_manager.system_console import (
    SystemConsole,
    CommandExecutionResult,
    CommandExecutionError,
)


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
        result = self._console.execute(command="git init")
        self._raise_command_execution_error(result=result)

    def _set_user_information(self, username: str, email: str) -> None:
        result_name = self._console.execute(command=f"git config user.name {username}")
        self._raise_command_execution_error(result=result_name)

        result_email = self._console.execute(command=f"git config user.email {email}")
        self._raise_command_execution_error(result=result_email)

    def _make_initial_commit(self) -> None:
        result_add = self._console.execute(command="git add .")
        self._raise_command_execution_error(result=result_add)

        result_commit = self._console.execute(command='git commit -m "🎉 chore: initial commit"')
        self._raise_command_execution_error(result=result_commit)

    @staticmethod
    def _raise_command_execution_error(result: CommandExecutionResult) -> None:
        if not result.success():
            raise CommandExecutionError(exit_code=result.exit_code, stderr_output=result.stderr)

    def _run_command(self, command: str) -> None:
        subprocess.run(
            command,
            shell=True,
            check=True,
            cwd=self._project_directory,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        )
