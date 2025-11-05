import os

from doublex import Mock, Mimic, expect_call
from doublex_expects import have_been_satisfied
from expects import expect, raise_error

from instant_python.config.domain.dependency_config import DependencyConfig
from instant_python.initialize.domain.env_manager import CommandExecutionError
from instant_python.initialize.infra.env_manager.system_console import SystemConsole
from instant_python.initialize.infra.env_manager.uv_env_manager import UvEnvManager
from test.initialize.infra.env_manager.mock_uv_env_manager import MockUvEnvManager, MockUvEnvManagerWithError
from test.initialize.infra.env_manager.mother.command_execution_result_mother import CommandExecutionResultMother


class TestUvEnvManager:
    _UV_EXECUTABLE = "~/.local/bin/uv"
    _SUCCESSFUL_COMMAND_RESULT = CommandExecutionResultMother.success()
    _FAILED_COMMAND_RESULT = CommandExecutionResultMother.failure()

    def setup_method(self) -> None:
        self._uv_dependency_manager = MockUvEnvManager(project_directory=os.getcwd())
        self._console = Mimic(Mock, SystemConsole)
        self._uv_env_manager = UvEnvManager(project_directory=os.getcwd(), console=self._console)

    def test_should_setup_environment_without_installing_uv_when_is_already_installed(self) -> None:
        python_version = "3.12"

        expect_call(self._console).execute(f"{self._UV_EXECUTABLE} --version").returns(self._SUCCESSFUL_COMMAND_RESULT)
        expect_call(self._console).execute(f"{self._UV_EXECUTABLE} python install {python_version}").returns(
            self._SUCCESSFUL_COMMAND_RESULT
        )
        expect_call(self._console).execute(f"{self._UV_EXECUTABLE} sync").returns(self._SUCCESSFUL_COMMAND_RESULT)

        self._uv_env_manager.setup(python_version=python_version, dependencies=[])

        expect(self._console).to(have_been_satisfied)

    def test_should_install_uv(self) -> None:
        self._uv_dependency_manager._install()

        self._uv_dependency_manager.expect_to_have_been_called_with("curl -LsSf https://astral.sh/uv/install.sh | sh")

    def test_should_install_specific_pyton_version(self) -> None:
        python_version = "3.12"

        self._uv_dependency_manager._install_python(version=f"{python_version}")

        self._uv_dependency_manager.expect_to_have_been_called_with(f"~/.local/bin/uv python install {python_version}")

    def test_should_install_dependencies(self) -> None:
        dependencies = [
            DependencyConfig(
                name="pytest",
                version="latest",
                is_dev=True,
                group="test",
            ),
            DependencyConfig(
                name="requests",
                version="2.32.0",
            ),
            DependencyConfig(
                name="mypy",
                version="latest",
                is_dev=True,
            ),
        ]

        self._uv_dependency_manager._install_dependencies(dependencies=dependencies)

        self._uv_dependency_manager.expect_to_have_been_called_with(
            "~/.local/bin/uv sync",
            "~/.local/bin/uv add --group test pytest",
            "~/.local/bin/uv add requests==2.32.0",
            "~/.local/bin/uv add --dev mypy",
        )

    def test_should_raise_error_when_command_fails(self) -> None:
        uv_dependency_manager = MockUvEnvManagerWithError(project_directory=os.getcwd())

        expect(lambda: uv_dependency_manager.setup(python_version="3.12", dependencies=[])).to(
            raise_error(CommandExecutionError)
        )
