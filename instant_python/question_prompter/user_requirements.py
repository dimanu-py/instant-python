from dataclasses import dataclass, asdict, field
from datetime import datetime
from typing import Self

import yaml


@dataclass
class UserRequirements:
    project_slug: str
    source_name: str
    license: str
    version: str
    description: str
    author: str
    python_version: str
    dependency_manager: str
    template: str
    git_email: str = field(default=None)
    git_user_name: str = field(default=None)
    dependencies: list[str] = field(default_factory=list)
    bounded_context: str = field(default=None)
    aggregate_name: str = field(default=None)
    git: bool = field(default=False)
    built_in_features: list[str] = field(default_factory=list)
    year: int = field(default=datetime.now().year)

    def __post_init__(self) -> None:
        self._file_path = "user_requirements.yml"

    def to_dict(self) -> dict:
        return asdict(self)

    def save_in_memory(self) -> None:
        with open(self._file_path, "w") as file:
            yaml.dump(self.to_dict(), file)
