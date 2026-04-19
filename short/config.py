from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    hostname : str
    username: str
    name: str
    password: int
    port: str
    model_config={'env_file':".env"}


settings=Settings()
