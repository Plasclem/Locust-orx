# Locust Orchestra Load Test

Ce dépôt contient un fichier `locustfile.py` minimaliste pour lancer un test de charge sur le site [orchestra.eu](https://www.orchestra.eu).

## Prérequis
- [Locust](https://docs.locust.io/) 2.x installé dans votre environnement Python

## Lancer le test
```bash
locust -f locustfile.py
```

Ensuite, ouvrez l'interface web de Locust (http://localhost:8089 par défaut) pour configurer le nombre d'utilisateurs simultanés et le taux de montée en charge.
