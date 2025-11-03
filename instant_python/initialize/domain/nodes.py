class File:
    def __init__(self, name: str, extension: str, content: str | None = None) -> None:
        self._name = name
        self._extension = extension
        self._content = content

    def build_path_for(self, path: str) -> str:
        return f"{path}/{self._name}{self._extension}"
