# coding: utf-8
import unittest
from selenium import webdriver
import time
import selenium.webdriver.support.ui
from common import function
from seleniumbase import BaseCase
from selenium.webdriver.support.ui import Select  # 导入列表操作模块Select一定大写
from common import ReadElement, ReadData
import pytest
import sys


# 保证用例能独立运行
class TestDevicelistCase(BaseCase):
    def setUp(self, masterqa_mode=False):
        super(TestDevicelistCase, self).setUp()
        # super(TestPortalCase, self) 首先找到TestPortalCase 的父类（就是类 BaseCase），然后把类 TestPortalCase  的对象转换为类 BaseCase的对象
        # print("setup_method(self):在每个方法之前执行")
        function.open_tmx(self)
        self.dr = self.driver
        try:
            function.login(self, ReadData.Basic_data(self, "TMX用户名"), ReadData.Basic_data(self, "TMX密码"))
            time.sleep(1)
            # 断言是否登录成功
            # self.assertEqual(self.dr.find_element_by_xpath(ReadElement.Portal_ele(self, "Asset定位")).text,
            #                  "Asset")
        except:
            print("登录失败")
            # 截图
            # function.error_png(self, 'test_1_login')
            # self.assertEqual(self.dr.find_element_by_xpath(ReadElement.Portal_ele(self, "Asset定位")).text,
            #                  "Asset")

    # 新增设备
    def test_1_add_device(self):
        '''新增设备成功'''
        try:
            function.by_ccs(self, ReadElement.device_ele(self, "Asset下拉操作")).click()
            time.sleep(0.5)
            # self.dr.find_element_by_partial_link_text("Device").click()
            # print(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "点击device")).text)
            function.by_xpath(self, ReadElement.device_ele(self, "点击device")).click()
            self.dr.implicitly_wait(15)
            self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "添加设备按钮")).click()
            time.sleep(1)
            # 通过复制JSpath定位
            self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "点击model")).click()
            time.sleep(1)
            self.dr.find_element_by_xpath(ReadElement.device_ele(self, "选择TMX08model")).click()
            time.sleep(1)
            self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "SN输入框")).send_keys("9786545356768")
            time.sleep(0.5)
            self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "点击GROUP")).click()
            time.sleep(0.3)
            self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "选择GROUP")).click()
            self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "设备提交按钮")).click()
            time.sleep(1)
            # 断言是否新增成功
            tt = self.dr.find_element_by_xpath(ReadElement.device_ele(self, "设备列表第一个sn")).text
            self.assertEqual(tt, '9786545356768')
        except:
            sn = self.dr.find_element_by_xpath(ReadElement.device_ele(self, "设备列表第一个sn")).text
            print(sn)
            function.error_png(self, 'test_1_add_device')
            self.assertEqual(sn, '9786545356768')

    def test_2_add_device(self):
        '''新增设备，列表已经存在的sn失败'''
        try:
            self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "Asset下拉操作")).click()
            time.sleep(0.5)
            # self.dr.find_element_by_partial_link_text("Device").click()
            # print(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "点击device")).text)
            self.dr.find_element_by_xpath(ReadElement.device_ele(self, "点击device")).click()
            self.dr.implicitly_wait(15)
            self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "添加设备按钮")).click()
            time.sleep(1)
            # 通过复制JSpath定位
            self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "点击model")).click()
            time.sleep(1)
            self.dr.find_element_by_xpath(ReadElement.device_ele(self, "选择TMX08model")).click()
            time.sleep(1)
            self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "SN输入框")).send_keys("9786545356768")
            time.sleep(0.5)
            self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "点击GROUP")).click()
            time.sleep(0.3)
            self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "选择GROUP")).click()
            self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "设备提交按钮")).click()
            time.sleep(1)
            # 断言是否新增成功
            tt = self.dr.find_element_by_xpath(ReadElement.device_ele(self, "设备列表第一个sn")).text
            self.assertEqual(tt, '9786545356768')
            S = self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "新增设备SN重复提示")).text
            print(S)
            self.assertEqual(S, '10022:[sn] already exist,Please re-enter')
        except:
            sn = self.dr.find_element_by_xpath(ReadElement.device_ele(self, "设备列表第一个sn")).text
            print(sn)
            function.error_png(self, sys._getframe().f_code.co_name)
            print(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "新增设备SN重复提示")).text)
            self.assertEqual(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "新增设备SN重复提示")).text,
                             '10022:[sn] already exist,Please re-enter')
            self.assertEqual(sn, '9786545356768')

    # 查询设备
    def test_3_query_device(self):
        '''查询设备'''
        try:
            self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "Asset下拉操作")).click()
            time.sleep(0.5)
            # self.dr.find_element_by_partial_link_text("Device").click()
            # print(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "点击device")).text)
            self.dr.find_element_by_xpath(ReadElement.device_ele(self, "点击device")).click()
            self.dr.implicitly_wait(15)
            self.dr.find_element_by_xpath(ReadElement.device_ele(self, "devicelist输入框")).send_keys("9786545356768")
            time.sleep(1)
            self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "查询按钮")).click()
            time.sleep(2)
        except:
            print(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "设备个数")).text)
            function.error_png(self, sys._getframe().f_code.co_name)
            self.assertEqual(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "设备个数")).text,
                             "Total 1 item")

    def test_4_screen_model(self):
        '''通过model筛选设备,并关闭筛选'''
        try:
            self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "Asset下拉操作")).click()
            time.sleep(0.5)
            # self.dr.find_element_by_partial_link_text("Device").click()
            # print(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "点击device")).text)
            self.dr.find_element_by_xpath(ReadElement.device_ele(self, "点击device")).click()
            self.dr.implicitly_wait(15)
            self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "下拉筛选Model")).click()
            time.sleep(1)
            self.dr.find_element_by_xpath(ReadElement.device_ele(self, "选择设备类型")).click()
            time.sleep(2)
            print(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "断言设备类型")).text)
            self.assertEqual(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "断言设备类型")).text,
                             "TMX09")
        except:
            print(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "断言设备类型")).text)
            function.error_png(self, 'test_3_screen_model')
            self.assertEqual(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "断言设备类型")).text,
                             ReadData.Basic_data(self, "断言设备类型"))
        try:
            self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "再次点击筛选Model")).click()
            time.sleep(2)
            self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "关闭筛选Model")).click()
            # self.dr.find_element_by_xpath(ReadElement.device_ele(self, "关闭筛选Model")).click()
            time.sleep(2)
            self.assertEqual(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "下拉筛选Model")).text,
                             "Model")
        except:

            print(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "下拉筛选Model")).text)
            function.error_png(self, sys._getframe().f_code.co_name)
            self.assertEqual(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "下拉筛选Model")).text,
                             "Model")

    def test_5_screen_group(self):
        '''通过group筛选设备,并关闭筛选'''
        try:
            self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "Asset下拉操作")).click()
            time.sleep(0.5)
            # self.dr.find_element_by_partial_link_text("Device").click()
            # print(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "点击device")).text)
            self.dr.find_element_by_xpath(ReadElement.device_ele(self, "点击device")).click()
            self.dr.implicitly_wait(15)
            self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "下拉筛选group")).click()
            time.sleep(2)
            self.dr.find_element_by_xpath(ReadElement.device_ele(self, "选择group类型")).click()
            time.sleep(2)
            print(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "断言group类型")).text)
            self.assertEqual(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "断言group类型")).text,
                             ReadData.Basic_data(self, "断言group类型"))
        except:
            print(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "断言group类型")).text + "fail")
            function.error_png(self, sys._getframe().f_code.co_name)
            self.assertEqual(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "断言group类型")).text,
                             ReadData.Basic_data(self, "断言group类型"))
        try:
            self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "再次点击筛选group")).click()
            time.sleep(2)
            self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "关闭筛选group")).click()
            # self.dr.find_element_by_xpath(ReadElement.device_ele(self, "关闭筛选Model")).click()
            time.sleep(2)
            self.assertEqual(
                self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "下拉筛选group")).text,
                "Group")
        except:

            print(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "下拉筛选group")).text)
        #函数内部获取当前函数名称，用sys._getframe().f_code.co_name方法获取
            function.error_png(self, sys._getframe().f_code.co_name)
            self.assertEqual(
                self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "下拉筛选group")).text,
                "Group")

    def test_6_screen_status(self):
        '''通过status筛选设备,并关闭筛选'''
        # 函数内部获取当前函数名称，用sys._getframe().f_code.co_name方法获取
        #获取类里面方法名称，跟获取函数名称一样sys._getframe().f_code.co_name)
        function.error_png(self, sys._getframe().f_code.co_name)#test_6_screen_status


    def test_7_modify_device(self):
        '''刷新设备列表，并修改设备'''
        try:
            self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "Asset下拉操作")).click()
            time.sleep(0.5)
            # self.dr.find_element_by_partial_link_text("Device").click()
            # print(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "点击device")).text)
            self.dr.find_element_by_xpath(ReadElement.device_ele(self, "点击device")).click()
            self.dr.implicitly_wait(15)
            time.sleep(1)
            self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "设备列表刷新按钮")).click()
            time.sleep(1)
            self.dr.find_element_by_xpath(ReadElement.device_ele(self, "devicelist输入框")).send_keys("9786545356768")
            time.sleep(1)
            self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "查询按钮")).click()
            time.sleep(0.5)
            self.dr.find_element_by_xpath(ReadElement.device_ele(self, "设备列表第一个sn")).click()
            time.sleep(1)
            self.dr.find_element_by_xpath(ReadElement.device_ele(self, "设备列表修改按钮")).click()
            time.sleep(2)
            self.dr.execute_script(ReadElement.device_ele(self, "Sim输入框")).clear()
            self.dr.execute_script(ReadElement.device_ele(self, "Sim输入框")).send_keys("888888888")
            time.sleep(1)
            self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "Description输入框")).send_keys("888888888")
            self.dr.find_element_by_xpath(ReadElement.device_ele(self, "提交按钮")).click()
            time.sleep(1)
            self.assertEqual(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "Sim字段")).text,
                             "888888888")
        except:
            function.error_png(self, sys._getframe().f_code.co_name)
            self.assertEqual(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "Sim字段")).text,
                             "888888888")

    # @classmethod
    def tearDown(self):  # 每个用例执行之后
        # self.T = "用例执行完成时间:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        # print(self.T)
        self.dr.quit()


if __name__ == '__main__':
    pytest.main()
