import joblib
from sklearn.linear_model import LinearRegression

# Données d'entraînement : Surfaces en m² (X) et Prix en millions de FCFA (y)
X = [[30], [50], [70], [100], [120]]
y = [15, 25, 35, 50, 60]

# Entraînement du modèle
modele = LinearRegression()
modele.fit(X, y)

# Sauvegarde du modèle sur le disque
joblib.dump(modele, "modele_prix.joblib")
print("Modèle entraîné et sauvegardé avec succès !")
