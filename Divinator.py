from flask import Flask, render_template, request, redirect, url_for
from lib import run_duel, character
from forms import DuelForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/duel", methods=["GET", "POST"])
def duel():

    form = DuelForm()
    if request.method == "POST":
        # Character 1
        char1 = {}
        char1['Name'] = form.char1_name.data
        char1['Class'] = form.char1_class.data
        char1['Race'] = form.char1_race.data
        char1['Weapon'] = form.char1_weapon.data
        # Character 2
        char2 = {}
        char2['Name'] = form.char2_name.data
        char2['Class'] = form.char2_class.data
        char2['Race'] = form.char2_race.data
        char2['Weapon'] = form.char2_weapon.data

        # call duel
        run_duel.main(char1, char2)
        # TODO: return page with results
    return render_template("duel.html", form=form)


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
    app.run(debug=True)