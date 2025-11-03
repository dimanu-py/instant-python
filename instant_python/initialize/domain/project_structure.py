from instant_python.initialize.domain.nodes import Node, NodeType, Directory, File
from instant_python.project_creator.unknown_node_typer_error import UnknownNodeTypeError


class ProjectStructure:
    def __init__(self, nodes: list[dict]) -> None:
        self._nodes = self._build_project_structure(nodes)

    def _build_project_structure(self, nodes: list[dict]) -> list[Node]:
        return [self._build_node(node) for node in nodes]

    def _build_node(self, node: dict) -> Node:
        node_type = node["type"]
        name = node["name"]

        if node_type == NodeType.DIRECTORY:
            children = node.get("children", [])
            is_python_module = node.get("python", False)
            directory_children = [self._build_node(child) for child in children]
            return Directory(name=name, is_python_module=is_python_module, children=directory_children)
        elif node_type == NodeType.FILE:
            extension = node.get("extension", "")
            content = node.get("content", None)
            return File(name=name, extension=extension, content=content)
        else:
            raise UnknownNodeTypeError(node_type)
