import pickle
from pathlib import Path
from typing import List, Literal, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, conlist

IrisFeatureVector = conlist(float, min_length=4, max_length=4)

class PredictRequest(BaseModel):
    features: IrisFeatureVector = Field(
        ...,
        description="Iris features in order: [sepal_length, sepal_width, petal_length, petal_width]"
    )

class BatchPredictRequest(BaseModel):
    batch: List[IrisFeatureVector]

class PredictResponse(BaseModel):
    class_id: int
    class_name: Literal["setosa", "versicolor", "virginica"]
    proba: Optional[List[float]] = None

class BatchPredictResponse(BaseModel):
    results: List[PredictResponse]

app = FastAPI(title="Iris Classifier API", version="1.0.0")

MODEL_PATH = Path("iris_model.pkl")
CLASS_MAP = {0: "setosa", 1: "versicolor", 2: "virginica"}

def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH.resolve()}. "
                                f"Run `python train.py` first.")
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    try:
        X = [req.features]
        proba = model.predict_proba(X)[0].tolist()
        cls = int(max(range(len(proba)), key=lambda i: proba[i]))
        return PredictResponse(class_id=cls, class_name=CLASS_MAP[cls], proba=proba)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


