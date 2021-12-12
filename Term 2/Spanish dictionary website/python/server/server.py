from flask import send_file, Flask

app = Flask(__name__)

@app.route("/")
def main():
    return send_file("screenshot.png", mimetype="image/png")

app.run()