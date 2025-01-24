from pathlib import Path
from typing import Set

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    tg_bot_token: str = "string"
    tg_users_whitelist: Set[str] = set()

    api_sandbox_token: str = "string"
    api_live_token: str = "string"

    project_root: Path = Path(__file__).parent.resolve()

    model_config = SettingsConfigDict(env_file=".env", extra="allow")


settings = Settings()
