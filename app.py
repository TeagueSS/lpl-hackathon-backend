from flask import Flask, request, jsonify
from Services import *
from Services.ClientService import ClientService
from Services.AdvisorService import AdvisorService
from Services.MatchingService import MatchingService
from Models.Client import Client

app = Flask(__name__)

client_service = ClientService()
advisor_service = AdvisorService()
matching_service = MatchingService()

@app.route("/test", methods=["GET"])
def test_endpoint():
    return {"message": "API is working!"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

@app.route('/add_client', methods=['POST'])
def add_client():
    data = request.json
    client_id = client_service.add_client(data)
    return jsonify({"client_id": client_id})

@app.route('/get_client', methods=['GET'])
def get_client():
    client_id = request.args.get('client_id')
    client = client_service.get_client(client_id)
    return jsonify(client)

@app.route('/add_advisor', methods=['POST'])
def add_advisor():
    data = request.json
    advisor_id = advisor_service.add_advisor(data)
    return jsonify({"advisor_id": advisor_id})

@app.route('/get_advisor', methods=['GET'])
def get_advisor():
    advisor_id = request.args.get('advisor_id')
    advisor = advisor_service.get_advisor(advisor_id)
    return jsonify(advisor)

@app.route('/find_matching_advisor', methods=['POST'])
def find_matching_advisor():
    data = request.json
    client_id = data.get('client_id')
    email = data.get('email')
    matches = matching_service.find_matching_advisor(client_id, email)
    return jsonify(matches)

if __name__ == '__main__':
    app.run(debug=True)
