import shutil
import tempfile

from expects import expect, equal

from instant_python.initialize.infra.env_manager.system_console import SystemConsole, CommandExecutionResult


class TestSystemCommandExecutor:
    def setup_method(self) -> None:
        self._temp_dir = tempfile.mkdtemp()
        self._console = SystemConsole(working_directory=self._temp_dir)

    def teardown_method(self) -> None:
        shutil.rmtree(self._temp_dir)

    def test_should_execute_command_successfully(self) -> None:
        result = self._console.execute("echo 'hello'")

        expected_result = CommandExecutionResult(
            exit_code=0,
            stdout="hello\n",
            stderr="",
        )
        expect(result).to(equal(expected_result))
