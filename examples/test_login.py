#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/24 9:41
# @Author  : yangbin.huang
# @Email   : yangbin.huang@things-matrix.com
# @File    : test_login.py


from seleniumbase import BaseCase
from parameterized import parameterized
import pytest

from pages.pageobject.signin.sign_in_page import SignInPage


class TestLogin(SignInPage, BaseCase):
    @parameterized.expand([("admin", "TMX2019demo")])
    def test_login_success(self, username, password):
        self.open_login_page("http://120.79.180.135/")
        self.type_username(username)
        self.type_password(password)
        self.click_login_button()

    @pytest.mark.smoke
    def test_login(self):
        self.open_login_page("http://120.79.180.135/")
        self.check_login_title("ThingsMatrix - Login")
        self.login("admin", "TMX2019demo")
        self.assert_title("ThingsMatrix - Home")

    @parameterized.expand([("admin", "invalid"), ("invalid", "TMX2019demo")])
    @pytest.mark.fail
    def test_login_fail(self, username, password):
        self.open_login_page("http://120.79.180.135/")
        self.login(username, password)
        self.assert_text("error in username or password, or restricted access to domain names",
                         ".ivu-message-custom-content")
