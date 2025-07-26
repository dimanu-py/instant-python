from pathlib import Path

from typer.testing import CliRunner

from instant_python.commands.init import app


class TestInitCommand:
    def setup_method(self) -> None:
        self._runner = CliRunner()

    def test_init_creates_project_structure(self) -> None:
        with self._runner.isolated_filesystem():
            result = self._runner.invoke(app, ["--config", f"{Path(__file__).parent / 'ipy.yml'}"])

        expected_lines = [
            ">>> Installing uv...",
            ">>> uv installed successfully",
            ">>> Installing Python 3.10...",
            ">>> Python 3.10 installed successfully",
            ">>> Installing dependencies...",
            ">>> Dependencies installed successfully",
        ]

        actual_lines = result.output.strip().split("\n")
        assert len(actual_lines) == len(expected_lines), f"Expected {len(expected_lines)} lines, got {len(actual_lines)}"

        for i, (expected, actual) in enumerate(zip(expected_lines, actual_lines)):
            assert actual == expected, f"Line {i+1} mismatch: expected '{expected}', got '{actual}'"
