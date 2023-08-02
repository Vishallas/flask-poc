from flask import Flask,render_template, jsonify
import dotenv
import os

app = Flask(__name__)

dotenv.load_dotenv()

@app.route('/')
def index():
    return  render_template("index.html")

@app.route('/ping')
def ping():

    return jsonify("pong")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=int(os.getenv('PORT')))
