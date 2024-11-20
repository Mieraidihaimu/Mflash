from flask import Blueprint, jsonify

def register_routes(app):
    @app.route('/')
    def home():
        return "Hello, Flask is running!"

    @app.route('/api/ping', methods=['GET'])
    def ping():
        return jsonify({"message": "Pong!"})
