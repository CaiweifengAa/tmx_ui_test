#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 15:37
# @Author  : yangbin.huang
# @Email   : yangbin.huang@things-matrix.com
# @File    : test_login_page.py

from seleniumbase import BaseCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLoginPage(BaseCase):

    def login(self, username="admin", password="TMX2019demo"):
        self.open(url="http://120.79.180.135/")
        # self.assert_title("ThingsMatrix - Login")
        # self.assert_text("WELCOME", "h1.login-title")
        # self.assert_text("Login", "div.ivu-card-head :last-child")
        # self.assert_text("Forget Password?", "div.forget-psw")
        # self.assert_text("Sign Up", "a.f-right")
        # self.assert_text("Terms & Conditions", "a[href='#/tc']")
        # self.assert_text("Privacy Policy", "a[href='#/privacypolicy']")
        # self.assert_text("©2019 - 2020 ThingsMatrix Inc.", "p.inc")
        # self.assert_element("input[placeholder=Username]")
        self.update_text("input[type='text']", username)
        # self.assert_element("input[placeholder=Password]")
        self.update_text("input[type='password']", password)
        self.click("button[type='button']")

        # wait = WebDriverWait(self.driver, 20)
        # wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.custom-content-con span.ivu-avatar-string')))
        # as_js = "return document.querySelector('div.user-avatar-dropdown span.ivu-avatar-string').innerText;"
        # Home_js = "return document.querySelector('div.ivu-breadcrumb span.ivu-breadcrumb-item-link').textContent;"
        # print(self.execute_script(as_js))
        # print(self.execute_script(Home_js))
        # self.wait_for_element('div.user-avatar-dropdown span.ivu-avatar-string')
        self.assert_text("AS", "div.user-avatar-dropdown span.ivu-avatar-string")
        self.assert_text("Home", "div.ivu-breadcrumb span.ivu-breadcrumb-item-link")

    def test_login(self):
        self.login()
        # self.assert_title("ThingsMatrix - Home")
