from typing import Callable, Any


def validate(func: Callable[..., Any]) -> Callable[..., Any]:
	"""Mark a method as a validator for ValueObject validation."""
	setattr(func, "_is_validator", True)
	return func
