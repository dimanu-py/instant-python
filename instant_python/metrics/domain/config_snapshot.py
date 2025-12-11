class ConfigSnapshot:
    def __init__(self, python_version: str, dependency_manager: str, template: str, built_in_features: list[str]) -> None:
        self._python_version = python_version
        self._dependency_manager = dependency_manager
        self._template = template
        self._built_in_features = built_in_features
