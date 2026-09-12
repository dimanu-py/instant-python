import os
import sys
from pathlib import Path

from instant_python.version.domain.installation_method import InstallationMethod
from instant_python.version.domain.installation_method_detector import InstallationMethodDetector


class SystemInstallationMethodDetector(InstallationMethodDetector):
    _PIPX_RECEIPT_FILENAME = "pipx_metadata.json"
    _UV_RECEIPT_FILENAME = "uv-receipt.toml"

    def detect(self) -> InstallationMethod:
        if "PYAPP" in os.environ:
            return InstallationMethod.BINARY

        environment_root = Path(sys.prefix)
        if (environment_root / self._PIPX_RECEIPT_FILENAME).is_file():
            return InstallationMethod.PIPX
        if (environment_root / self._UV_RECEIPT_FILENAME).is_file():
            return InstallationMethod.UV
        return InstallationMethod.PIP
