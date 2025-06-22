from dataclasses import dataclass, field, asdict

from instant_python.configuration.dependency.not_dev_dependency_included_in_group import (
    NotDevDependencyIncludedInGroup,
)


@dataclass
class DependencyConfiguration:
    name: str
    version: str
    is_dev: bool = field(default=False)
    group: str = field(default_factory=str)

    def __post_init__(self) -> None:
        self.version = str(self.version)
        self._ensure_dependency_is_dev_if_group_is_set()

    def to_primitives(self) -> dict[str, str | bool]:
        return asdict(self)

    def get_installation_flag(self) -> tuple[str, ...]:
        if self.group:
            return (f"--group {self.group}",)
        elif self.is_dev:
            return ("--dev",)
        return tuple()

    def get_specification(self) -> str:
        if self.version == "latest":
            return self.name
        return f"{self.name}=={self.version}"

    def _ensure_dependency_is_dev_if_group_is_set(self) -> None:
        if self.group and not self.is_dev:
            raise NotDevDependencyIncludedInGroup(self.name, self.group)
