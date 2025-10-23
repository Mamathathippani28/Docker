# Iris Classification API (FastAPI + Docker)

This project demonstrates a **containerized machine learning inference service** built with **FastAPI**, **scikit-learn**, and **Docker**.  
It trains a logistic regression model on the **Iris dataset** and exposes a `/predict` endpoint for real-time predictions.

---

## Overview

The solution includes:
- A **training script** (`train.py`) that builds and serializes a `scikit-learn` model (`iris_model.pkl`)
- A **FastAPI application** (`main.py`) that loads the trained model and serves predictions
- A **Dockerfile** for reproducible, portable deployment
- **Swagger UI** at `/docs` for easy testing

---

## Project Structure

```
iris-api/
├── app/
│   └── main.py              # FastAPI app for inference
├── models/
│   └── iris_model.pkl       # Serialized ML model
├── train.py                 # Model training script
├── requirements.txt         # Dependencies
├── Dockerfile               # Container build instructions
└── README.md                # Project documentation
```

---

## Technology Stack

| Component | Technology |
|------------|-------------|
| Language | Python 3.11 |
| Framework | FastAPI 0.115.0 |
| ML Library | scikit-learn 1.4.2 |
| Serialization | pickle |
| Web Server | Uvicorn 0.30.6 |
| Containerization | Docker |

---

## Setup and Usage

### 1️⃣ Train the Model
If you want to regenerate the model locally:

```bash
python train.py
```

This creates a serialized model file at:
```
iris_model.pkl
```

### 2️⃣ Build the Docker Image

```bash
docker build -t iris-api .
```

### 3️⃣ Run the Container

```bash
docker run --rm -p 8000:8000 iris-api
```

The API will be available at:
```
http://localhost:8000
```

---

## 🔍 API Endpoints

| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/health` | GET | Health check endpoint |
| `/predict` | POST | Returns Iris flower prediction and class probabilities |

### Example Request
```bash
curl -X POST "http://localhost:8000/predict"   -H "Content-Type: application/json"   -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

### Example Response
```json
{
  "class_id": 0,
  "class_name": "setosa",
  "proba": [0.99, 0.01, 0.00]
}
```

### Interactive Swagger UI
Visit:
```
http://localhost:8000/docs
```

---

## Requirements

All dependencies are listed in `requirements.txt`:

```
fastapi==0.115.0
uvicorn==0.30.6
pydantic==2.8.2
numpy==1.26.4
scikit-learn==1.4.2
```

You can install them locally using:
```bash
pip install -r requirements.txt
```

---

## Dockerfile Summary

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ app/
COPY iris_model.pkl
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Testing

1. Run container
2. Send test request with any HTTP client:
   - `curl`
   - Postman
   - Swagger UI (`/docs`)

You should get class predictions for Iris flower species:
- `setosa`
- `versicolor`
- `virginica`

---

## Troubleshooting

| Issue | Cause | Solution |
|--------|--------|----------|
| `Model file not found` | `iris_model.pkl` missing | Run `train.py` or verify `models/` path |
| `TypeError: conlist() got an unexpected keyword argument 'min_items'` | Wrong Pydantic version | Ensure `pydantic>=2.0` |
| Port 8000 already in use | Another service running | Change port or stop other container |

---

## Reproducibility

The entire project (model, dependencies, and API) is fully reproducible through Docker.  
Rebuild anytime:
```bash
docker build --no-cache -t iris-api .
```
---

**Author:** Mamatha Thippani  
**Git:** [GitHub](https://github.com/Mamathathippani28)

