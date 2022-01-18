from flask import render_template
from . import main


@main.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@main.route("/register", methods=['GET', 'POST'])
def register():
    return render_template("register.html")


@main.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")


