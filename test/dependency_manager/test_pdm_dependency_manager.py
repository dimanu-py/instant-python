import os

from expects import expect, raise_error

from instant_python.configuration.dependency.dependency_configuration import DependencyConfiguration
from instant_python.dependency_manager.command_execution_error import CommandExecutionError
from test.dependency_manager.mock_pdm_dependency_manager import (
    MockPdmDependencyManagerWithError,
    MockPdmDependencyManager,
)


class TestPdmDependencyManager:
    def setup_method(self) -> None:
        self._pdm_dependency_manager = MockPdmDependencyManager(project_directory=os.getcwd())

    def test_should_install_pdm(self) -> None:
        self._pdm_dependency_manager._install()

        self._pdm_dependency_manager.expect_to_have_been_called_with(
            "curl -sSL https://pdm-project.org/install-pdm.py | python3 -"
        )

    def test_should_install_specific_pyton_version(self) -> None:
        python_version = "3.12"

        self._pdm_dependency_manager._install_python(version=f"{python_version}")

        self._pdm_dependency_manager.expect_to_have_been_called_with(
            f"~/.local/bin/pdm python install {python_version}"
        )

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
        ]

        self._pdm_dependency_manager._install_dependencies(dependencies=dependencies)

        self._pdm_dependency_manager.expect_to_have_been_called_with(
            "~/.local/bin/pdm install",
            "~/.local/bin/pdm add --group test pytest",
            "~/.local/bin/pdm add requests==2.32.0",
        )

    def test_should_raise_error_when_command_fails(self) -> None:
        pdm_dependency_manager = MockPdmDependencyManagerWithError(project_directory=os.getcwd())

        expect(lambda: pdm_dependency_manager.setup_environment(python_version="3.12", dependencies=[])).to(
            raise_error(CommandExecutionError)
        )
