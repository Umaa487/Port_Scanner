from routes.scan import scanner_api
from routes.status import scanner_status as sc
from flask import Flask, request

app = Flask(__name__)

@app.route("/scan", methods=['POST'])
def scan():
    data = request.get_json()
    scanner_api.scan_response(data)

@app.route("/status/<id>", methods=['GET'])
def status(id):
    sc.status_response(id)

if __name__ == '__main__':
    app.run(debug=True)
