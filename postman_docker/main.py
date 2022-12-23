from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    if request.method == "GET":
        return jsonify({"response": "Hello World!!!" })
    
        
    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    