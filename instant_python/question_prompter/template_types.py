from enum import Enum


class TemplateTypes(str, Enum):
	DDD = "domain_driven_design"
	CLEAN = "clean_architecture"
	STANDARD = "standard_project"
