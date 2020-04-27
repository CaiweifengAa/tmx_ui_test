#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 14:30
# @Author  : yangbin.huang
# @Email   : yangbin.huang@things-matrix.com
# @File    : test_login.py


import pytest
from parameterized import parameterized

from pages.home_page import HomePage
from pages.pageobject.signin.sign_in_page import SignInPage
from common.content_patterns import urls_content
from common.url.url_builder import get_url


class TestLogin(SignInPage, HomePage):

    @pytest.mark.smoke
    def test_login_success(self):
        self.open_login_page(get_url(urls_content.USER_LOGIN))
        self.type_username("admin")
        self.type_password("TMX2019demo")
        self.click_login_button()
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



