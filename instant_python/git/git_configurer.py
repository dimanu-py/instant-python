import subprocess

from instant_python.configuration.git.git_configuration import GitConfiguration


class GitConfigurer:
    def __init__(self, project_directory: str) -> None:
        self._project_directory = project_directory

    def setup_repository(self, configuration: GitConfiguration) -> None:
        if not configuration.initialize:
            return

        print(">>> Setting up git repository...")
        self._initialize_repository()
        self._set_user_information(
            username=configuration.username,
            email=configuration.email,
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
