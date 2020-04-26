#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 14:12
# @Author  : yangbin.huang
# @Email   : yangbin.huang@things-matrix.com
# @File    : run.py

import pytest

if __name__ == '__main__':
    pytest.main(['-s', './examples/test_login.py'])
    # pytest.main(["-s"])