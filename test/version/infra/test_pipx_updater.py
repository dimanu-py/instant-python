import pytest
from doublex import Mimic, Mock, expect_call
from doublex_expects import have_been_satisfied
from expects import expect

from instant_python.shared.infra.system_console import SystemConsole
from instant_python.version.domain.updater import LATEST_VERSION
from instant_python.version.infra.pipx_updater import PipxUpdater


@pytest.mark.unit
class TestPipxUpdater:
    def setup_method(self) -> None:
        self._console = Mimic(Mock, SystemConsole)
        self._pipx_updater = PipxUpdater(console=self._console)

    def test_should_upgrade_to_latest_version(self) -> None:
        expect_call(self._console).execute_or_raise("pipx upgrade instant-python")

        self._pipx_updater.update(LATEST_VERSION)

        expect(self._console).to(have_been_satisfied)

    def test_should_install_pinned_version_when_version_given(self) -> None:
        expect_call(self._console).execute_or_raise("pipx install instant-python==1.2.3 --force")

        self._pipx_updater.update("1.2.3")

        expect(self._console).to(have_been_satisfied)
