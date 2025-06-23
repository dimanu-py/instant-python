from instant_python.git.git_configurer import GitConfigurer


class MockGitConfigurer(GitConfigurer):
    def __init__(self, project_directory: str) -> None:
        super().__init__(project_directory=project_directory)
