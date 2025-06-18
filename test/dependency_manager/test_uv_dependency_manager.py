import os

from test.dependency_manager.mock_uv_dependency_manager import MockUvDependencyManager


class TestUvDependencyManager:
    def test_should_install_uv(self) -> None:
        project_directory = os.getcwd()
        uv_dependency_manager = MockUvDependencyManager(project_directory=project_directory)

        uv_dependency_manager._install()

        uv_dependency_manager.expect_to_have_been_called_with(command="curl -LsSf https://astral.sh/uv/install.sh | sh")
