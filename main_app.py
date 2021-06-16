from flask import Flask,render_template

from user.views import register_get, register_post

app = Flask(__name__, template_folder="templates")


def index():
    return render_template("index.html")


app.add_url_rule('/', 'home', index)
app.add_url_rule('/register/', 'register_get', register_get, methods=["get"])
app.add_url_rule('/register/', 'register_post', register_post, methods=["post"])

app.run()
