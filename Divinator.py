from flask import Flask, render_template, request, redirect, url_for
from lib import duel

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/duel", methods=["GET", "POST"])
def duel():
    if request.method == "POST":
        character_1_class = request.form.get('p1_class', default='Fighter')
        character_1_race = request.form.get('p1_race', default='Human')
        character_1_weapon = request.form.get('p1_weapon', default='Greatsword')
        character_1 = {
            'class': character_1_class,
            'race': character_1_race,
            'weapon': character_1_weapon,
        }
        character_2_class = request.form.get('p2_class')
        character_2_race = request.form.get('p2_race')
        character_2_weapon = request.form.get('p2_weapon')
        character_2 = {
            'class': character_2_class,
            'race': character_2_race,
            'weapon': character_2_weapon,
        }
        # call duel
        duel.main(character_1, character_2)
        # TODO: return page with results
    return render_template("duel.html")


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