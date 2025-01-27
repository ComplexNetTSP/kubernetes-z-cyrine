from flask import Flask, request
from datetime import datetime
import socket

app = Flask(__name__)

@app.route("/")
def homepage():
    server_ip = request.host_url
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
        <h1>Cyrine ZRIBI</h1>
        <h2>Project: My Simple Flask Web Page</h2>
        <p>Version: V1</p>
        <p>Server Hostname: {server_ip}</p>
        <p>Current Date: {current_date}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
