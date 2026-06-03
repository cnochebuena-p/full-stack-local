# Note: if code is running then paste http://127.0.0.1:5000/ or localhost:5000
# onto browser to get it to work.

# to get the following import to work, it might be necessary to run this
# the terminal:
# python3 -m pip install flask 
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

counter = 0

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/count", methods=["GET"])
def get_count():
    global counter
    return jsonify({"count": counter})

@app.route("/api/increment", methods=["POST"])
def increment():
    global counter
    counter += 1
    return jsonify({"count": counter})

if __name__ == "__main__":
    app.run(debug=True)