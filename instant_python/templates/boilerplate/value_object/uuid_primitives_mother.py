from test{{ "shared.domain.random_generator" | resolve_import_path(template.name) }} import RandomGenerator


class UuidPrimitivesMother:
	@staticmethod
	def any() -> str:
		return RandomGenerator.uuid()

	@staticmethod
	def invalid() -> str:
		return "00000000-0000-0000-0000"