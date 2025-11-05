from instant_python.initialize.domain.project_formatter import ProjectFormatter
from instant_python.initialize.infra.env_manager.system_console import SystemConsole, CommandExecutionError


class RuffProjectFormatter(ProjectFormatter):
    def __init__(self, console: SystemConsole) -> None:
        self._console = console

    def format(self) -> None:
        result = self._console.execute(command="uvx ruff format")
        if not result.success():
            raise CommandExecutionError(
                exit_code=result.exit_code,
                stderr_output=result.stderr,
            )
