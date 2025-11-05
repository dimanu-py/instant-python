from instant_python.initialize.domain.project_formatter import ProjectFormatter
from instant_python.initialize.infra.env_manager.system_console import SystemConsole


class RuffProjectFormatter(ProjectFormatter):
    def __init__(self, console: SystemConsole) -> None:
        self._console = console

    def format(self) -> None:
        self._console.execute_or_raise(command="uvx ruff format")
