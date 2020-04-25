#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 14:30
# @Author  : yangbin.huang
# @Email   : yangbin.huang@things-matrix.com
# @File    : test_login.py


from seleniumbase import BaseCase
import pytest

from pages.pageobject.signin.sign_in_page import SignInPage
from common.content_patterns import urls_content
from common.url.url_builder import get_url


class TestLogin(SignInPage, BaseCase):

    def test_login_success(self):
        self.open_login_page(get_url(urls_content.USER_LOGIN))
        self.type_username("admin")
        self.type_password("TMX2019demo")
        self.click_login_button()

    @pytest.mark.smoke
    def test_login(self):
        self.open_login_page(get_url(urls_content.USER_LOGIN))
        self.check_login_title("ThingsMatrix - Login")
        self.login("admin", "TMX2019demo")
        self.assert_title("ThingsMatrix - Home")



