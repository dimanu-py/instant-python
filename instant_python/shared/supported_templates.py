from enum import Enum


class SupportedTemplates(str, Enum):
    DDD = "domain_driven_design"
    CLEAN = "clean_architecture"
    STANDARD = "standard_project"
    CUSTOM = "custom"

    @classmethod
    def get_supported_templates(cls) -> list[str]:
        return [template.value for template in cls]
