from pathlib import Path


def test_resources_path() -> Path:
    return Path("test").resolve() / "resources"
