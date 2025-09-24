
# Telco Customer Churn - Projet 3 (AIA01)

Auteur: Samir Fezani
Description: Projet de prédiction du churn client à partir du dataset 'Telco Customer Churn'.

## Structure du dépôt
- `notebooks/` : notebooks Jupyter (EDA, modelling)
- `src/telco_churn/` : package python (ingestion, preprocessing, features, models, api)
- `data/` : dossier pour données (NE PAS pousser les jeux bruts sur GitHub; utiliser DVC ou Git LFS)
- `models/` : modèles enregistrés (à versionner via DVC si nécessaire)
- `tests/` : tests unitaires
- `.github/workflows/` : CI (tests + lint)

## Installation
```bash
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

## Récupérer le dataset Telco (Kaggle)
Tu peux télécharger le jeu de données (Telco Customer Churn) depuis Kaggle :
```bash
# Option 1: utiliser l'API Kaggle (recommandée)
kaggle datasets download -d blastchar/telco-customer-churn -p data/raw --unzip
# Option 2: curl (si tu as un lien direct)
curl -L -o ~/Downloads/telco-customer-churn.zip https://www.kaggle.com/api/v1/datasets/download/blastchar/telco-customer-churn
```

## Usage rapide (exemples)
- Lancer le notebook principal `notebooks/01_EDA_and_Modeling.ipynb` (Jupyter Lab/Notebook)
- Entraîner un modèle depuis `src/telco_churn/models.py`
- Lancer l'API de prédiction (exemple):
  ```bash
  uvicorn src.telco_churn.api:app --reload --port 8080
  ```

## Rendu final
Avant de créer l'archive finale :
- Nettoyer les outputs des notebooks (`nbstripout` ou `jupyter nbconvert --clear-output`).
- Inclure `REPORT.pdf` ou `rapport.md` expliquant la méthodologie et résultats.
- Nomme l'archive: `samir_fezani_projet3_AIA01.zip`
