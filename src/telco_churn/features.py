
"""Feature engineering and preprocessing pipeline."""
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np

def build_preprocessor(df: pd.DataFrame):
    # Identify columns
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    cat_cols = df.select_dtypes(include=['object', 'bool', 'category']).columns.tolist()
    # Remove target if present
    if 'Churn' in num_cols:
        num_cols.remove('Churn')
    if 'Churn' in cat_cols:
        cat_cols.remove('Churn')

    numeric_transformer = Pipeline(steps=[
        ('scaler', StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ('ohe', OneHotEncoder(handle_unknown='ignore', sparse=False))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, num_cols),
            ('cat', categorical_transformer, cat_cols),
        ],
        remainder='drop'
    )
    return preprocessor
