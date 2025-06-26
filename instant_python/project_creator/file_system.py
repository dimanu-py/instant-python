from pathlib import Path
from typing import Union

from instant_python.configuration.configuration_schema import ConfigurationSchema
from instant_python.project_creator.unknown_node_typer_error import UnknownNodeTypeError
from instant_python.project_creator.directory import Directory
from instant_python.project_creator.file import File
from instant_python.project_creator.node import Node, NodeType
from instant_python.render.jinja_environment import JinjaEnvironment


class FileSystem:
    def __init__(self, project_structure: list[dict[str, Union[list[str], str, bool]]]) -> None:
        self._boilerplate_files: list[File] = []
        self._tree: list[Node] = [self._build_node(node) for node in project_structure]

    def write_on_disk(self, file_renderer: JinjaEnvironment, context: ConfigurationSchema) -> None:
        project_path = Path(context.project_folder_name)
        for node in self._tree:
            node.create(base_path=project_path)

        for file in self._boilerplate_files:
            file.fill(renderer=file_renderer, context_config=context)

    def _build_node(self, node: dict[str, Union[str, list, bool]]) -> Node:
        node_type = node["type"]
        name = node["name"]

        if node_type == NodeType.DIRECTORY:
            children = node.get("children", [])
            is_python_module = node.get("python", False)
            directory_children = [self._build_node(child) for child in children]
            return Directory(name=name, children=directory_children, is_python=is_python_module)
        elif node_type == NodeType.BOILERPLATE:
            extension = node.get("extension", "")
            file = File(name=name, extension=extension)
            self._boilerplate_files.append(file)
            return file
        elif node_type == NodeType.FILE:
            extension = node.get("extension", "")
            return File(name=name, extension=extension)
        else:
            raise UnknownNodeTypeError(node_type)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(boilerplate_files={self._boilerplate_files}, tree={self._tree})"
