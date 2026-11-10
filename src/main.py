# Algoritme som bruker salt & pepper X
# Krypteringsfunksjon X

# TODO: Lagring av brukerdata - Ser på det imorgen

from pprint import pprint

from flask import Flask, redirect, render_template, request, session

from decorators import login_required
from logger import logger
from user import User, get_all

# Temporary (RAM lagring)
users = get_all()  # Type {[str, User]}

app = Flask(__name__)
app.secret_key = "3hfdsajfhskruk"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/log-out")
def log_out():
    session.clear()
    return redirect("/")


@app.route("/register")
def get_register():
    logger.debug("Viser registeringsside")
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def post_register():
    user = User(**request.form)
    logger.debug(user)
    # TODO: Hvis bruker allerede eksisterer...?
    # TODO: Hvis brukernavn / passord er tomt??

    users[user.username.lower()] = user
    session["user"] = user
    session["logged_in"] = True
    pprint(users)
    return redirect("/")


@app.route("/min-profil")
@login_required
def min_profil():
    return render_template("min_profil.html")


@app.route("/log-in")
def get_login():
    return render_template("login.html")


@app.route("/log-in", methods=["POST"])
def post_login():
    user = users.get(request.form.get("username").lower(), False)
    logger.debug(user)
    if not user or not user.check_password(request.form.get("password")):
        logger.info("Feil passord")
        return render_template(
            "login.html", error_msg="Feil brukernavn eller passord.", form=request.form
        )
    logger.info("Riktig passord")
    session["user"] = user
    session["logged_in"] = True
    return redirect("/")


@app.route("/comment/<post_id>", methods=["GET"])
def comment(post_id):
    form_data = request.form
    comment = form_data.get("comment")
    if not session.get("logged_in"):
        return "du må logge inn :("
    return "OK"


# Dev mode:
if __name__ == "__main__":
    logger.info("App started.")
    logger.debug(app.debug)
    app.run(host="0.0.0.0")
