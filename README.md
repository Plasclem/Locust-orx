# Locust Orchestra Load Test

Ce dépôt contient un fichier `locustfile.py` minimaliste pour lancer un test de charge sur le site [orchestra.eu](https://www.orchestra.eu).

## Prérequis
- Python 3.10 ou supérieur
- Les dépendances listées dans `requirements.txt`

### Installation rapide
Créez un environnement virtuel dédié puis installez les dépendances :

```bash
python -m venv .venv
source .venv/bin/activate  # sous Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Lancer le test
```bash
locust -f locustfile.py
```

Ensuite, ouvrez l'interface web de Locust (http://localhost:8089 par défaut) pour configurer le nombre d'utilisateurs simultanés et le taux de montée en charge.
