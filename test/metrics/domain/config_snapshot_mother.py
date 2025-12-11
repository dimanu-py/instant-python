import random
from typing import Any

from instant_python.metrics.domain.config_snapshot import ConfigSnapshot
from instant_python.shared.supported_built_in_features import SupportedBuiltInFeatures
from instant_python.shared.supported_managers import SupportedManagers
from instant_python.shared.supported_python_versions import SupportedPythonVersions
from instant_python.shared.supported_templates import SupportedTemplates


class ConfigSnapshotMother:
    @staticmethod
    def any() -> Any:
        return ConfigSnapshot(
            python_version=random.choice(list(SupportedPythonVersions)),
            dependency_manager=random.choice(list(SupportedManagers)),
            template=random.choice(list(SupportedTemplates)),
            built_in_features=random.choices(list(SupportedBuiltInFeatures), k=3),
        )
