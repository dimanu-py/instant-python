import pytest
from doublex import Mimic, Mock, expect_call
from doublex_expects import have_been_satisfied
from expects import expect, raise_error

from instant_python.shared.infra.system_console import SystemConsole
from instant_python.version.domain.updater import LATEST_VERSION
from instant_python.version.infra import binary_updater as binary_updater_module
from instant_python.version.infra.binary_updater import BinaryUpdater, IpyBinaryNotFoundError


@pytest.mark.unit
class TestBinaryUpdater:
    def setup_method(self) -> None:
        self._console = Mimic(Mock, SystemConsole)
        self._binary_updater = BinaryUpdater(console=self._console)

    def test_should_run_self_update_when_upgrading_to_latest_version(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(binary_updater_module.shutil, "which", lambda _: "/home/user/.local/bin/ipy")
        expect_call(self._console).execute_or_raise('"/home/user/.local/bin/ipy" self update')

        self._binary_updater.update(LATEST_VERSION)

        expect(self._console).to(have_been_satisfied)

    def test_should_raise_error_when_binary_cannot_be_located(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(binary_updater_module.shutil, "which", lambda _: None)

        expect(lambda: self._binary_updater.update(LATEST_VERSION)).to(raise_error(IpyBinaryNotFoundError))

    def test_should_reinstall_pinned_version_using_shell_script_on_unix(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(binary_updater_module.platform, "system", lambda: "Linux")
        expect_call(self._console).execute_or_raise(
            "curl -LsSf https://raw.githubusercontent.com/dimanu-py/instant-python/main/scripts/install.sh"
            " | IPY_VERSION=1.2.3 sh"
        )

        self._binary_updater.update("1.2.3")

        expect(self._console).to(have_been_satisfied)

    def test_should_reinstall_pinned_version_using_powershell_script_on_windows(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(binary_updater_module.platform, "system", lambda: "Windows")
        expect_call(self._console).execute_or_raise(
            "powershell -ExecutionPolicy ByPass -c \"$env:IPY_VERSION='1.2.3'; "
            'irm https://raw.githubusercontent.com/dimanu-py/instant-python/main/scripts/install.ps1 | iex"'
        )

        self._binary_updater.update("1.2.3")

        expect(self._console).to(have_been_satisfied)
