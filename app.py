from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "GNSS Error Prediction Backend is Running ✅"})

@app.route("/datasets", methods=["GET"])
def list_datasets():
    datasets = ["GEO", "MEO", "MEO2"]
    return jsonify(datasets)

@app.route("/graph/<dataset>", methods=["GET"])
def get_graph(dataset):
    dataset = dataset.lower()
    filename = f"{dataset}_graph.png"
    path = os.path.join(app.root_path, "static")

    if not os.path.exists(os.path.join(path, filename)):
        return jsonify({"error": "Graph not found"}), 404

    return send_from_directory(path, filename)

@app.route("/result/<dataset>", methods=["GET"])
def get_result(dataset):
    dataset = dataset.lower()
    filename = f"{dataset}_result.json"
    path = os.path.join(app.root_path, "results")

    if not os.path.exists(os.path.join(path, filename)):
        return jsonify({"error": "Result not found"}), 404

    with open(os.path.join(path, filename)) as f:
        data = json.load(f)

    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
