import unittest
from unittest import TestCase
import app.models.chat_setting.account_manager as am

import pymongo
import mongoengine
import time


class TestCreateAccount(TestCase):

    @classmethod
    def setUpClass(cls):
        print('*** 全体前処理 ***')

    @classmethod
    def tearDownClass(cls):
        print('*** 全体後処理 ***')

    def setUp(self):
        print('+ テスト前処理')

    def tearDown(self):
        print('+ テスト後処理')

    # @unittest.skip("")
    def test_exec_creation(self):
        current_time_str = str(int(time.time() * 100))
        user_id = "uID_" + current_time_str
        password = "pwd_" + current_time_str
        display_name = "" #"dName_" + current_time_str
        search_id = "sID_" + current_time_str

        am.create_account(user_id, password, display_name, search_id)

    @unittest.skip("")
    def test_exec_creation_in_Japanese(self):
        current_time_str = str(int(time.time() * 100))
        user_id = "uID_" + current_time_str
        password = "pwd_" + current_time_str
        display_name = "表示名"
        search_id = "sID_" + current_time_str

        am.create_account(user_id, password, display_name, search_id)

    @unittest.skip("")
    def test_exec_creation_exception_of_NotUniqueError(self):
        current_time_str = str(int(time.time() * 100))
        user_id = "uID_" + current_time_str
        password = "pwd_" + current_time_str
        display_name = "表示名"
        search_id = "sID_" + current_time_str

        with self.assertRaises(mongoengine.errors.NotUniqueError):
            am.create_account(user_id, password, display_name, search_id)
            am.create_account(user_id, password, display_name, search_id)

    def test_delete_all_account(self):
        pass

