import shutil
import tempfile

from expects import expect, be_true

from instant_python.initialize.infra.env_manager.system_console import SystemConsole


class TestSystemCommandExecutor:
    def setup_method(self) -> None:
        self._temp_dir = tempfile.mkdtemp()
        self._console = SystemConsole(working_directory=self._temp_dir)

    def teardown_method(self) -> None:
        shutil.rmtree(self._temp_dir)

    def test_should_execute_command_successfully(self) -> None:
        result = self._console.execute("echo 'hello'")

        expect(result.success()).to(be_true)
