from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_prediction_ia():
    reponse = client.post("/predire", json={"surface_m2": 80})
    assert reponse.status_code == 200
    assert reponse.json() == {
        "surface_m2": 80.0,
        "prix_estime_millions_fcfa": 40.0
    }
