# test_data.py
import sys
import pandas as pd

# Vérifier l'interpréteur Python
print("Python utilisé :", sys.executable)

# Vérifier la version de pandas
print("Version de pandas :", pd.__version__)

# Chemin du dataset
data_path = "data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv"


# Charger le dataset
try:
    df = pd.read_csv(data_path)
    print("✅ Dataset chargé avec succès !")
except FileNotFoundError:
    print(f"❌ Fichier non trouvé à {data_path}")
    exit()

# Infos du dataset
print("\nShape du dataset :", df.shape)
print(df.head())
print(df.info())
print(df.isnull().sum())
