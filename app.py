# Note: if code is running then paste http://127.0.0.1:5000/ or localhost:5000
# onto browser to get it to work.

# to get the following import to work, it might be necessary to run this
# the terminal:
# python3 -m pip install flask 

# render_template sends HTML files from templates folder
# jsonify converts Python dictionaries into JSON for APIs
# request lets you read incoming data from the browser
from flask import Flask, render_template, jsonify, request

# Creates webapp located at __name__
# This is used to find the folders in the project
app = Flask(__name__)

# Tracks clicks
counter = 0

# When someone visits the website, 
@app.route("/")

# run home and load templates/index.html to send to the browser
def home():
    return render_template("index.html")

# Note: Only allows get requests
# When making an HTTP request to "/api/count", 
@app.route("/api/count", methods=["GET"])

# use the global version of counter to sends a jsonified version of counter
# to the browser
def get_count():
    global counter
    return jsonify({"count": counter})

# Note: Allows route to accept & process data
# When making an HTTP request to "/api/increment",
@app.route("/api/increment", methods=["POST"])

# increase the counter by 1 and sends jsonified version of counter
# to the browser
def increment():
    global counter
    counter += 1
    return jsonify({"count": counter})

# if executed firectly, start the Flask server and enable
# the debugger
if __name__ == "__main__":
    app.run(debug=True)