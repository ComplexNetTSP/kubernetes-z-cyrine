from flask import Flask, request
from datetime import datetime
import socket
from pymongo import MongoClient

app = Flask(__name__)

# Connexion à MongoDB
client = MongoClient("mongodb://mongodb:27017/")  # Nom du conteneur MongoDB
db = client["challenge_db"] 
collection = db["requests"]

@app.route("/")
def homepage():
    # Récupération des informations
    client_ip = request.remote_addr
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    server_hostname = request.host_url

    # Insertion dans MongoDB
    collection.insert_one({"client_ip": client_ip, "date": current_date})

    # Récupération des 10 dernières entrées
    last_requests = collection.find().sort("_id", -1).limit(10)

    # Génération de l'affichage HTML
    last_requests_html = "<ul>"
    for req in last_requests:
        last_requests_html += f"<li>{req['client_ip']} - {req['date']}</li>"
    last_requests_html += "</ul>"

    return f"""
        <h1>Cyrine ZRIBI</h1>
        <h2>Project:My Simple Flask Web Page</h2>
        <p>Version: V2</p>
        <p>Server Hostname: {server_hostname}</p>
        <p>Current Date: {current_date}</p>
        <h3>Last 10 Requests</h3>
        {last_requests_html}
    """

@app.route('/healthz')
def health_check():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
