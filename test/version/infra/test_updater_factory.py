import pytest
from expects import be_a, expect

from instant_python.shared.infra.system_console import SystemConsole
from instant_python.version.domain.installation_method import InstallationMethod
from instant_python.version.infra.binary_updater import BinaryUpdater
from instant_python.version.infra.pip_updater import PipUpdater
from instant_python.version.infra.pipx_updater import PipxUpdater
from instant_python.version.infra.updater_factory import UpdaterFactory
from instant_python.version.infra.uv_updater import UvUpdater


@pytest.mark.unit
class TestUpdaterFactory:
    def setup_method(self) -> None:
        self._updater_factory = UpdaterFactory(console=SystemConsole(working_directory="."))

    @pytest.mark.parametrize(
        ("installation_method", "expected_updater_type"),
        [
            pytest.param(InstallationMethod.BINARY, BinaryUpdater, id="binary"),
            pytest.param(InstallationMethod.PIPX, PipxUpdater, id="pipx"),
            pytest.param(InstallationMethod.UV, UvUpdater, id="uv"),
            pytest.param(InstallationMethod.PIP, PipUpdater, id="pip"),
        ],
    )
    def test_should_resolve_the_updater_matching_the_installation_method(
        self, installation_method: InstallationMethod, expected_updater_type: type
    ) -> None:
        updater = self._updater_factory.resolve(installation_method)

        expect(updater).to(be_a(expected_updater_type))
