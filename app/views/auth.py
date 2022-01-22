from flask import render_template, request
from . import main
from flask import current_app


@main.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # TODO セッションが残っていれば、そのままチャット画面表示
        #current_app.logger.info("get")
        return render_template("index.html")

    if request.method == 'POST':
        pass


@main.route("/register", methods=['GET', 'POST'])
def register():

    if request.method == 'GET':
        return render_template("auth/register.html")

    if request.method == 'POST':
        pass


@main.route("/login", methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template("auth/login.html")

    if request.method == 'POST':
        pass


