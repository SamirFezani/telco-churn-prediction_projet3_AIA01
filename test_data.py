# test_data.py
import sys
import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)  # dossier contenant test_data.py (racine du repo)
main_path = os.path.join(BASE_DIR, "data", "raw", "WA_Fn-UseC_-Telco-Customer-Churn.csv")
sample_path = os.path.join(BASE_DIR, "tests", "sample_telco.csv")

if os.path.exists(main_path):
    data_path = main_path
else:
    print(f" Fichier principal non trouvé, utilisation du sample : {sample_path}")
    data_path = sample_path

df = pd.read_csv(data_path)

def test_not_empty():
    assert not df.empty

def test_expected_columns():
    expected = [
        "gender","SeniorCitizen","Partner","Dependents","tenure",
        "PhoneService","InternetService","MonthlyCharges","TotalCharges","Churn"
    ]
    for col in expected:
        assert col in df.columns
