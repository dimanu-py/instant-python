{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
from test.{{ template_domain_import }}.random_generator import RandomGenerator


class StringPrimitivesMother:
	@staticmethod
	def any() -> str:
		return RandomGenerator.word()