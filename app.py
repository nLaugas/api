from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"

@app.route("/json")
def getJson():
  return jsonify(username="user",
                   email="@gmail",
                   id="2")

if __name__ == '__main__':
    app.run()


"""localhost:5000/"""