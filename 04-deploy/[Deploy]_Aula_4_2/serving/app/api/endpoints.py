from app.core.model_manager import model_manager
from app.models.schemas import HealthResponse, PredictionInput, PredictionResponse
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
async def predict(data: PredictionInput):
    print(data)
    """Make predictions using the loaded model."""
    try:
        if not model_manager.is_loaded:
            raise HTTPException(status_code=503, detail="Model not loaded")

        result = model_manager.predict(data.features)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/health", response_model=HealthResponse)
async def health():
    """Check the health status of the service."""
    return {"status": "healthy", "model_loaded": model_manager.is_loaded}
