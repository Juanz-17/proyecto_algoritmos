from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Conexión MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["analisis_algoritmos"]
resultados = db["resultados"]

@app.route("/")
def home():
    return jsonify({"mensaje": "Backend Flask funcionando correctamente"})

@app.route("/api/guardar", methods=["POST"])
def guardar_resultado():
    data = request.json
    resultados.insert_one(data)
    return jsonify({"mensaje": "Resultado guardado correctamente"}), 201

@app.route("/api/resultados", methods=["GET"])
def obtener_resultados():
    docs = list(resultados.find({}, {"_id": 0}))
    return jsonify(docs)

if __name__ == "__main__":
    app.run(debug=True)