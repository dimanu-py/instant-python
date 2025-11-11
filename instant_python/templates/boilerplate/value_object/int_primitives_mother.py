from test{{ "shared.domain.random_generator" | resolve_import_path(template.name) }} import RandomGenerator


class IntPrimitivesMother:
	@staticmethod
	def any() -> int:
		return RandomGenerator.positive_integer()