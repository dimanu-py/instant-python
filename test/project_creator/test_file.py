from pathlib import Path

from instant_python.configuration.parser.parser import Parser
from instant_python.project_creator.file import File
from instant_python.render.jinja_environment import JinjaEnvironment


class TestFile:
    def setup_method(self) -> None:
        self._file = File(name="exceptions/domain_error", extension=".py")

    def teardown_method(self) -> None:
        file_path = Path(__file__).parent / "domain_error.py"

        if file_path.exists():
            file_path.unlink()

    def test_should_extract_file_name(self) -> None:
        assert self._file._file_name == "domain_error.py"

    def test_should_create_file_at_specified_path(self) -> None:
        self._file.create(base_path=Path(__file__).parent)

        file_path = Path(__file__).parent / "domain_error.py"
        assert file_path.exists()

    def test_should_fill_file_with_template_content(self) -> None:
        self._file.create(base_path=Path(__file__).parent)
        renderer = JinjaEnvironment(package_name="test", template_directory="project_creator/resources")
        config = Parser.parse(str(Path(__file__).parent / "resources" / "config.yml"))

        self._file.fill(
            renderer=renderer,
            context_config=config,
        )

        file_path = Path(__file__).parent / "domain_error.py"
        assert file_path.read_text() == "class DomainError(Exception):\n    pass\n"
