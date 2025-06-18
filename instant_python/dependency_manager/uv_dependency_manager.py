class UvDependencyManager:
    def __init__(self, project_directory: str) -> None:
        self._project_directory = project_directory

    def _install(self) -> None:
        raise NotImplementedError
