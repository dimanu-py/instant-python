import tempfile
from pathlib import Path

from instant_python.project_generator.node import Node, NodeType
from instant_python.project_generator.python_file import PythonFile
from instant_python.project_generator.python_module import PythonModule


class FolderTree:
    def create(self, project_structure: dict) -> None:
        tree = [self._build_tree(node) for node in project_structure.get("root", [])]
        temporary_directory = Path(tempfile.mkdtemp())
        for node in tree:
            node.create(base_path=temporary_directory)

    def _build_tree(self, node: dict) -> Node:
        node_type = node.get("type")
        name = node.get("name")
        children = node.get("children", [])

        if node_type == NodeType.PYTHON_MODULE:
            module_children = [self._build_tree(child) for child in children]
            return PythonModule(name=name, children=module_children)
        elif node_type == NodeType.PYTHON_FILE:
            return PythonFile(name=name)
        else:
            raise ValueError(f"Invalid node type: {node_type}")
