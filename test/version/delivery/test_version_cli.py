import re

import pytest
from expects import contain, expect
from typer.testing import CliRunner

from instant_python import __version__
from instant_python.version.delivery.cli import app

_ANSI_ESCAPE_PATTERN = re.compile(r"\x1b\[[0-9;]*m")


def _strip_ansi(text: str) -> str:
    return _ANSI_ESCAPE_PATTERN.sub("", text)


@pytest.mark.acceptance
class TestVersionCli:
    def setup_method(self) -> None:
        self._runner = CliRunner()

    def test_should_show_installed_version(self) -> None:
        result = self._runner.invoke(app, ["version"])

        expect(result.output).to(contain(__version__))

    def test_should_expose_update_command_with_version_option(self) -> None:
        result = self._runner.invoke(app, ["update", "--help"])

        expect(_strip_ansi(result.output)).to(contain("--version"))
