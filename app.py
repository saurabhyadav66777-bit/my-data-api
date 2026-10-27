from flask import Flask, request

app = Flask(__name__)

# केवल अपने अधिकृत टेस्ट डेटा का उपयोग करें
DATA = {
    "demo": {
        "status": "success",
        "name": "Demo User",
        "message": "My API is working"
    }
}

@app.get("/")
def home():
    return {
        "service": "My Custom API",
        "status": "online"
    }

@app.get("/lookup")
def lookup():
    query = request.args.get("q", "").strip()

    if not query:
        return {"error": "q parameter is required"}, 400

    result = DATA.get(query)

    if result is None:
        return {"status": "not_found"}, 404

    return result

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)