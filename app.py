from flask import Flask, render_template
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

# list of cat images
images = ""


@app.route("/")
def index():
    return render_template("index.html")#, url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",5000)))