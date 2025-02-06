from flask import Flask, request
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# Connexion à MongoDB
client = MongoClient("mongodb://mongodb:27017")
db = client.challenge_db
collection = db.requests

@app.route('/')
def home():
    # Récupération de l'adresse IP du client et de la date actuelle
    client_ip = request.remote_addr
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Insertion dans MongoDB
    collection.insert_one({"client_ip": client_ip, "date": current_date})

    # Récupération des 10 dernières entrées
    last_requests = collection.find().sort("_id", -1).limit(10)
    last_requests_html = "<ul>"
    for req in last_requests:
        last_requests_html += f"<li>{req['client_ip']} - {req['date']}</li>"
    last_requests_html += "</ul>"

    return f"""
        <h1>Hello from Flask App 2</h1>
        <p>Connected to MongoDB</p>
	<h1>Version : V2<h1>
        <p>Server Hostname: {client_ip}</p>
        <p>Current Date: {current_date}</p>
        <h3>Last 10 Requests</h3>
        {last_requests_html}
    """

@app.route('/healthz')
def health_check():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
