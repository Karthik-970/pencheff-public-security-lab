from flask import Flask, request

app = Flask(__name__)

# INTENTIONAL LAB FINDING:
# Fake credential for testing secret detection.
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"


@app.route("/")
def home():
    return "<h1>Pencheff Public Security Lab</h1>"


@app.route("/search")
def search():
    query = request.args.get("q", "")

    # INTENTIONAL LAB FINDING:
    # User-controlled input is inserted directly into HTML.
    return f"<h2>Search result: {query}</h2>"


if __name__ == "__main__":
    app.run()
