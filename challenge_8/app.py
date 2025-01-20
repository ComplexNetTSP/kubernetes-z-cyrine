from flask import Flask, request
from pymongo import MongoClient
from datetime import datetime
import socket

app = Flask(__name__)

# Connexion à MongoDB
mongo_client = MongoClient("mongodb://chall8-mongodb-service:27017/")
db = mongo_client["challenge_db"]
collection = db["requests"]

@app.route('/')
def home():
    # Récupération de l'adresse IP du client et de la date actuelle
    client_ip = request.remote_addr
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Récupération de l'adresse IP du pod
    pod_ip = socket.gethostbyname(socket.gethostname())

    # Insertion dans MongoDB
    collection.insert_one({"client_ip": client_ip, "date": current_date, "pod_ip": pod_ip})

    # Récupération des 10 dernières entrées
    last_requests = collection.find().sort("_id", -1).limit(10)
    last_requests_html = "<ul>"
    for req in last_requests:
        last_requests_html += f"<li> {req['client_ip']} - {req['date']} - {req.get('pod_ip', 'N/A')}</li>"
    last_requests_html += "</ul>"

    return f"""
        <h1>Hello from Flask App</h1>
        <p>Connected to MongoDB</p>
        <p>Current Date: {current_date}</p>
        <p>Pod IP: {pod_ip}</p>
        <h3>Last 10 Requests</h3>
        {last_requests_html}
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
