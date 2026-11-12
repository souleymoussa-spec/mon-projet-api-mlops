import joblib
from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="API Prédiction Immobilière")

# Active la collecte automatique des métriques sur la route /metrics
Instrumentator().instrument(app).expose(app)

modele = joblib.load("modele_prix.joblib")

class Appartement(BaseModel):
    surface_m2: float

@app.get("/")
def lire_racine():
    return {"statut": "Modèle IA prêt à prédire"}

@app.post("/predire")
def predire_prix(appart: Appartement):
    prediction = modele.predict([[appart.surface_m2]])
    prix_estime = round(float(prediction[0]), 2)
    return {
        "surface_m2": appart.surface_m2,
        "prix_estime_millions_fcfa": prix_estime
    }
