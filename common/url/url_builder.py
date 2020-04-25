#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/24 15:17
# @Author  : yangbin.huang
# @Email   : yangbin.huang@things-matrix.com
# @File    : url_builder.py

from common.configuration.configuration import get_data_from_config_yaml
from common.content_patterns import urls_content


def url_form(company_name, host_name, env, path):
    if "." in company_name:
        ip = "http://{company_name}/".format(company_name=company_name)
        return ip
    if "test" == env:
        domain = "co"
    else:
        domain = "io"
    if path.startswith("/"):
        path = path[1:]
    url = "https://{company_name}.{host_name}.{domain}/{path}".format(company_name=company_name, host_name=host_name,
                                                              domain=domain, path=path)
    return url


def get_url(path):
    company_name = get_data_from_config_yaml("companyName")
    env = get_data_from_config_yaml("env")
    host_name = urls_content.HOST_NAME
    url = url_form(company_name, host_name, env, path)
    return url
