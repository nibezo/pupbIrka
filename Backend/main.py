from flask import Flask, request, Response
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def root():
    return Response(json.dumps({"message": "Hello"}),
                    status=200, mimetype='application/json')
