from flask import Flask, request, render_template
from functions import get_file

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == "POST":
        url = request.form['url']
        type_ = request.form['type']
        get_file(url, type_)
    return render_template("home.html")