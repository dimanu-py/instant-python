from pathlib import Path

from instant_python.project_generator.directory import Directory
from instant_python.project_generator.file import File
from instant_python.project_generator.node import Node, NodeType


class UnknownNodeType(ValueError):
    def __init__(self, node_type: str) -> None:
        self._message = f"Unknown node type: {node_type}"
        super().__init__(self._message)


class FolderTree:
    def __init__(self, project_directory: str) -> None:
        self._project_directory = Path(project_directory)

    def create(self, project_structure: dict) -> None:
        tree = [self._build_tree(node) for node in project_structure.get("root", [])]
        for node in tree:
            node.create(base_path=self._project_directory)

    @property
    def project_directory(self) -> str:
        return str(self._project_directory)

    def _build_tree(self, node: dict) -> Node:
        node_type = node.get("type")
        name = node.get("name")

        if node_type == NodeType.DIRECTORY:
            children = node.get("children", [])
            is_python_module = node.get("python", False)
            directory_children = [self._build_tree(child) for child in children]
            return Directory(name=name, children=directory_children, python_module=is_python_module)
        elif node_type == NodeType.FILE:
            extension = node.get("extension", "")
            return File(name=name, extension=extension)
        else:
            raise UnknownNodeType(node_type)
