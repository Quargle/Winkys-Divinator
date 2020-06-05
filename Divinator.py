
# Standard Library Imports
# Third Party Imports
from flask import Flask, render_template, request
# Local imports
from lib import run_duel, var
import forms


app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/duel", methods=["GET", "POST"])
def duel():

    form = forms.DuelForm()
    # Kind of ugly way of setting name defaults
    if request.method == "GET":
        form.char1.char_name.data = "Character 1"
        form.char2.char_name.data = "Character 2"
    if request.method == "POST":
        # call duel
        char1, char2 = run_duel.main(form)
        return render_template(
            "duel.html",
            form=form,
            method=request.method,
            char1=char1,
            char2=char2,
        )
    return render_template(
        "duel.html",
        form=form,
        method=request.method,
    )


@app.route("/thousand_duels", methods=["GET", "POST"])
def thousand_duels():
    if request.method == "POST":
        pass
        # TODO: return page with results

    return render_template("thousand.html")


@app.route("/goblins", methods=["GET", "POST"])
def goblins():
    if request.method == "POST":
        pass
        # TODO: return page with results

    return render_template("goblins.html")


if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)
