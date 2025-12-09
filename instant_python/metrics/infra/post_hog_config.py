from pydantic_settings import SettingsConfigDict, BaseSettings


class PostHogConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_prefix="POST_HOG_")
    api_key: str = ""
    host: str = ""
