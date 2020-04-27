#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 10:34
# @Author  : yangbin.huang
# @Email   : yangbin.huang@things-matrix.com
# @File    : home_page.py

from seleniumbase import BaseCase


class HomePage(BaseCase):

    def __init__(self, *args, **kwargs):
        super(HomePage, self).__init__(*args, **kwargs)
        self.css_user_badge = "span.ivu-avatar-string"

    def verify_user_badge(self, badge):
        self.assert_text(badge, self.css_user_badge)

    def check_page_title(self, title):
        self.assert_title(title)
