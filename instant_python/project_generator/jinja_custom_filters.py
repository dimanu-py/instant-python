def is_in(values: list[str], container: list) -> bool:
    return any(value in container for value in values)
