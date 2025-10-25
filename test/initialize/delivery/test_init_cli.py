import json
import tempfile
from pathlib import Path

import yaml
from approvaltests import verify_all_combinations
from typer.testing import CliRunner

from instant_python.dependency_manager.dependency_manager import DependencyManager
from instant_python.initialize.delivery.cli import app
from instant_python.shared.supported_built_in_features import SupportedBuiltInFeatures
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
        templates = SupportedTemplates.get_supported_templates()
        built_in_templates = SupportedBuiltInFeatures.get_supported_built_in_features()
        source_folders = ["src", "app"]
        init_git_repository = [True, False]
        git_usernames = ["", "johndoe"]
        git_emails = ["", "johndoe@gmail.com"]
        specify_bounded_context = [True, False]
        bounded_context_names = ["", "backoffice"]
        aggregate_names = ["", "customer"]

        verify_all_combinations(
            self._run_cli_with_config,
            [
                dependency_managers,
                licenses,
                python_versions,
                source_folders,
                init_git_repository,
                git_usernames,
                git_emails,
                templates,
                specify_bounded_context,
                bounded_context_names,
                aggregate_names,
                built_in_templates,
            ],
        )

    def _run_cli_with_config(
        self,
        dependency_manager: str,
        license_type: str,
        python_version: str,
        source_name: str,
        git_initialize: bool,
        git_username: str,
        git_email: str,
        template_name: str,
        specify_bounded_context: bool,
        bounded_context_name: str,
        aggregate_name: str,
        built_in_features: list[str],
    ) -> dict:
        config = self._create_config_with_parameters(
            dependency_manager=dependency_manager,
            license_type=license_type,
            python_version=python_version,
            source_name=source_name,
            git_initialize=git_initialize,
            git_username=git_username,
            git_email=git_email,
            template_name=template_name,
            specify_bounded_context=specify_bounded_context,
            bounded_context_name=bounded_context_name,
            aggregate_name=aggregate_name,
            built_in_features=built_in_features,
        )

        with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as config_file:
            yaml.dump(config, config_file)
            config_file_path = config_file.name

        try:
            with self._runner.isolated_filesystem():
                result = self._runner.invoke(app, ["--config", config_file_path])

            return {
                "exit_code": result.exit_code,
                "output": result.output,
                "config": {
                    "dependency_manager": dependency_manager,
                    "license": license_type,
                    "python_version": python_version,
                    "source_name": source_name,
                    "git_initialize": git_initialize,
                    "template_name": template_name,
                    "specify_bounded_context": specify_bounded_context,
                    "built_in_features": built_in_features,
                },
            }
        finally:
            Path(config_file_path).unlink()

    def _create_config_with_parameters(
        self,
        dependency_manager: str,
        license_type: str,
        python_version: str,
        source_name: str,
        git_initialize: bool,
        git_username: str,
        git_email: str,
        template_name: str,
        specify_bounded_context: bool,
        bounded_context_name: str,
        aggregate_name: str,
        built_in_features: list[str],
    ) -> dict:
        config = json.loads(json.dumps(_read_base_config()))

        config["general"]["dependency_manager"] = dependency_manager
        config["general"]["license"] = license_type
        config["general"]["python_version"] = python_version
        config["general"]["source_name"] = source_name
        config["git"]["initialize"] = git_initialize
        config["git"]["username"] = git_username
        config["git"]["email"] = git_email
        config["template"]["name"] = template_name
        config["template"]["specify_bounded_context"] = specify_bounded_context
        config["template"]["bounded_context_name"] = bounded_context_name
        config["template"]["aggregate_name"] = aggregate_name
        config["template"]["built_in_features"] = built_in_features

        return config


def _read_base_config() -> dict:
    config_path = Path(__file__).parent / "ipy.yml"
    with config_path.open("r") as file:
        return yaml.safe_load(file)
