from instant_python.version.domain.installation_method import InstallationMethod
from instant_python.version.domain.installation_method_detector import InstallationMethodDetector
from instant_python.version.domain.updater_resolver import UpdaterResolver


class VersionUpdater:
    def __init__(self, detector: InstallationMethodDetector, updater_resolver: UpdaterResolver) -> None:
        self._detector = detector
        self._updater_resolver = updater_resolver

    def execute(self, version: str) -> InstallationMethod:
        installation_method = self._detect_installation_method()
        self._update_installed_version(installation_method, version)
        return installation_method

    def _update_installed_version(self, installation_method: InstallationMethod, version: str) -> None:
        updater = self._updater_resolver.resolve(installation_method)
        updater.update(version)

    def _detect_installation_method(self) -> InstallationMethod:
        return self._detector.detect()
