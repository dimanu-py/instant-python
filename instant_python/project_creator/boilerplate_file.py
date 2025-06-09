from pathlib import Path

from instant_python.project_creator.node import Node


class BoilerplateFile(Node):
    def __init__(self, name: str, extension: str) -> None:
        self._file_name = f"{name.split('/')[-1]}{extension}"

    def create(self, base_path: Path) -> None:
        raise NotImplementedError
