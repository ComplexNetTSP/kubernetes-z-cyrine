from flask import Flask, request
from datetime import datetime
import socket

app = Flask(__name__)

@app.route('/')
def home():
    # Obtenir la date actuelle
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Obtenir l'adresse IP du pod
    pod_ip = socket.gethostbyname(socket.gethostname())

    return f"""
        <h1>Hello from Flask App 1 - No DB</h1>
        <p>Current Date: {current_date}</p>
        <p>Pod IP Address: {pod_ip}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

