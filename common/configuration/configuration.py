#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/24 14:35
# @Author  : yangbin.huang
# @Email   : yangbin.huang@things-matrix.com
# @File    : configuration.py

import yaml
import os


# os.path.dirname(os.path.realname(__file__))：指的是，获得你刚才所引用的模块 所在的绝对路径，__file__为内置属性
def get_yaml_data(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        content = yaml.safe_load(f)
    return content


def get_data_from_config_yaml(key):
    yaml_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../config.yml")
    yaml_data = get_yaml_data(yaml_file)
    return yaml_data[key]


if __name__ == '__main__':
    print(get_data_from_config_yaml("env"))
