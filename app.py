from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/add-data", methods=["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        }, 400)

if __name__=="__main__":
    app.run(Debug=True)