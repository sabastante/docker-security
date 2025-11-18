from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def root():
    response = {
        "status": 200,
        "message": "welcome to ekoparty hackademy"
    }
    return jsonify(response), 200


@app.get("/health")
def health():
    response = {
        "status": "ok",
        "message": "api is healthy"
    }
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)