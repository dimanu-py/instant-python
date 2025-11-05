from instant_python.initialize.domain.env_manager import CommandExecutionError
from instant_python.initialize.infra.env_manager.system_console import SystemConsole


class RuffProjectFormatter:
    def __init__(self, console: SystemConsole | None = None) -> None:
        self._console = console

    def format(self) -> None:
        result = self._console.execute(command="uvx ruff format")
        if not result.success():
            raise CommandExecutionError(
                exit_code=result.exit_code,
                stderr_output=result.stderr,
            )
