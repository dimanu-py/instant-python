from pathlib import Path

from instant_python.config.domain.config_schema import ConfigSchema
from instant_python.initialize.domain.nodes import Directory, File
from instant_python.initialize.domain.project_structure import ProjectStructure
from instant_python.initialize.domain.project_writer import ProjectWriter


class FileSystemProjectWriter(ProjectWriter):
    def write(self, project_structure: ProjectStructure, config: ConfigSchema, destination: Path) -> None:
        for node in project_structure:
            write_path = node.build_path_for(destination)
            if isinstance(node, Directory):
                write_path.mkdir(parents=True, exist_ok=True)
                if node._is_python_module:
                    init_file_path = write_path / "__init__.py"
                    init_file_path.touch(exist_ok=True)
            elif isinstance(node, File):
                write_path.touch(exist_ok=True)
