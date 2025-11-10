from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "ML Model Serving API"
    MODEL_NAME: Optional[str] = None
    MODEL_VERSION_ALIAS: Optional[str] = None
    MLFLOW_TRACKING_URI: str = "http://host.docker.internal:8080"

    class Config:
        case_sensitive = True


settings = Settings()
