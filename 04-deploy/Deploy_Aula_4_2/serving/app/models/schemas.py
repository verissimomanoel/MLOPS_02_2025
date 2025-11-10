from typing import Any, Dict

from pydantic import BaseModel, Field


class PredictionInput(BaseModel):
    features: Dict[str, Any] = Field(..., description="Input features for prediction")


class PredictionResponse(BaseModel):
    prediction: Any
    status: str


class HealthResponse(BaseModel):
    status: str
    model_loaded: bool
