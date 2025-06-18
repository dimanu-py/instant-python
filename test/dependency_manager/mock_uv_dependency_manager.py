from expects import expect, contain

from instant_python.dependency_manager.uv_dependency_manager import UvDependencyManager


class MockUvDependencyManager(UvDependencyManager):
    def __init__(self, project_directory: str) -> None:
        super().__init__(project_directory)
        self._commands = []

    def expect_to_have_been_called_with(self, command: str) -> None:
        expect(self._commands).to(contain(command))
