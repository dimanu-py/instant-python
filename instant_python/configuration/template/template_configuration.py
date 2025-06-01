from dataclasses import dataclass, field, asdict

from instant_python.configuration.template.bounded_context_not_applicable import BoundedContextNotApplicable
from instant_python.configuration.template.bounded_context_not_especified import (
    BoundedContextNotSpecified,
)
from instant_python.configuration.template.constants import (
    SUPPORTED_TEMPLATES,
    SUPPORTED_BUILT_IN_FEATURES,
)
from instant_python.configuration.template.invalid_built_in_features_values import (
    InvalidBuiltInFeaturesValues,
)
from instant_python.configuration.template.invalid_template_value import (
    InvalidTemplateValue,
)


@dataclass
class TemplateConfiguration:
    name: str
    built_in_features: list[str] = field(default_factory=list)
    specify_bounded_context: bool = field(default=False)
    bounded_context: str | None = field(default=None)
    aggregate_name: str | None = field(default=None)

    def __post_init__(self) -> None:
        self._ensure_template_is_supported()
        self._ensure_built_in_features_are_supported()
        self._ensure_bounded_context_is_only_applicable_for_ddd_template()
        self._ensure_bounded_context_is_set_if_specified()

    def _ensure_template_is_supported(self) -> None:
        if self.name not in SUPPORTED_TEMPLATES:
            raise InvalidTemplateValue(self.name, SUPPORTED_TEMPLATES)

    def _ensure_built_in_features_are_supported(self) -> None:
        unsupported_features = [
            feature
            for feature in self.built_in_features
            if feature not in SUPPORTED_BUILT_IN_FEATURES
        ]
        if unsupported_features:
            raise InvalidBuiltInFeaturesValues(unsupported_features, SUPPORTED_BUILT_IN_FEATURES)

    def _ensure_bounded_context_is_only_applicable_for_ddd_template(self) -> None:
        if self.specify_bounded_context and self.name != "domain_driven_design":
            raise BoundedContextNotApplicable(self.name)

    def _ensure_bounded_context_is_set_if_specified(self) -> None:
        if self.specify_bounded_context and (
            not self.bounded_context or not self.aggregate_name
        ):
            raise BoundedContextNotSpecified()

    def to_primitives(self) -> dict[str, str | list[str]]:
        return asdict(self)
