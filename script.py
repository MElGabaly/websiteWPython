# import flask class from flask lib
# render temp to use html file
from flask import Flask, render_template

# name the script as main
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
