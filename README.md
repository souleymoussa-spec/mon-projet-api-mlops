# 🚀 API de Prédiction Immobilière (Pipeline MLOps Complet)

Ce projet met en œuvre une architecture **MLOps / DevOps** de bout en bout pour entraîner, tester, conteneuriser, surveiller et déployer un modèle de Machine Learning.

## 🛠️ Technologies utilisées
* **Machine Learning :** Python 3.11, Scikit-learn, Joblib
* **API & Documentation :** FastAPI, Uvicorn, Pydantic (Swagger UI)
* **Tests Automatisés :** Pytest, HTTPX
* **Conteneurisation :** Docker & Docker Compose
* **Observabilité & Monitoring :** Prometheus & Grafana
* **CI/CD :** GitHub Actions

## 📂 Architecture du projet
* `train.py` : Entraîne le modèle de régression linéaire et sauvegarde `modele_prix.joblib`.
* `main.py` : Expose l'API REST (`/predire`) et les métriques Prometheus (`/metrics`).
* `test_main.py` : Vérifie automatiquement le bon fonctionnement des prédictions.
* `Dockerfile` & `docker-compose.yml` : Orchestre l'API, Prometheus et Grafana.
* `.github/workflows/ci.yml` : Lance automatiquement les tests `pytest` à chaque `git push`.

## ⚡ Lancer le projet en local (avec Docker)

1. Cloner le dépôt :
   ```bash
   git clone https://github.com
   cd mon-projet-api-mlops
   ```

2. Démarrer l'API, Prometheus et Grafana :
   ```bash
   docker compose up --build -d
   ```

3. Accéder aux interfaces :
   * **Documentation interactive (Swagger) :** `http://localhost:8000/docs`
   * **Prometheus :** `http://localhost:9090`
   * **Grafana :** `http://localhost:3000` (identifiants : `admin` / `admin`)
