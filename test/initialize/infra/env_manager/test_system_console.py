import shutil
import tempfile

from expects import expect, be_true, be_false, equal, contain

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

    def test_should_capture_failing_command(self) -> None:
        result = self._console.execute("ls /nonexistent_directory_xyz")

        expect(result.success()).to(be_false)

    def test_should_capture_output_error(self) -> None:
        result = self._console.execute("ls /nonexistent_directory_xyz")

        expect(result.stderr).to(contain("cannot access '/nonexistent_directory_xyz'"))

    def test_should_return_non_zero_exit_code_on_error(self) -> None:
        result = self._console.execute("ls /nonexistent_directory_xyz")

        expect(result.exit_code).to_not(equal(0))



