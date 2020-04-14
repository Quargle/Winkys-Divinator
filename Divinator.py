from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/duel")
def duel():
    return render_template("duel.html")


@app.route("/thousand_duels")
def thousand_duels():
    return render_template("thousand.html")


@app.route("/goblins")
def goblins():
    return render_template("goblins.html")


if __name__ == "__main__":
    app.run(debug=True)