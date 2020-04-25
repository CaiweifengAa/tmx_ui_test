#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/24 16:09
# @Author  : yangbin.huang
# @Email   : yangbin.huang@things-matrix.com
# @File    : get_data_from_mysql.py

from seleniumbase.core.mysql import DatabaseManager

dm = DatabaseManager("test")

r = dm.query_fetch_one("select name from dmp_admin.flow;", None)

print(r)