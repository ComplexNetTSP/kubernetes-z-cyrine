# Utiliser l'image officielle Python
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires
COPY app.py /app/

# Installer les dépendances
RUN pip install flask pymongo

# Exposer le port
EXPOSE 5000

# Lancer l'application
CMD ["python", "app.py"]
