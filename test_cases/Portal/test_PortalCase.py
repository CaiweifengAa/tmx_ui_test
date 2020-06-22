# -*- coding: utf-8 -*-

from parameterized import parameterized
import pytest
from common import ReadData, function, ReadElement
from selenium import webdriver
import time
from seleniumbase import BaseCase


class TestPortalCase(BaseCase):
    def setUp(self, masterqa_mode=False):
        super(TestPortalCase, self).setUp()
        # super(TestPortalCase, self) 首先找到TestPortalCase 的父类（就是类 BaseCase），然后把类 TestPortalCase  的对象转换为类 BaseCase的对象
        # print("setup_method(self):在每个方法之前执行")
        function.open_tmx(self)
        self.dr = self.driver

    # 登陆成功用例
    @pytest.mark.login_success
    def test_1_login(self):
        '''输入正确的用户名，密码，登陆成功'''
        # function.open_tmx(self)
        # self.dr = self.driver
        try:
            function.login(self, ReadData.Basic_data(self, "TMX用户名"), ReadData.Basic_data(self, "TMX密码"))
            time.sleep(1)
            # 断言是否登录成功
            self.assertEqual(self.dr.find_element_by_xpath(ReadElement.Portal_ele(self, "Asset定位")).text,
                             "Asset")
            print("登录成功")
        except:
            print("登录失败")
            # 截图
            function.error_png(self, 'test_1_login')
            self.assertEqual(self.dr.find_element_by_xpath(ReadElement.Portal_ele(self, "Asset定位")).text,
                             "Asset")

    # 登陆失败用例
    # @pytest.mark.parametrize('user_name,password', [("admin", "123456")])
    # @parameterized.expand参数化，有几组参数就执行几个用例
    @parameterized.expand([("admin", "invalid"), ("admin", ""), ("invalid", "TMX2019demo"), ("", "TMX2019demo"), ("", "")])
    @pytest.mark.login_fail
    def test_2_login_fail(self, user_name, password):
        '''输入正确的用户名，错误的密码，登陆失败'''
        try:
            function.login(self, user_name, password)
            time.sleep(3)
            # 断言是否登录成功
            tt = self.dr.find_element_by_css_selector(ReadElement.Portal_ele(self, "Welcome标志定位")).text
            print(tt)
            self.assertEqual(tt, "WELCOME")
            cc = self.dr.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/div/span').text
            print(cc)
        except:
            tt = self.dr.find_element_by_css_selector(ReadElement.Portal_ele(self, "Welcome标志定位")).text
            print(tt)
            # 截图
            function.error_png(self, 'test_2_login_fail')
            self.assertEqual(tt, "WELCOME")

    @pytest.mark.Portal
    def test_3_ForgetPassword(self):
        '''用户名忘记密码'''

        try:
            self.dr.find_element_by_partial_link_text(ReadElement.Portal_ele(self, "忘记密码")).click()
            time.sleep(2)
            # tt=self.dr.find_element_by_css_selector(self,ReadElement.Portal_ele(self,"忘记密码Tip")).text
            # print(tt)
            self.assertEqual(self.dr.find_element_by_css_selector(ReadElement.Portal_ele(self, "忘记密码Tip")).text, "Tip")
            time.sleep(0.5)
            # class组合属性定位class中有空格用点“.”表示
            # self.dr.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div/div/div[3]/button").click()
            self.dr.find_element_by_css_selector(ReadElement.Portal_ele(self, "忘记密码确认按钮")).click()
        except:
            # 截图
            function.error_png(self, ' test_7_ForgetPassword')
            self.assertEqual(self.dr.find_element_by_css_selector(ReadElement.Portal_ele(self, "忘记密码确认按钮")).text, "OK")

    @pytest.mark.Portal
    def test_4_conditions(self):
        '''点击terms&conditions链接'''
        try:
            self.dr.find_element_by_xpath(ReadElement.Portal_ele(self, "conditions链接")).click()
            # self.dr.find_element_by_partial_link_text(ReadElement.Portal_ele(self,"conditions链接")).click()
            time.sleep(2)
            all = self.dr.window_handles
            # 切换到conditions页面用dr.switch_to.window不要用dr.switch_to_window
            # self.dr.switch_to_window(all[-1])
            self.dr.switch_to.window(all[-1])
            print('terms&conditions链接title:' + self.dr.title)
            # 断言
            # self.assertEqual(
            #     self.dr.title, "ThingsMatrix - Terms & Conditions")
        except:
            # 截图
            function.error_png(self, 'test_8_conditions')
            self.assertEqual(
                self.dr.title, "ThingsMatrix - Terms & Conditions")

    @pytest.mark.Portal
    def test_5_Privacy(self):
        '''点击Privacy链接'''
        try:
            self.dr.find_element_by_partial_link_text(ReadElement.Portal_ele(self, "Privacy链接")).click()
            # self.dr.find_element_by_partial_link_text(ReadElement.Portal_ele(self,"conditions链接")).click()
            time.sleep(2)
            all = self.dr.window_handles

            # 切换到conditions页面用dr.switch_to.window不要用dr.switch_to_window
            self.dr.switch_to.window(all[-1])
            print(self.dr.title)
            time.sleep(2)

            # 断言
            self.assertEqual(
                self.dr.title, "ThingsMatrix - Privacy Policy")
        except:
            # 截图
            function.error_png(self, 'test_9_Privacy')
            self.assertEqual(
                self.dr.title, "ThingsMatrix - Privacy Policy")


if __name__ == "__main__":
    pytest.main(["-v", "test_PortalCase.py"])
