import tempfile
import uuid
from pathlib import Path

from expects import expect, be_a

from instant_python.metrics.infra.user_identity_manager import UserIdentityManager


class TestUserIdentityManager:
    def test_should_generate_new_id_when_identification_file_does_not_exist(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            config_dir = Path(temp_dir)
            user_identity_manager = UserIdentityManager(config_dir=config_dir)

            distinct_id = user_identity_manager.get_distinct_id()

            expect(distinct_id).to(be_a(str))
            expect(uuid.UUID(distinct_id)).to(be_a(uuid.UUID))
