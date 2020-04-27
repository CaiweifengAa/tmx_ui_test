#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/23 14:23
# @Author  : yangbin.huang
# @Email   : yangbin.huang@things-matrix.com
# @File    : sign_in_page.py

from seleniumbase import BaseCase


class SignInPage(BaseCase):

    def __init__(self, *args, **kwargs):
        super(SignInPage, self).__init__(*args, **kwargs)
        self.css_login_title_welcome = "h1.login-title"
        self.css_input_username = "input[type='text']"
        self.css_input_password = "input[type='password']"
        self.css_login_button = "button[type='button']"
        self.css_forget_password_link = "div.forget-psw"
        self.css_sign_up_link = "a.f-right"
        self.css_terms_conditions_link = "a[href='#/tc']"
        self.css_privacy_policy_link = "a[href='#/privacypolicy']"
        self.css_copyrights = "p.inc"
        self.css_message = ".ivu-message-notice-content-text .ivu-message-custom-content"

    def check_login_title(self, text):
        self.assert_title(text)

    def type_username(self, username):
        self.click(self.css_input_username)
        self.update_text(self.css_input_username, username)

    def type_password(self, password):
        self.click(self.css_input_password)
        self.update_text(self.css_input_password, password)

    def click_login_button(self):
        self.click(self.css_login_button)

    def login(self, username, password):
        self.type_username(username)
        self.type_password(password)
        self.click_login_button()

    def forget_password_link(self):
        self.click(self.css_forget_password_link)

    def sign_up_link(self):
        self.click(self.css_sign_up_link)

    def terms_conditions_link(self):
        self.click(self.css_terms_conditions_link)

    def privacy_policy_link(self):
        self.click(self.css_privacy_policy_link)

    def open_login_page(self, page_name):
        self.open(page_name)

    def login_fail_message(self, message):
        self.assert_text(message, self.css_message)
