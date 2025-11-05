from instant_python.initialize.infra.env_manager.system_console import CommandExecutionResult
from test.random_generator import RandomGenerator


class CommandExecutionResultMother:
    _EMPTY_OUTPUT = ""
    _SUCCESS_EXIT_CODE = 0
    _FAILED_EXIT_CODE = 1

    @classmethod
    def success(cls) -> CommandExecutionResult:
        return CommandExecutionResult(
            exit_code=cls._SUCCESS_EXIT_CODE,
            stdout=RandomGenerator.word(),
            stderr=cls._EMPTY_OUTPUT,
        )

    @classmethod
    def failure(cls) -> CommandExecutionResult:
        return CommandExecutionResult(
            exit_code=cls._FAILED_EXIT_CODE,
            stdout=cls._EMPTY_OUTPUT,
            stderr=RandomGenerator.word(),
        )
