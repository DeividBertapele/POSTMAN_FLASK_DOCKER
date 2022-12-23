from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def flask_api():
        return "<h1> FLASK API.... </h1>"


@app.route('/get_api', methods=["GET"])
def get_method():
    # if request.method == "GET":
        return "<h1> GET API funcionando..!! </h1>"


@app.route('/post_api', methods=["POST"])
def post_method():
    # if request.method == "POST":
        return "<h1> POST API..!! </h1>"


@app.route('/put_api', methods=["PUT"])
def put_method():
    # if request.method == "PUT":
        return "<h1> PUT API...!! </h1>"


@app.route('/delete_api', methods=["DELETE"])
def delete_method():
    # if request.method == "PUT":
        return "<h1> DELETE API...!! </h1>"
    


 
if __name__ == "__main__":
    app.run(debug=True)