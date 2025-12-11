from pathlib import Path

from doublex import expect_call, Mock
from expects import expect, equal, be_false

from instant_python.metrics.application.config_snapshot_creator import ConfigSnapshotCreator
from instant_python.shared.domain.config_repository import ConfigRepository
from test.metrics.domain.config_snapshot_mother import ConfigSnapshotMother
from test.shared.domain.mothers.config_schema_mother import ConfigSchemaMother


class TestConfigSnapshotCreator:
    def setup_method(self) -> None:
        self._repository = Mock(ConfigRepository)
        self._config_snapshot_creator = ConfigSnapshotCreator()

    def test_should_create_snapshot_when_config_exists(self) -> None:
        snapshot = ConfigSnapshotMother.any()
        config_path = Path("ipy.yml")
        expect_call(self._repository).read(config_path).returns(ConfigSchemaMother.any())

        snapshot_taken = self._config_snapshot_creator.execute(config_path)

        expect(snapshot_taken.is_unknown()).to(be_false)
        expect(snapshot_taken).to(equal(snapshot))
