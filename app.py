import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# IPFS API URL
IPFS_API_URL = "http://127.0.0.1:5002/api/v0"

# Upload file to IPFS
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    files = {'file': file.read()}
    response = requests.post(f"{IPFS_API_URL}/add", files=files)
    if response.status_code == 200:
        ipfs_hash = response.json()["Hash"]
        return jsonify({"ipfs_hash": ipfs_hash})
    return jsonify({"error": "Failed to upload"}), 500

# Retrieve file from IPFS
@app.route('/retrieve/<hash>', methods=['GET'])
def retrieve_file(hash):
    response = requests.get(f"http://127.0.0.1:8082/ipfs/{hash}")
    if response.status_code == 200:
        return response.content, 200
    return jsonify({"error": "File not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
