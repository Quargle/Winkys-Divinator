from flask import Flask, render_template, request
from lib import run_duel, var
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
        # call duel
        run_duel.main(form)
    return render_template(
        "duel.html",
        form=form,
        method=request.method,
        output=var.output)


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