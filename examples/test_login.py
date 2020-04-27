#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/24 9:41
# @Author  : yangbin.huang
# @Email   : yangbin.huang@things-matrix.com
# @File    : test_login.py


from parameterized import parameterized
import pytest

from common.content_patterns import urls_content
from common.url.url_builder import get_url
from pages.pageobject.signin.sign_in_page import SignInPage
from pages.home_page import HomePage


class TestLogin(HomePage, SignInPage):

    @pytest.mark.smoke
    def test_login(self):
        self.open_login_page(get_url(urls_content.USER_LOGIN))
        self.check_login_title("ThingsMatrix - Login")
        self.login("admin", "TMX2019demo")
        self.check_page_title("ThingsMatrix - Home")
        self.verify_user_badge("AS")

    @parameterized.expand([("admin", "invalid"), ("invalid", "TMX2019demo")])
    @pytest.mark.fail
    def test_login_fail(self, username, password):
        self.open_login_page(get_url(urls_content.USER_LOGIN))
        self.login(username, password)
        # 用户名、密码错误或域名访问受限
        # error in username or password, or restricted access to domain names
        self.login_fail_message("用户名、密码错误或域名访问受限")
