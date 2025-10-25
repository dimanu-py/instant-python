import json
import tempfile
from pathlib import Path

import yaml
from approvaltests import verify_all_combinations
from typer.testing import CliRunner

from instant_python.initialize.delivery.cli import app
from instant_python.shared.supported_built_in_features import SupportedBuiltInFeatures
from instant_python.shared.supported_licenses import SupportedLicenses
from instant_python.shared.supported_managers import SupportedManagers
from instant_python.shared.supported_python_versions import SupportedPythonVersions
from instant_python.shared.supported_templates import SupportedTemplates


class TestInitCli:
    def setup_method(self) -> None:
        self._runner = CliRunner()

    def test_initializes_project_with_general_section_combinations(self) -> None:
        dependency_managers = SupportedManagers.get_supported_managers()
        licenses = SupportedLicenses.get_supported_licenses()
        python_versions = SupportedPythonVersions.get_supported_versions()

        verify_all_combinations(
            self._run_cli_with_general_config,
            [
                dependency_managers,
                licenses,
                python_versions,
            ],
        )

    def test_initializes_project_with_git_section_combinations(self) -> None:
        create_git_repository = [True, False]

        verify_all_combinations(
            self._run_cli_with_git_config,
            [
                create_git_repository,
            ],
        )

    def test_initializes_project_with_template_section_combinations(self) -> None:
        templates = SupportedTemplates.get_supported_templates()
        built_in_features = SupportedBuiltInFeatures.get_supported_built_in_features()

        verify_all_combinations(
            self._run_cli_with_template_config,
            [
                templates,
                built_in_features,
            ],
        )

    def _run_cli_with_general_config(
        self,
        dependency_manager: str,
        license_type: str,
        python_version: str,
    ) -> dict:
        config = self._create_general_config(
            dependency_manager=dependency_manager,
            license_type=license_type,
            python_version=python_version,
        )

        return self._run_cli_with_config(config)

    def _run_cli_with_git_config(
        self,
        initialize_git: bool,
    ) -> dict:
        config = self._create_git_config(
            initialize_git=initialize_git,
        )

        return self._run_cli_with_config(config)

    def _run_cli_with_template_config(
        self,
        template: str,
        built_in_feature: str,
    ) -> dict:
        config = self._create_template_config(
            template=template,
            built_in_feature=built_in_feature,
        )

        return self._run_cli_with_config(config)

    def _run_cli_with_config(self, config: dict) -> dict:
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as config_file:
            yaml.dump(config, config_file)
            config_file_path = config_file.name

        with self._runner.isolated_filesystem():
            result = self._runner.invoke(app, ["--config", str(config_file_path)])

        return {
            "exit_code": result.exit_code,
            "errors": result.exception,
        }

    def _create_general_config(
        self,
        dependency_manager: str,
        license_type: str,
        python_version: str,
    ) -> dict:
        config = json.loads(json.dumps(self._read_base_config()))

        config["general"]["dependency_manager"] = dependency_manager
        config["general"]["license"] = license_type
        config["general"]["python_version"] = python_version

        return config

    def _create_git_config(
        self,
        initialize_git: bool,
    ) -> dict:
        config = json.loads(json.dumps(self._read_base_config()))

        config["git"]["initialize"] = initialize_git

        return config

    def _create_template_config(
        self,
        template: str,
        built_in_feature: str,
    ) -> dict:
        config = json.loads(json.dumps(self._read_base_config()))

        config["template"]["name"] = template
        config["template"]["built_in_features"] = [built_in_feature]

        return config

    @staticmethod
    def _read_base_config() -> dict:
        config_path = Path(__file__).parent / "ipy.yml"
        with config_path.open("r") as file:
            return yaml.safe_load(file)
