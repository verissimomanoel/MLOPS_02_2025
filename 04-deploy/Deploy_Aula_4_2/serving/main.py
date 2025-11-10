import logging

import uvicorn
from app.api.endpoints import router
from app.core.config import settings
from app.core.model_manager import model_manager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pythonjsonlogger import jsonlogger

logger = logging.getLogger("ml_serving")
if not logger.handlers:
    logHandler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter()
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)
    logger.setLevel(logging.INFO)

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix=settings.API_V1_STR)

@app.on_event("startup")
async def startup_event():
    """Load the ML model on startup if model name and version are configured."""
    if settings.MODEL_NAME and settings.MODEL_VERSION_ALIAS:
        try:
            model_manager.load_model(
                model_name=settings.MODEL_NAME,
                model_version_alias=settings.MODEL_VERSION_ALIAS,
            )
            logger.info(
                f"Model {settings.MODEL_NAME}@{settings.MODEL_VERSION_ALIAS} loaded successfully on startup"
            )
        except Exception as e:
            logger.error(f"Failed to load model on startup: {str(e)}")
    else:
        logger.warning(
            "MODEL_NAME or MODEL_VERSION_ALIAS not set in configuration; skipping model load on startup"
        )


def main():
    """Run the API server."""
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="info")


if __name__ == "__main__":
    main()
