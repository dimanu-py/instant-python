{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
from test.{{ template_domain_import }}.random_generator import RandomGenerator


class IntPrimitivesMother:
	@staticmethod
	def any() -> int:
		return RandomGenerator.positive_integer()