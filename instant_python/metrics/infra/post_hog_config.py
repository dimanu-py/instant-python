from pydantic import Field

from pydantic_settings import SettingsConfigDict, BaseSettings


class PostHogConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_prefix="POST_HOG_")
    api_key: str = ""
    host: str = ""
    metrics_enabled: bool = Field(
        default=True,
        alias="IPY_METRICS_ENABLE",
    )

    def is_metrics_disabled(self) -> bool:
        return not self.metrics_enabled
