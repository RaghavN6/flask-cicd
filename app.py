from flask import Flask

app = Flask(__name__)


@app.get("/")
def home():
    return {"message": "Flask CI/CD application is running"}, 200


@app.get("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
