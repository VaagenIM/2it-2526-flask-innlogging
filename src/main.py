# Algoritme som bruker salt & pepper X
# Krypteringsfunksjon X

# TODO: Lagring av brukerdata - Ser på det imorgen

from flask import Flask, render_template, request, redirect
from user import User
from pprint import pprint

# Temporary (RAM lagring)
users = {} # Type {[str, User]}

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def get_register():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def post_register():
    form_data = request.form.to_dict()
    username = form_data.get("username")
    password = form_data.get("password")

    # TODO: Hvis bruker allerede eksisterer...?
    # TODO: Hvis brukernavn / passord er tomt??

    users[username.lower()] = User(username, password)
    pprint(users)
    return redirect("/")

@app.route("/login", methods=["POST"])
def post_login():
    username = request.form.get("username")
    if username.lower() in users:
        ... # ? ;)

# Dev mode:
if __name__ == "__main__":
    app.run(debug=True)
