from flask import Flask, render_template, request, redirect, url_for
import helper

app = Flask(__name__)

# FRAGE 2 – Wie werden die Daten gespeichert?
# Stateless in einer In-Memory-Liste im Modul helper
# Jedes Todo ist ein Dataclass-Objekt mit Feldern: title, isCompleted.

@app.route("/", methods=["GET"])
def index():
    todos = helper.get_all()
    # FRAGE 3 – Wie werden die Daten an die index.html übergeben?
    # Über render_template als Template-Variable todos
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    title = (request.form.get("title") or "").strip()
    if title:
        # FRAGE 1 – Wo findet die „Ver-BBB-isierung“ statt?
        # In helper.bbbify(title), das von helper.add benutzt wird
        helper.add(title)
    return redirect(url_for("index"))

@app.route("/update/<int:index>", methods=["GET"])
def update(index: int):
    helper.toggle(index)
    return redirect(url_for("index"))

# FRAGE 4 – Wie ist definiert, auf welche URLs die App reagiert?
# Über @app.route Dekoratoren
@app.route("/create/<title>", methods=["GET"])
def create_via_url(title: str):
    title = (title or "").strip()
    if title:
        helper.add(title)
    return redirect(url_for("index"))

if __name__ == "__main__":
    # Direktstart: python main.py
    app.run(debug=True)
