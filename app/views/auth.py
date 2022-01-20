from flask import render_template, request
from . import main

import logging
logging.basicConfig(level=logging.DEBUG, filename="./app/log/chatapp.log")
logger = logging.getLogger(__name__)


@main.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        logger.info("get index page.")
        # TODO セッションが残っていれば、そのままチャット画面表示
        return render_template("index.html")

    if request.method == 'POST':
        logger.info("post index page.")
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


