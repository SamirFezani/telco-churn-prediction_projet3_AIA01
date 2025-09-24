
from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
import os

app = FastAPI(title='Telco Churn Prediction API')

MODEL_PATH = os.environ.get('MODEL_PATH', 'models/model.joblib')
model = None

@app.on_event('startup')
def load_model():
    global model
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
    else:
        model = None

@app.get('/health')
def health():
    return {'status':'ok', 'model_loaded': model is not None}

@app.post('/predict')
def predict(payload: dict):
    if model is None:
        raise HTTPException(status_code=503, detail='Model not loaded on server')
    df = pd.DataFrame([payload])
    # NOTE: the pipeline expected the same columns as during training.
    proba = model.predict_proba(df)[:,1][0]
    return {'churn_proba': float(proba)}
