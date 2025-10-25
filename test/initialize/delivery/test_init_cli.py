import json
import tempfile
from pathlib import Path

import yaml
from approvaltests import verify_all_combinations
from typer.testing import CliRunner

from instant_python.initialize.delivery.cli import app
from instant_python.shared.supported_licenses import SupportedLicenses
from instant_python.shared.supported_managers import SupportedManagers
from instant_python.shared.supported_python_versions import SupportedPythonVersions
from instant_python.shared.supported_templates import SupportedTemplates


class TestInitCli:
    def setup_method(self) -> None:
        self._runner = CliRunner()

    def test_initializes_project_structure(self) -> None:
        dependency_managers = SupportedManagers.get_supported_managers()
        licenses = SupportedLicenses.get_supported_licenses()
        python_versions = SupportedPythonVersions.get_supported_versions()
        create_git_repository = [True, False]
        templates = SupportedTemplates.get_supported_templates()

        verify_all_combinations(
            self._run_cli_with_config,
            [
                dependency_managers,
                licenses,
                python_versions,
                create_git_repository,
                templates,
            ],
        )

    def _run_cli_with_config(
        self,
        dependency_manager: str,
        license_type: str,
        python_version: str,
        initialize_git: bool,
        template: str,
    ) -> dict:
        config = self._create_config_with_parameters(
            dependency_manager=dependency_manager,
            license_type=license_type,
            python_version=python_version,
            initialize_git=initialize_git,
            template=template,
        )

        with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as config_file:
            yaml.dump(config, config_file)
            config_file_path = config_file.name

        with self._runner.isolated_filesystem():
            result = self._runner.invoke(app, ["--config", str(config_file_path)])

        return {
            "exit_code": result.exit_code,
            "errors": result.exception,
            "config": {
                "dependency_manager": dependency_manager,
                "license": license_type,
                "python_version": python_version,
                "initialize_git": initialize_git,
                "template": template,
            },
        }

    def _create_config_with_parameters(
        self,
        dependency_manager: str,
        license_type: str,
        python_version: str,
        initialize_git: bool,
        template: str,
    ) -> dict:
        config = json.loads(json.dumps(self._read_base_config()))

        config["general"]["dependency_manager"] = dependency_manager
        config["general"]["license"] = license_type
        config["general"]["python_version"] = python_version

        config["git"]["initialize"] = initialize_git

        config["template"]["name"] = template

        return config

    @staticmethod
    def _read_base_config() -> dict:
        config_path = Path(__file__).parent / "ipy.yml"
        with config_path.open("r") as file:
            return yaml.safe_load(file)
