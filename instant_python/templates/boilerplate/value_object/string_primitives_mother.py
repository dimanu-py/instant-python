{% set template_domain_import = "shared.domain"|compute_base_path(template.name) %}
{% if template_domain_import %}
from test.{{ template_domain_import }}.random_generator import RandomGenerator
{% else %}
from test.random_generator import RandomGenerator
{% endif %}


class StringPrimitivesMother:
	@staticmethod
	def any() -> str:
		return RandomGenerator.word()