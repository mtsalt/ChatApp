from flask import render_template, request
from . import main
from flask import current_app
from app.models.chat_setting.account_manager import create_account

@main.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # TODO セッションが残っていれば、そのままチャット画面表示
        #current_app.logger.info("get")
        return render_template("index.html")

    if request.method == 'POST':
        return render_template("success.html")


@main.route("/register", methods=['GET', 'POST'])
def register():

    if request.method == 'GET':
        return render_template("auth/register.html")

    if request.method == 'POST':
        # TODO : Validation 処理（必須。クライアントにも実装）
        user_id = request.json["user_id"]
        password = request.json["password"]
        confirm_password = request.json["confirm_password"]
        display_name = request.json["display_name"]
        search_id = request.json["search_id"]

        # user_id
        #    - 同じIDが存在していないか
        #    - アルファベット + 数字 の文字列で構成されているか
        #    - 1文字以上 文字以下の文字列で構成されているか

        # password
        #    - 確認用パスワードと同じ文字列であるか
        #    - アルファベット + 数字 の文字列で構成されているか
        #    - 文字以上 文字以下の文字列で構成されているか

        # display_name
        #    = 文字以上 文字以下の文字列で構成されているか

        # search_id
        #    - 文字以上 文字以下の文字列で構成されているか

        create_account(user_id, password, display_name, search_id)

        if True:
            return render_template("auth/login.html")


@main.route("/login", methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template("auth/login.html")

    if request.method == 'POST':
        user_id = request.json["user_id"]
        password = request.json["password"]
        current_app.logger.info("id: " + user_id + ",  pass: " + password)
        return render_template("success.html")


@main.route("/logout", methods=['GET'])
def logout():
    # ページアクセスをきっかけにして、セッション情報などからログアウト
    pass

