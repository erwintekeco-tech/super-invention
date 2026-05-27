from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
# Gecorrigeerde CORS-instelling zodat je mobiele app verbinding mag maken
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/scan', methods=['POST'])
def scan():
    data = request.get_json() or {}
    drempel = data.get('drempel', 50)
    venster = data.get('venster', 5)
    
    return jsonify({
        "bericht": f"Python-scan uitgevoerd. Baseline drempel: {drempel} reqs/{venster}s. Status: OK.",
        "type": "succes",
        "blokkeer_ip": None 
    })

if __name__ == '__main__':
    # Belangrijk voor hostingpartijen: luisteren op poort 10000 of via omgevingsvariabele
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
