from instant_python.config.domain.config_schema import ConfigSchema
from instant_python.initialize.domain.project_structure import ProjectStructure
from instant_python.initialize.domain.project_writer import ProjectWriter


class FileSystemProjectWriter(ProjectWriter):
    def write(self, project_structure: ProjectStructure, config: ConfigSchema, destination) -> None:
        raise NotImplementedError
