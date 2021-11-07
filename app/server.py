from flask import Flask, render_template, url_for, request, redirect, make_response
from common import *
from logging import getLogger
logger = getLogger(__name__)



app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def root():

    if request.method == "GET":
        return render_template('index.html')

    elif request.method == "POST":
        
        data = request.json
        id_val = data["id"]
        password_val = data["password"]

        if authentication(id_val, password_val):
            res = make_response(render_template('sample.html'))
            res.headers.set("Access-Control-Allow-Origin", "*")
            res.headers.set("Access-Control-Allow-Credentials", True)
            return render_template('sample.html')
        else:
            return "authentication error."

@app.route("/account", methods=['GET', 'POST'])
def account():

    if request.method == 'GET':
        return render_template('create_account.html')

    if request.method == 'POST':
        data = request.json
        id_val = data["id"]
        display_name_val = data["display_name"]
        password_val = data["password"]
        search_id_val = data["search_id"]

        # db 登録
        
        return data
        
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)