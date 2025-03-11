import subprocess


class GitConfigurer:
    def __init__(self, project_directory: str) -> None:
        self._project_directory = project_directory

    def configure(self, email: str, username: str) -> None:
        self._initialize_repository()

        if email and username:
            self._set_user_information(email, username)

        self._initial_commit()

    def _initialize_repository(self) -> None:
        print(">>> Initializing git repository...")
        subprocess.run(
            "git init",
            shell=True,
            check=True,
            cwd=self._project_directory,
            stdout=subprocess.DEVNULL,
        )
        print(">>> Git repository initialized successfully")

    def _set_user_information(self, email: str | None, username: str | None) -> None:
        print(">>> Configuring git user and email...")
        subprocess.run(
            f"git config user.name {username} && git config user.email {email}",
            shell=True,
            check=True,
            cwd=self._project_directory,
            stdout=subprocess.DEVNULL,
        )
        print(">>> Git user and email configured successfully")

    def _initial_commit(self) -> None:
        print(">>> Making initial commit...")
        subprocess.run(
	        "git add . && git commit -m '🎉 chore: initial commit'",
	        shell=True,
	        check=True,
	        cwd=self._project_directory,
            stdout=subprocess.DEVNULL,
        )
        print(">>> Initial commit made successfully")
