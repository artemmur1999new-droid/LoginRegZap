from flask import Flask, request
from requests import post
import os

app = Flask(__name__)

@app.route("/login/<site:path>")
def login(site)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    host = "0.0.0.0"
    app.run(
        debug=False,
        port=port,
        host=host
    )
