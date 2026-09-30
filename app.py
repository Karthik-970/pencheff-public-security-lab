import os

from flask import Flask, render_template, request

app = Flask(__name__)

# Credentials must never be hardcoded in source. Load them from the
# environment (or a secrets manager) instead.
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search")
def search():
    query = request.args.get("q", "")

    # Jinja2 autoescaping ensures user-controlled input is safely
    # rendered rather than injected into raw HTML.
    return render_template("search.html", query=query)


if __name__ == "__main__":
    app.run()
