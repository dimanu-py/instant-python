from dataclasses import dataclass


@dataclass
class GeneralConfiguration:
    slug: str
    source_name: str
    description: str
    version: str
    author: str
    license: str
    python_version: str
    dependency_manager: str
