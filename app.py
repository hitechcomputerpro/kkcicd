from flask import Flask, render_template
from flask_cors import CORS
app = Flask(__name__, template_folder="template", static_folder="static")
CORS(app)
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run( port=3000, host="0.0.0.0")