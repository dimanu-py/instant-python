from dataclasses import dataclass, asdict, field

import yaml


@dataclass
class UserRequirements:
    project_name: str
    slug: str
    source_name: str
    license: str
    version: str
    description: str
    github_username: str
    github_email: str
    python_version: str
    dependency_manager: str
    python_manager: str
    default_dependencies: bool
    template: str
    bounded_context: str = field(default=None)
    aggregate_name: str = field(default=None)
    common_ddd_objects: bool = field(default=False)

    def to_dict(self) -> dict:
        return asdict(self)

    def save_in_memory(self):
        with open("user_requirements.yml", "w") as file:
            yaml.dump(self.to_dict(), file)
