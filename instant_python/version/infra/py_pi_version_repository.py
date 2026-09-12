from instant_python.version.domain.latest_version import LatestVersion
from instant_python.version.domain.latest_version_repository import LatestVersionRepository
from instant_python.version.infra.urllib_http_client import UrllibHttpClient


class PyPiLatestLatestVersionRepository(LatestVersionRepository):
    _PYPI_URL = "https://pypi.org/pypi/instant-python/json"

    def __init__(self, client: UrllibHttpClient) -> None:
        self._client = client

    def get_latest_version(self) -> LatestVersion:
        latest_version = self._client.request(self._PYPI_URL)
        return LatestVersion(latest_version) if latest_version else LatestVersion.unknown()
