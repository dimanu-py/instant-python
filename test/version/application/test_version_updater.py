import pytest
from doublex import Mock, expect_call
from doublex_expects import have_been_satisfied
from expects import equal, expect

from instant_python.version.application.version_updater import VersionUpdater
from instant_python.version.domain.installation_method import InstallationMethod
from instant_python.version.domain.installation_method_detector import InstallationMethodDetector
from instant_python.version.domain.updater import Updater
from instant_python.version.domain.updater_resolver import UpdaterResolver


@pytest.mark.unit
class TestVersionUpdater:
    _ANY_VERSION = "1.2.3"
    _LATEST_VERSION = "latest"

    def setup_method(self) -> None:
        self._detector = Mock(InstallationMethodDetector)
        self._updater_resolver = Mock(UpdaterResolver)
        self._updater = Mock(Updater)
        self._version_updater = VersionUpdater(detector=self._detector, updater_resolver=self._updater_resolver)

    def test_should_forward_latest_version_to_the_resolved_updater(self) -> None:
        expect_call(self._detector).detect().returns(InstallationMethod.PIP)
        expect_call(self._updater_resolver).resolve(InstallationMethod.PIP).returns(self._updater)
        expect_call(self._updater).update(self._LATEST_VERSION)

        self._version_updater.execute(self._LATEST_VERSION)

        expect(self._updater).to(have_been_satisfied)

    def test_should_forward_the_requested_version_to_the_resolved_updater(self) -> None:
        expect_call(self._detector).detect().returns(InstallationMethod.BINARY)
        expect_call(self._updater_resolver).resolve(InstallationMethod.BINARY).returns(self._updater)
        expect_call(self._updater).update(self._ANY_VERSION)

        self._version_updater.execute(self._ANY_VERSION)

        expect(self._updater).to(have_been_satisfied)

    def test_should_return_the_detected_installation_method(self) -> None:
        expect_call(self._detector).detect().returns(InstallationMethod.PIP)
        expect_call(self._updater_resolver).resolve(InstallationMethod.PIP).returns(self._updater)
        expect_call(self._updater).update(self._ANY_VERSION)

        installation_method = self._version_updater.execute(self._ANY_VERSION)

        expect(installation_method).to(equal(InstallationMethod.PIP))
