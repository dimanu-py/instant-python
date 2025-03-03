import tempfile
from pathlib import Path

from src.project_generator.directory import Directory
from src.project_generator.node import Node, NodeType
from src.project_generator.file import File


class UnknownNodeType(ValueError):
    def __init__(self, node_type: str) -> None:
        self._message = f"Unknown node type: {node_type}"
        super().__init__(self._message)


class FolderTree:
    def create(self, project_structure: dict) -> None:
        tree = [self._build_tree(node) for node in project_structure.get("root", [])]
        temporary_directory = Path(tempfile.mkdtemp())
        for node in tree:
            node.create(base_path=temporary_directory)

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
