class ConfigSnapshot:
    _UNKNOWN = "unknown"

    def __init__(
        self, python_version: str, dependency_manager: str, template: str, built_in_features: list[str]
    ) -> None:
        self._python_version = python_version
        self._dependency_manager = dependency_manager
        self._template = template
        self._built_in_features = built_in_features

    def is_unknown(self) -> bool:
        return all(
            value == self._UNKNOWN or value == []
            for value in [self._python_version, self._dependency_manager, self._template, self._built_in_features]
        )
