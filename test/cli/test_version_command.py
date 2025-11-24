import pytest
from typer.testing import CliRunner

from instant_python.cli.cli import app


@pytest.mark.acceptance
class TestVersionCommand:
    def setup_method(self) -> None:
        self._runner = CliRunner()

    def test_should_display_version_with_long_flag(self) -> None:
        result = self._runner.invoke(app, ["--version"])

        assert result.exit_code == 0
        assert "instant-python" in result.stdout.lower()

    def test_should_display_version_with_short_flag(self) -> None:
        result = self._runner.invoke(app, ["-V"])

        assert result.exit_code == 0
        assert "instant-python" in result.stdout.lower()

    def test_should_display_version_before_executing_other_commands_and_should_not_execute_extra_command(self) -> None:
        result = self._runner.invoke(app, ["--version", "init"])

        assert result.exit_code == 0
        assert "instant-python" in result.stdout.lower()
