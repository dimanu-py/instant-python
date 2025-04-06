from instant_python.question_prompter.template_types import TemplateTypes


def is_in(values: list[str], container: list) -> bool:
    return any(value in container for value in values)


def compute_base_path(initial_path: str, template_type: str) -> str:
    if template_type == TemplateTypes.DDD:
        return initial_path

    path_components = initial_path.split(".")
    if template_type == TemplateTypes.CLEAN:
        return ".".join(path_components[1:])
    elif template_type == TemplateTypes.STANDARD:
        return ".".join(path_components[2:])
    else:
        raise ValueError(f"Unknown template type: {template_type}")
