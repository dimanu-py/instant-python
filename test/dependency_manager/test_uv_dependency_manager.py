import os

from test.dependency_manager.mock_uv_dependency_manager import MockUvDependencyManager


class TestUvDependencyManager:
    def test_should_install_uv(self) -> None:
        project_directory = os.getcwd()
        uv_dependency_manager = MockUvDependencyManager(project_directory=project_directory)

        uv_dependency_manager._install()

        uv_dependency_manager.expect_to_have_been_called_with(command="curl -LsSf https://astral.sh/uv/install.sh | sh")

    def test_should_install_specific_pyton_version(self) -> None:
        project_directory = os.getcwd()
        uv_dependency_manager = MockUvDependencyManager(project_directory=project_directory)
        python_version = "3.12"

        uv_dependency_manager._install_python(version=f"{python_version}")

        uv_dependency_manager.expect_to_have_been_called_with(command=f"~/.local/bin/uv python install {python_version}")
