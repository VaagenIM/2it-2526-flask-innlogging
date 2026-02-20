# Algoritme som bruker salt & pepper X
# Krypteringsfunksjon X

# TODO: Lagring av brukerdata - Ser på det imorgen

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Wørld!!!"

# Dev mode:
if __name__ == "__main__":
    app.run(debug=True)
