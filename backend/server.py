from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/gigs', methods=['GET'])
def get_gigs():
    with open('backend/gigs.json') as f:
        gigs = json.load(f)
    return jsonify(gigs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
