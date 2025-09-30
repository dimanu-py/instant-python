{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
{% if template_domain_import %}
from test.{{ template_domain_import }}.random_generator import RandomGenerator
{% else %}
from test.random_generator import RandomGenerator
{% endif %}


class UuidPrimitivesMother:
	@staticmethod
	def any() -> str:
		return RandomGenerator.uuid()

	@staticmethod
	def invalid() -> str:
		return "00000000-0000-0000-0000"