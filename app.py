from flask import Flask, request, Response
from datetime import datetime
import json

app = Flask(__name__)

@app.route("/")
def index():
    data = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "ip": request.headers.get('X-Forwarded-For', request.remote_addr)
    }

    pretty_json = json.dumps(data, indent=2)
    return Response(pretty_json + "\n", mimetype='application/json')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
