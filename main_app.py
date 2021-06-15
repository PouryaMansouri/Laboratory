from flask import Flask

from user.views import register_get, register_post

app = Flask(__name__, template_folder="templates")


def index():
    return "home"


app.add_url_rule('/', 'home', index)
app.add_url_rule('/register/', 'register_get', register_get, methods=["get"])
app.add_url_rule('/register/', 'register_post', register_post, methods=["post"])

app.run()
