from dataclasses import dataclass, asdict, field
from datetime import datetime
from typing import Self

import yaml


@dataclass
class UserRequirements:
    project_name: str
    project_slug: str
    source_name: str
    license: str
    version: str
    description: str
    author: str
    email: str
    python_version: str
    dependency_manager: str
    python_manager: str
    default_dependencies: bool
    template: str
    bounded_context: str = field(default=None)
    aggregate_name: str = field(default=None)
    git: bool = field(default=False)
    built_in_features: list[str] = field(default_factory=list)
    year: int = field(default=datetime.now().year)

    def to_dict(self) -> dict:
        return asdict(self)

    def save_in_memory(self) -> None:
        with open("user_requirements.yml", "w") as file:
            yaml.dump(self.to_dict(), file)

    @classmethod
    def load_from_file(cls) -> Self:
        with open("user_requirements.yml") as file:
            return cls(**yaml.safe_load(file))
