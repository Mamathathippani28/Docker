# train.py
import pickle
from pathlib import Path
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_and_save(model_path: str = "models/iris_model.pkl"):
    X, y = load_iris(return_X_y=True)

    # simple pipeline: scale -> logistic regression
    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=1000, multi_class="auto"))
    ])

    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    pipe.fit(X_tr, y_tr)

    acc = accuracy_score(y_te, pipe.predict(X_te))
    print(f"Validation accuracy: {acc:.4f}")

    Path("models").mkdir(parents=True, exist_ok=True)
    with open(model_path, "wb") as f:
        pickle.dump(pipe, f)
    print(f"Saved model to {model_path}")

if __name__ == "__main__":
    train_and_save()
