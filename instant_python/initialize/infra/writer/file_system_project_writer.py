from pathlib import Path

from instant_python.config.domain.config_schema import ConfigSchema
from instant_python.initialize.domain.nodes import Directory, File
from instant_python.initialize.domain.project_structure import ProjectStructure
from instant_python.initialize.domain.project_writer import ProjectWriter, NodeWriter


class FileSystemNodeWriter(NodeWriter):
    def create_directory(self, path: Path) -> None:
        pass

    def create_file(self, path: Path, content: str | None = None) -> None:
        pass


class FileSystemProjectWriter(ProjectWriter):
    def __init__(self) -> None:
        self._node_writer = FileSystemNodeWriter()

    def write(self, project_structure: ProjectStructure, config: ConfigSchema, destination: Path) -> None:
        for node in project_structure:
            write_path = node._build_path_for(destination)
            if isinstance(node, Directory):
                write_path.mkdir(parents=True, exist_ok=True)
                if node._is_python_module:
                    init_file_path = write_path / "__init__.py"
                    init_file_path.touch(exist_ok=True)
            elif isinstance(node, File):
                write_path.touch(exist_ok=True)
