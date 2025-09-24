
"""Ingestion & basic cleaning utilities for Telco churn dataset."""
import pandas as pd
import os

def load_data(path: str) -> pd.DataFrame:
    """Load CSV dataset from path."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Data file not found: {path}")
    df = pd.read_csv(path)
    return df

def basic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    """Simple cleaning:
    - Strip columns, convert TotalCharges to numeric, fill missing Tenure for new customers, etc.
    """
    df = df.copy()
    # Strip whitespace in column names and object values
    df.columns = df.columns.str.strip()
    obj_cols = df.select_dtypes(['object']).columns
    for c in obj_cols:
        df[c] = df[c].str.strip()
    # Convert TotalCharges to numeric (it may have spaces)
    if 'TotalCharges' in df.columns:
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    # Example: fill missing TotalCharges with 0 for customers with tenure 0
    if 'tenure' in df.columns and 'TotalCharges' in df.columns:
        df.loc[df['tenure'] == 0, 'TotalCharges'] = 0.0
    # Drop customerID if present
    if 'customerID' in df.columns:
        df = df.drop(columns=['customerID'])
    return df
