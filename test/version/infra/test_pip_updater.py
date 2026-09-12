import sys

import pytest
from doublex import Mimic, Mock, expect_call
from doublex_expects import have_been_satisfied
from expects import expect

from instant_python.shared.infra.system_console import SystemConsole
from instant_python.version.domain.updater import LATEST_VERSION
from instant_python.version.infra.pip_updater import PipUpdater


@pytest.mark.unit
class TestPipUpdater:
    def setup_method(self) -> None:
        self._console = Mimic(Mock, SystemConsole)
        self._pip_updater = PipUpdater(console=self._console)

    def test_should_upgrade_to_latest_version(self) -> None:
        expect_call(self._console).execute_or_raise(f'"{sys.executable}" -m pip install --upgrade instant-python')

        self._pip_updater.update(LATEST_VERSION)

        expect(self._console).to(have_been_satisfied)

    def test_should_install_pinned_version_when_version_given(self) -> None:
        expect_call(self._console).execute_or_raise(f'"{sys.executable}" -m pip install instant-python==1.2.3')

        self._pip_updater.update("1.2.3")

        expect(self._console).to(have_been_satisfied)
