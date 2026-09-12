import pytest
from expects import contain, expect
from typer.testing import CliRunner

from instant_python.version.delivery.cli import app


@pytest.mark.acceptance
class TestUpdateCli:
    def setup_method(self) -> None:
        self._runner = CliRunner()

    def test_should_expose_update_command_with_version_option(self) -> None:
        result = self._runner.invoke(app, ["update", "--help"])

        expect(result.output).to(contain("--version"))
