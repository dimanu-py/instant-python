{% if general.python_version in ["3.13", "3.12", "3.11"] %}
from enum import StrEnum


class ExchangeType(StrEnum):
{% else %}
from enum import Enum


class ExchangeType(str, Enum):
{% endif %}
    TOPIC = "topic"
    DIRECT = "direct"
    FANOUT = "fanout"
