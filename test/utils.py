from pathlib import Path


def resources_path() -> Path:
    return Path("test").resolve() / "resources"
