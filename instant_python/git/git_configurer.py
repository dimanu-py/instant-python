import subprocess

from instant_python.configuration.git.git_configuration import GitConfiguration


class GitConfigurer:
    def __init__(self, project_directory: str) -> None:
        self._project_directory = project_directory

    def setup_repository(self, configuration: GitConfiguration) -> None:
        if not configuration.initialize:
            return

        self._initialize_repository()
        self._set_user_information(
            username=configuration.username,
            email=configuration.email,
        )

    def _initialize_repository(self) -> None:
        print(">>> Initializing git repository...")
        self._run_command(command="git init")
        print(">>> Git repository initialized successfully")

    def _set_user_information(self, username: str, email: str) -> None:
        self._run_command(command=f"git config user.name {username}")
        self._run_command(command=f"git config user.email {email}")

    def _run_command(self, command: str) -> None:
        subprocess.run(
            command,
            shell=True,
            check=True,
            cwd=self._project_directory,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        )
