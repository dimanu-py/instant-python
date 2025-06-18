import os

from test.dependency_manager.mock_uv_dependency_manager import MockUvDependencyManager


class TestUvDependencyManager:
    def setup_method(self) -> None:
        self._uv_dependency_manager = MockUvDependencyManager(project_directory=os.getcwd())

    def test_should_install_uv(self) -> None:
        self._uv_dependency_manager._install()

        self._uv_dependency_manager.expect_to_have_been_called_with(command="curl -LsSf https://astral.sh/uv/install.sh | sh")

    def test_should_install_specific_pyton_version(self) -> None:
        python_version = "3.12"

        self._uv_dependency_manager._install_python(version=f"{python_version}")

        self._uv_dependency_manager.expect_to_have_been_called_with(command=f"~/.local/bin/uv python install {python_version}")
