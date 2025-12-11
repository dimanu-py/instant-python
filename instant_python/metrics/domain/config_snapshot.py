from typing import TypedDict


class ConfigSnapshotPrimitives(TypedDict):
    python_version: str
    dependency_manager: str
    template_type: str
    built_in_features: list[str]


class ConfigSnapshot:
    _UNKNOWN = "unknown"

    def __init__(
        self, python_version: str, dependency_manager: str, template: str, built_in_features: list[str]
    ) -> None:
        self._python_version = python_version
        self._dependency_manager = dependency_manager
        self._template = template
        self._built_in_features = built_in_features

    @classmethod
    def unknown(cls) -> "ConfigSnapshot":
        return cls(
            python_version=cls._UNKNOWN,
            dependency_manager=cls._UNKNOWN,
            template=cls._UNKNOWN,
            built_in_features=[],
        )

    def is_unknown(self) -> bool:
        return all(
            value == self._UNKNOWN or value == []
            for value in [self._python_version, self._dependency_manager, self._template, self._built_in_features]
        )

    def to_primitives(self) -> ConfigSnapshotPrimitives:
        return ConfigSnapshotPrimitives(
            python_version=self._python_version,
            dependency_manager=self._dependency_manager,
            template_type=self._template,
            built_in_features=self._built_in_features,
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ConfigSnapshot):
            return NotImplemented
        return (
            self._python_version == other._python_version
            and self._dependency_manager == other._dependency_manager
            and self._template == other._template
            and self._built_in_features == other._built_in_features
        )

    def __repr__(self) -> str:
        return (
            f"ConfigSnapshot(python_version={self._python_version}, "
            f"dependency_manager={self._dependency_manager}, "
            f"template={self._template}, "
            f"built_in_features={self._built_in_features})"
        )