from instant_python.configuration.git.git_configuration import GitConfiguration


class GitConfigurer:
    def __init__(self, project_directory: str) -> None:
        self._project_directory = project_directory

    def setup_repository(self, configuration: GitConfiguration) -> None:
        if not configuration.initialize:
            return
