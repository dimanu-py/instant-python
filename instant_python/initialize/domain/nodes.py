class File:
    def __init__(self, name: str, extension: str, content: str | None = None) -> None:
        self._name = name
        self._extension = extension
        self._content = content

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name}, extension={self._extension})"

    def build_path_for(self, path: str) -> str:
        return f"{path}/{self._name}{self._extension}"
