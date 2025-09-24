
"""Training, evaluation and model persistence."""
import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
from sklearn.pipeline import Pipeline
from .features import build_preprocessor

def train_baseline(X, y, model_type='random_forest', random_state=42):
    preprocessor = build_preprocessor(X.join(y))
    if model_type == 'logistic':
        clf = LogisticRegression(max_iter=1000, random_state=random_state)
        param_grid = {'clf__C':[0.01,0.1,1,10]}
    else:
        clf = RandomForestClassifier(random_state=random_state, n_jobs=-1)
        param_grid = {'clf__n_estimators':[100,200], 'clf__max_depth':[5,10,None]}

    pipe = Pipeline(steps=[('pre', preprocessor), ('clf', clf)])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=random_state)

    gs = GridSearchCV(pipe, {'clf__' + k.split('__')[-1]: v for k,v in param_grid.items()} if False else {}, cv=3, n_jobs=-1)  # placeholder no grid by default
    # We will fit the pipeline directly (GridSearch can be used later)
    pipe.fit(X_train, y_train)
    preds = pipe.predict(X_test)
    probs = pipe.predict_proba(X_test)[:,1] if hasattr(pipe, 'predict_proba') else None

    results = {
        'accuracy': accuracy_score(y_test, preds),
        'precision': precision_score(y_test, preds),
        'recall': recall_score(y_test, preds),
        'f1': f1_score(y_test, preds),
        'roc_auc': roc_auc_score(y_test, probs) if probs is not None else None,
        'confusion_matrix': confusion_matrix(y_test, preds).tolist()
    }
    return pipe, results

def save_model(pipeline, path='models/model.joblib'):
    joblib.dump(pipeline, path)
    return path
