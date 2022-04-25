from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Home Page</p>"

@app.route("/classes")
def classes():
    return "<p>Classes</p>"

@app.route("/contact")
def contact():
    return "<p>Contact</p>"

@app.route("/donate")
def donate():
    return "<p>Donate</p>"

@app.route("/faq")
def faq():
    return "<p>FAQ</p>"

@app.route("/gallery")
def gallery():
    return "<p>Gallery</p>"

@app.route("/press")
def press():
    return "<p>Press</p>"

@app.route("/schedule")
def schedule():
    return "<p>Schedule</p>"

@app.route("/sports")
def sports():
    return "<p>Sports</p>"