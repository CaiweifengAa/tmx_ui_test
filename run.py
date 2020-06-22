#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 14:12
# @Author  : yangbin.huang
# @Email   : yangbin.huang@things-matrix.com
# @File    : run.py
# 首先寻找以test_开头或者以_test结尾的测试模块，然后执行模块里面以test_开头或者是以_test结尾的测试代码，这里依据这个要去，编写测试模块
import pytest

if __name__ == '__main__':
    # pytest.main(['-s', './examples/test_login.py'])

    pytest.main(["-s", '--html=D:\\workspace\\tmx_ui_test\\HTMLreport\\report.html', './test_cases/Portal/test_PortalCase.py' , './test_cases/Asset/Devicelist/test_devicelist.py'])
#-s：显示打印内容
# 通过python代码执行pytest
# 1.直接执行pytest.main() 【自动查找当前目录下，以test_开头的文件或者以_test结尾的py文件】
# 2.设置pytest的执行参数 pytest.main(['--html=./report.html','test_login.py'])【执行test_login.py文件，并生成html格式的报告】
# 方式2中，执行参数和插件参数，通过[]进行分割，[]内的多个参数通过‘逗号,’进行分割
#使用到的命令为：pytest -v 就会显示出详细的执行信息
# –html=路径/report.html：生成xml/html格式测试报告（需要先安装pytest-html）
# 如：pytest pytest-demp.py --html-./report.html
