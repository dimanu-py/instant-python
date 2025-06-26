from pathlib import Path

from expects import expect, equal, be_true, raise_error

from instant_python.configuration.parser.parser import Parser
from instant_python.project_creator.file import File
from instant_python.project_creator.file_has_not_been_created import FileHasNotBeenCreated
from instant_python.render.jinja_environment import JinjaEnvironment


class TestFile:
    def setup_method(self) -> None:
        self._file = File(name="exceptions/domain_error_simple", extension=".py")

    def teardown_method(self) -> None:
        file_path = Path(__file__).parent / "domain_error_simple.py"

        if file_path.exists():
            file_path.unlink()

    def test_should_extract_file_name(self) -> None:
        expect(self._file._file_name).to(equal("domain_error_simple.py"))

    def test_should_create_file_at_specified_path(self) -> None:
        self._file.create(base_path=Path(__file__).parent)

        file_path = Path(__file__).parent / "domain_error_simple.py"
        expect(file_path.exists()).to(be_true)

    def test_should_fill_file_with_template_content(self) -> None:
        self._file.create(base_path=Path(__file__).parent)
        renderer = JinjaEnvironment(package_name="test", template_directory="project_creator/resources")
        config = Parser.parse_from_file(str(Path(__file__).parent / "resources" / "config.yml"))

        self._file.fill(
            renderer=renderer,
            context_config=config,
        )

        file_path = Path(__file__).parent / "domain_error_simple.py"
        expect(file_path.read_text()).to(equal("class DomainError(Exception):\n    pass"))

    def test_should_not_be_able_to_fill_file_if_does_not_exist(self) -> None:
        renderer = JinjaEnvironment(package_name="test", template_directory="project_creator/resources")
        config = Parser.parse_from_file(str(Path(__file__).parent / "resources" / "config.yml"))

        expect(
            lambda: self._file.fill(
                renderer=renderer,
                context_config=config,
            )
        ).to(raise_error(FileHasNotBeenCreated))
