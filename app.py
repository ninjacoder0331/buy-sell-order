from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Flask API on Vercel!",
        "status": "success",
        "version": "1.0.0"
    })

@app.route("/buyOrder", methods=["POST"])
def buyorder():
    try:
        external_url = "https://freedomtracker.net/api/buyOrder"
        data = {
            "symbol": request.json.get("symbol"),
            "qty": request.json.get("qty")
        }
        response = requests.post(external_url, json=data)

        ibkr_external_url = "https://evolved-leech-firstly.ngrok-free.app/buy"
        ibkr_data = {
            "symbol" : request.json.get("symbol"),
            "quantity" : request.json.get("qty")
        }
        ibkr_response = request.post(ibkr_external_url , json=ibkr_data)

        if response.status_code == 200 and ibkr_response.status_code == 200:
            return jsonify({"status" : response.json()})
        else:
            return jsonify({"status" : "error"})


    except Exception as e:
        return jsonify({"status" : "error"})

@app.route("/sellOrder", methods=["POST"])
def sellorder():
    try:
        external_url = "https://freedomtracker.net/api/sellOrder"
        data = {
            "symbol" : request.json.get("symbol"),
            "qty" : request.json.get("qty")
        }
        response = requests.post(external_url, json=data)

        ibkr_external_url = "https://evolved-leech-firstly.ngrok-free.app/sell"
        ibkr_data = {
            "symbol" : request.json.get("symbol"),
            "quantity" : request.json.get("qty")
        }
        ibkr_response = request.post(ibkr_external_url, json=ibkr_data)
        if response.status_code == 200 and ibkr_response.status_code == 200:
            return jsonify({"status" : response.json()})
        else:
            return jsonify({"status" : "error"})
            
    except Exception as e:
        return jsonify({"status" : "error"})

# For local development
if __name__ == '__main__':
    app.run(debug=True)

# For Vercel deployment
application = app 