import sys
from pathlib import Path

import pytest
from expects import equal, expect

from instant_python.version.domain.installation_method import InstallationMethod
from instant_python.version.infra.system_installation_method_detector import SystemInstallationMethodDetector


@pytest.mark.unit
class TestSystemInstallationMethodDetector:
    def setup_method(self) -> None:
        self._detector = SystemInstallationMethodDetector()

    def test_should_detect_binary_installation_when_pyapp_env_var_is_set(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("PYAPP", "1")

        installation_method = self._detector.detect()

        expect(installation_method).to(equal(InstallationMethod.BINARY))

    def test_should_detect_binary_installation_when_pyapp_env_var_holds_its_own_location(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setenv("PYAPP", "/home/user/.local/share/pyapp/ipy")

        installation_method = self._detector.detect()

        expect(installation_method).to(equal(InstallationMethod.BINARY))

    def test_should_detect_pipx_installation_when_pipx_receipt_is_present(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
    ) -> None:
        monkeypatch.delenv("PYAPP", raising=False)
        monkeypatch.setattr(sys, "prefix", str(tmp_path))
        (tmp_path / "pipx_metadata.json").write_text("{}")

        installation_method = self._detector.detect()

        expect(installation_method).to(equal(InstallationMethod.PIPX))

    def test_should_detect_uv_installation_when_uv_receipt_is_present(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
    ) -> None:
        monkeypatch.delenv("PYAPP", raising=False)
        monkeypatch.setattr(sys, "prefix", str(tmp_path))
        (tmp_path / "uv-receipt.toml").write_text("")

        installation_method = self._detector.detect()

        expect(installation_method).to(equal(InstallationMethod.UV))

    def test_should_default_to_pip_installation_when_no_receipt_is_present(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
    ) -> None:
        monkeypatch.delenv("PYAPP", raising=False)
        monkeypatch.setattr(sys, "prefix", str(tmp_path))

        installation_method = self._detector.detect()

        expect(installation_method).to(equal(InstallationMethod.PIP))
