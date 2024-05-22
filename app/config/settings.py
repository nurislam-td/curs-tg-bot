from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore", env_file='.env', case_sensitive=False)
    bot_token: str
    db_user: str
    db_password: str
    db_host: str
    db_name: str
    db_port: int
    mode: str

    @property
    def db_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.db_user}:"
            f"{self.db_password}@{self.db_host}:"
            f"{self.db_port}/{self.db_name}"
        )


settings = Settings()
