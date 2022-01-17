from mongoengine import connect, disconnect
from mongoengine import Document
from mongoengine import fields

import pymongo
import mongoengine


from app.utils.cryptography import crypto


# TODO : 呼び出しの際は相対インポートを実施する？　（ディレクトリを変更するような処理の方が解りやすいかも）
# TODO : CONST変数をconfigなどに書き込む( DB変数情報 ＆ ポート番号など )
# TODO : Docstring作成
# TODO : LOG保存のために情報を集める
# TODO : 例外の種類を調べる

# TODO : テストのためのフォルダ構成を調べる＆考える

# TODO : configへ移動
ID_MIN_LENGTH = 5
ID_MAX_LENGTH = 30

PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 30

DISPLAYNAME_MIN_LENGTH = 1
DISPLAYNAME_MAX_LENGTH = 20

SEARCHID_MIN_LENGTH = 5
SEARCHID_MAX_LENGTH = 20

MONGODB_HOST = "172.17.0.2"
MONGODB_PORT = 27017
MONGODB_ACCOUNT_DB = ""


class AccountData(Document):
    user_id = fields.StringField(min_length=5, max_length=30, required=True, unique=True)
    password = fields.StringField(min_length=8, max_length=30, required=True)
    display_name = fields.StringField(min_length=1, max_length=20, required=True)
    search_id = fields.StringField(min_length=5, max_length=20, unique=True)


def connect_mongodb():
    # connect to mongodb
    connect(
        db="sample",
        username='sampleUser',
        password='Abc5fHJRTAbn485',
        host=MONGODB_HOST,
        port=MONGODB_PORT
    )


def create_account(user_id, password, display_name, search_id):
    try:
        connect_mongodb()
        new_user = AccountData(
            user_id=user_id,
            password=crypto.encrypt_string(password),
            display_name=display_name,
            search_id=search_id
        )
        new_user.save()
        print("created new user.")
    except mongoengine.connection.ConnectionFailure:
        # ログへの記録と失敗したことのみを伝える
        raise Exception("DBへの登録失敗 - 文字の制約を守っていないから")
    except pymongo.errors.DuplicateKeyError:
        # ログへの記録と失敗したことのみを伝える
        print(user_id, password, display_name, search_id)
        raise Exception("DBへの登録失敗 - 文字の制約を守っていないから")
    except mongoengine.errors.ValidationError:
        # ログへの記録と失敗したことのみを伝える
        print(user_id, password, display_name, search_id)
        raise Exception("")
    finally:
        disconnect()


def update_account_data(user_id, password, display_name, search_id):
    try:
        connect_mongodb()
        target = AccountData.objects.get(user_id=user_id)
        target.password = crypto.encrypt_string(password)
        target.display_name = display_name
        target.search_id = search_id
        target.save()
    except (mongoengine.connection.ConnectionFailure, mongoengine.documents.DoesNotExist):
        # ログへの記録と失敗したことのみを伝える
        raise Exception("DB process error")
    except mongoengine.documents.DoesNotExist:
        # ログへの記録と失敗したことのみを伝える
        pass
    finally:
        disconnect()


def delete_account(user_id):
    try:
        connect_mongodb()
        target = AccountData(user_id=user_id)
        target.delete()
    except mongoengine.connection.ConnectionFailure:
        # ログへの記録と失敗したことのみを伝える
        raise Exception("DBへの登録失敗 - 文字の制約を守っていないから")
    except mongoengine.document.DoesNotExist:
        # ログへの記録と失敗したことのみを伝える
        pass
    finally:
        disconnect()


def _delete_all_account():
    try:
        connect_mongodb()
        target = AccountData.objects.all()
        target.delete()
    except mongoengine.connection.ConnectionFailure:
        # ログへの記録と失敗したことのみを伝える
        raise Exception("DBへの登録失敗 - 文字の制約を守っていないから")
    finally:
        disconnect()


def get_account_data(user_id):
    connect_mongodb()
    try:
        target = AccountData.objects.get(user_id=user_id)
        return target
    except mongoengine.connection.ConnectionFailure:
        # ログへの記録と失敗したことのみを伝える
        raise Exception("DBへの登録失敗 - 文字の制約を守っていないから")
    except mongoengine.documents.DoesNotExist:
        # ログへの記録と失敗したことのみを伝える
        pass
    finally:
        disconnect()
