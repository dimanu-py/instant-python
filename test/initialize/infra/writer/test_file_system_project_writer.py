import json
import tempfile
from pathlib import Path

from approvaltests import verify

from instant_python.initialize.infra.writer.file_system_project_writer import FileSystemProjectWriter
from test.config.domain.mothers.config_schema_mother import ConfigSchemaMother
from test.initialize.domain.mothers.project_structure_mother import ProjectStructureMother


class TestFileSystemProjectWriter:
    def test_should_create_python_module_in_file_system(self) -> None:
        project_structure = ProjectStructureMother.with_one_directory()
        config = ConfigSchemaMother.any()
        writer = FileSystemProjectWriter()

        with tempfile.TemporaryDirectory() as project_dir:
            project_location_path = Path(project_dir)
            writer.write(project_structure, config, project_location_path)
            created_structure = self._read_folder_structure(Path(project_location_path))

        verify(json.dumps(created_structure, indent=2))

    def _read_folder_structure(self, path: Path) -> dict:
        raise NotImplementedError

