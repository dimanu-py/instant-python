from test{{ "shared.domain.random_generator" | resolve_import_path(template.name) }} import RandomGenerator


class StringPrimitivesMother:
	@staticmethod
	def any() -> str:
		return RandomGenerator.word()