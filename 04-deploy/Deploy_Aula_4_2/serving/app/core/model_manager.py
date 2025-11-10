import logging
from pathlib import Path
from typing import Any, Dict

import joblib
import mlflow
import mlflow.sklearn
import numpy as np
from app.core.config import settings

logger = logging.getLogger("ml_serving")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
MODEL_CACHE_DIR = BASE_DIR / "model_cache"
MODEL_CACHE_DIR.mkdir(exist_ok=True, parents=True)


class ModelLoadError(Exception):
    """Custom exception for model loading errors"""

    pass


class ModelManager:
    def __init__(self):
        self._model = None
        self._encoder = None
        self._model_info = None
        self._loading = False

        print("MLFLOW_TRACKING_URI: ", settings.MLFLOW_TRACKING_URI)

        mlflow.set_tracking_uri(settings.MLFLOW_TRACKING_URI)
        mlflow.set_registry_uri(settings.MLFLOW_TRACKING_URI)

    @property
    def model_info(self):
        """Get current model information"""
        return self._model_info

    def load_model(self, model_name: str, model_version_alias: str) -> None:
        """Load the ML model from MLflow model registry

        Args:
            model_name: Name of the model in MLflow registry
            model_version_alias: Version or alias of the model (e.g. 'production', 'staging', '1')
        """
        # Check if we're already loading
        if self._loading:
            logger.warning("Model load already in progress")
            return

        self._loading = True
        import time

        start_time = time.time()

        try:
            logger.info(
                f"Starting model load from MLflow registry: {model_name}@{model_version_alias}"
            )

            model_uri = f"models:/{model_name}@{model_version_alias}"
            model_cache_path = MODEL_CACHE_DIR / model_name / model_version_alias
            mlflow_model_path = model_cache_path / "MLmodel"

            if mlflow_model_path.exists():
                logger.info(f"Found model in local cache at: {model_cache_path}")
                try:
                    self._model = mlflow.sklearn.load_model(str(model_cache_path))
                    logger.info("Successfully loaded model from local cache")
                except Exception as cache_error:
                    logger.warning(
                        f"Failed to load from cache: {cache_error}. Will download from MLflow."
                    )
                    model_cache_path.mkdir(exist_ok=True, parents=True)
                    self._model = mlflow.sklearn.load_model(
                        model_uri, dst_path=str(model_cache_path)
                    )
            else:
                logger.info(
                    f"Model not found in cache. Downloading from MLflow... Path: {model_cache_path}"
                )
                model_cache_path.mkdir(exist_ok=True, parents=True)
                self._model = mlflow.sklearn.load_model(
                    model_uri, dst_path=str(model_cache_path)
                )

            self._model_info = {
                "name": model_name,
                "version": model_version_alias,
                "uri": model_uri,
            }

            load_time = time.time() - start_time
            logger.info(
                f"Model loaded successfully in {load_time:.2f} seconds from {model_uri}"
            )

        except mlflow.exceptions.MlflowException as e:
            load_time = time.time() - start_time
            logger.error(
                f"MLflow error loading model after {load_time:.2f} seconds: {str(e)}"
            )
            raise ModelLoadError(f"MLflow error: {str(e)}")
        except Exception as e:
            load_time = time.time() - start_time
            logger.error(
                f"Unexpected error loading model after {load_time:.2f} seconds: {str(e)}"
            )
            raise ModelLoadError(f"Unexpected error: {str(e)}")
        finally:
            self._encoder = joblib.load(BASE_DIR / "encoder.joblib")
            self._loading = False

    def predict(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Make predictions using the loaded model."""
        if self._model is None:
            raise RuntimeError("Model not loaded. Please load the model first.")

        try:
            # Convert input data to the format expected by the model
            features = self._preprocess_input(data)

            # Make prediction
            prediction = self._model.predict(features)

            # Format the prediction response
            result = self._format_prediction(prediction)

            return result
        except Exception as e:
            logger.error(f"Error making prediction: {str(e)}")
            raise

    def _preprocess_input(self, data: Dict[str, Any]) -> np.ndarray:
        """Preprocess the input data before making predictions."""
        try:
            import pandas as pd

            df = pd.DataFrame([data])
            features = self._encoder.transform(df)
            return features
        except Exception as e:
            logger.error(f"Error in preprocessing: {str(e)}, Input data: {data}")
            raise ValueError(f"Preprocessing error: {str(e)}")

    def _format_prediction(self, prediction: np.ndarray) -> Dict[str, Any]:
        """Format the prediction output."""
        return {"prediction": prediction.tolist()[0], "status": "success"}

    @property
    def model(self):
        return self._model

    @property
    def is_loaded(self) -> bool:
        return self._model is not None


model_manager = ModelManager()
