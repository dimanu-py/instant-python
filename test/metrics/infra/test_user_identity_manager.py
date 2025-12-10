import json
import tempfile
import uuid
from pathlib import Path

from expects import expect, be_a, equal, be_true, have_keys

from instant_python.metrics.infra.user_identity_manager import UserIdentityManager


class TestUserIdentityManager:
    def test_should_generate_new_id_when_identification_file_does_not_exist(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            config_dir = Path(temp_dir)
            user_identity_manager = UserIdentityManager(config_dir=config_dir)

            distinct_id = user_identity_manager.get_distinct_id()

            expect(distinct_id).to(be_a(str))
            expect(uuid.UUID(distinct_id)).to(be_a(uuid.UUID))

    def test_should_create_metrics_file_and_store_distinct_id_for_new_user(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            config_dir = Path(temp_dir)
            metrics_file = config_dir / "metrics.json"
            user_identity_manager = UserIdentityManager(config_dir=config_dir)

            distinct_id = user_identity_manager.get_distinct_id()

            expect(metrics_file.exists()).to(be_true)
            stored_distinct_id = json.loads(metrics_file.read_text())
            expect(stored_distinct_id).to(have_keys("distinct_id"))
            expect(stored_distinct_id["distinct_id"]).to(equal(distinct_id))

    def test_should_return_same_id_on_consecutive_calls(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            config_dir = Path(temp_dir)
            user_identity_manager = UserIdentityManager(config_dir=config_dir)

            first_id = user_identity_manager.get_distinct_id()
            second_id = user_identity_manager.get_distinct_id()

            expect(first_id).to(equal(second_id))

    def test_should_regenerate_id_when_metrics_file_is_invalid(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            config_dir = Path(temp_dir)
            metrics_file = config_dir / "metrics.json"
            metrics_file.write_text("invalid json content")

            user_identity_manager = UserIdentityManager(config_dir=config_dir)
            distinct_id = user_identity_manager.get_distinct_id()

            expect(distinct_id).to(be_a(str))
            expect(uuid.UUID(distinct_id)).to(be_a(uuid.UUID))
            stored_data = json.loads(metrics_file.read_text())
            expect(stored_data["distinct_id"]).to(equal(distinct_id))

