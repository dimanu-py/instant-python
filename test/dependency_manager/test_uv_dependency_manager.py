import os

from expects import expect, raise_error

from instant_python.configuration.dependency.dependency_configuration import DependencyConfiguration
from instant_python.dependency_manager.command_execution_error import CommandExecutionError
from test.dependency_manager.mock_uv_dependency_manager import MockUvDependencyManager, MockUvDependencyManagerWithError


class TestUvDependencyManager:
    def setup_method(self) -> None:
        self._uv_dependency_manager = MockUvDependencyManager(project_directory=os.getcwd())

    def test_should_install_uv(self) -> None:
        self._uv_dependency_manager._install()

        self._uv_dependency_manager.expect_to_have_been_called_with("curl -LsSf https://astral.sh/uv/install.sh | sh")

    def test_should_install_specific_pyton_version(self) -> None:
        python_version = "3.12"

        self._uv_dependency_manager._install_python(version=f"{python_version}")

        self._uv_dependency_manager.expect_to_have_been_called_with(f"~/.local/bin/uv python install {python_version}")

    def test_should_install_dependencies(self) -> None:
        dependencies = [
            DependencyConfiguration(
                name="pytest",
                version="latest",
                is_dev=True,
                group="test",
            ),
            DependencyConfiguration(
                name="requests",
                version="2.32.0",
            ),
            DependencyConfiguration(
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
        uv_dependency_manager = MockUvDependencyManagerWithError(project_directory=os.getcwd())

        expect(lambda: uv_dependency_manager.setup_environment(python_version="3.12", dependencies=[])).to(
            raise_error(CommandExecutionError)
        )
