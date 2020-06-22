# coding: utf-8
import unittest
from selenium import webdriver
import time
import selenium.webdriver.support.ui
from selenium.webdriver.support.ui import Select  # 导入列表操作模块Select一定大写
from parameterized import parameterized
import pytest
from common import ReadData, function, ReadElement
from selenium import webdriver
import time
from seleniumbase import BaseCase
import sys
import os
from BeautifulReport import BeautifulReport
from HTMLreport.img import img_path
from selenium.webdriver.common.action_chains import ActionChains

class TestSettingsCase(BaseCase):
    def save_img(self, img_name):
        self.dr.get_screenshot_as_file(
            '{}/{}.png'.format(os.path.abspath(img_path.imgPath()), img_name))
    # 保证用例能独立运行
    def setUp(self, masterqa_mode=False):
        super(TestSettingsCase, self).setUp()
        # super(TestPortalCase, self) 首先找到TestPortalCase 的父类（就是类 BaseCase），然后把类 TestPortalCase  的对象转换为类 BaseCase的对象
        function.open_tmx(self)
        self.dr = self.driver
        try:
            function.login(self, ReadData.Basic_data(self, "TMX用户名"), ReadData.Basic_data(self, "TMX密码"))
            time.sleep(1)
        except:
            print("登录失败")

    @pytest.mark.setting
    @BeautifulReport.add_test_img('test_001_General_setting_Language')
    #错误示范：
    def test_001_General_setting_Language(self):
        '''General settings语言设置,英文切换为中文'''
        try:
            function.by_ccs(self, ReadElement.setting(self, "settings图标")).click()
            time.sleep(0.5)
            self.dr.execute_script(ReadElement.setting(self, "Generalsettings")).click()
            time.sleep(0.5)
            self.dr.execute_script(ReadElement.setting(self, "Edit按钮")).click()
            time.sleep(0.5)
            self.dr.execute_script(ReadElement.setting(self, "语言下拉列表")).click()
            time.sleep(0.5)
            self.dr.execute_script(ReadElement.setting(self, "中文简体")).click()
            self.dr.implicitly_wait(10)
            self.dr.execute_script(ReadElement.setting(self, "save按钮")).click()
            time.sleep(0.5)
            self.assertEqual(self.dr.execute_script(ReadElement.setting(self, "长度单位")).text, "1公制")
        except:
            print(self.dr.execute_script(ReadElement.setting(self, "长度单位")).text)
            function.save_img(self, sys._getframe().f_code.co_name)
            self.assertEqual(self.dr.execute_script(ReadElement.setting(self, "长度单位")).text, "1公制")

    @pytest.mark.setting
    @BeautifulReport.add_test_img('test_002_General_setting_Language')
    def test_002_General_setting_Language(self):
        '''General settings语言设置,中切换为英文'''
        try:
            function.by_ccs(self, ReadElement.setting(self, "settings图标")).click()
            time.sleep(0.5)
            self.dr.execute_script(ReadElement.setting(self, "Generalsettings")).click()
            time.sleep(0.5)
            self.dr.execute_script(ReadElement.setting(self, "Edit按钮")).click()
            time.sleep(0.5)
            self.dr.execute_script(ReadElement.setting(self, "语言下拉列表")).click()
            time.sleep(0.5)
            self.dr.execute_script(ReadElement.setting(self, "选择English")).click()
            self.dr.implicitly_wait(10)
            self.dr.execute_script(ReadElement.setting(self, "save按钮")).click()
            self.sleep(1)
            self.assertEqual(self.dr.execute_script(ReadElement.setting(self, "长度单位")).text, "Metric")
        except:
            print(self.dr.execute_script(ReadElement.setting(self, "长度单位")).text)
            function.save_img(self, sys._getframe().f_code.co_name)
            self.assertEqual(self.dr.execute_script(ReadElement.setting(self, "长度单位")).text, "Metric")

    @pytest.mark.setting
    @BeautifulReport.add_test_img('test_003_General_setting_timezone')
    def test_003_General_setting_timezone(self):
        '''General settings手动设置纽约时区，并还原自动时区'''
        try:
            function.by_ccs(self, ReadElement.setting(self, "settings图标")).click()
            time.sleep(0.5)
            self.dr.execute_script(ReadElement.setting(self, "Generalsettings")).click()
            time.sleep(0.5)
            self.dr.execute_script(ReadElement.setting(self, "Edit按钮")).click()
            time.sleep(0.5)
            function.by_ccs(self, ReadElement.setting(self, "自动时区关闭")).click()
            self.dr.implicitly_wait(10)
            function.by_ccs(self, ReadElement.setting(self, "时区输入框")).click()
            time.sleep(1)
            self.dr.execute_script(ReadElement.setting(self, "NEWYORK时区")).click()
            time.sleep(2)
            self.dr.implicitly_wait(10)
            self.dr.execute_script(ReadElement.setting(self, "save按钮")).click()
            time.sleep(1)
            self.assertEqual(function.by_ccs(self, ReadElement.setting(self, "Time zone")).text, "America/New_York")
            self.assertEqual(function.by_ccs(self, ReadElement.setting(self, "时区点")).text, "GMT -04:00")
            self.dr.execute_script(ReadElement.setting(self, "Edit按钮")).click()
            time.sleep(0.5)
            function.by_ccs(self, ReadElement.setting(self, "自动时区开启")).click()
            self.dr.implicitly_wait(10)
            self.dr.execute_script(ReadElement.setting(self, "save按钮")).click()
            time.sleep(1)
        except:
            print(function.by_ccs(self, ReadElement.setting(self, "Time zone")).text)
            print(function.by_ccs(self, ReadElement.setting(self, "时区点")).text)
            function.save_img(self, sys._getframe().f_code.co_name)
            self.assertEqual(function.by_ccs(self, ReadElement.setting(self, "Time zone")).text, "America/New_York")
            self.assertEqual(function.by_ccs(self, ReadElement.setting(self, "时区点")).text, "GMT -04:00")

    @pytest.mark.setting
    @BeautifulReport.add_test_img('test_004_General_setting_timezone')
    def test_004_General_setting_timezone(self):
        '''General settings设置自动时区+重置设置'''
        try:
            function.by_ccs(self, ReadElement.setting(self, "settings图标")).click()
            time.sleep(0.5)
            self.dr.execute_script(ReadElement.setting(self, "Generalsettings")).click()
            time.sleep(0.5)
            self.dr.execute_script(ReadElement.setting(self, "Edit按钮")).click()
            time.sleep(0.5)
            function.by_ccs(self, ReadElement.setting(self, "自动时区关闭")).click()
            self.dr.implicitly_wait(10)
            function.by_ccs(self, ReadElement.setting(self, "时区输入框")).click()
            time.sleep(2)
            self.dr.execute_script(ReadElement.setting(self, "NEWYORK时区")).click()
            time.sleep(1)
            self.dr.implicitly_wait(10)
            self.dr.execute_script(ReadElement.setting(self, "save按钮")).click()
            time.sleep(0.5)
            self.dr.execute_script(ReadElement.setting(self, "Restore default")).click()
            time.sleep(1)
            self.assertEqual(function.by_ccs(self, ReadElement.setting(self, "Restore提示语")).text,
                             "Restored to company default settings")
            print("Restore提示语："+function.by_ccs(self, ReadElement.setting(self, "Restore提示语")).text)
            self.assertEqual(function.by_ccs(self, ReadElement.setting(self, "Time zone")).text, "Asia/Shanghai")
            self.assertEqual(function.by_ccs(self, ReadElement.setting(self, "时区点")).text, "GMT +08:00")
            self.dr.execute_script(ReadElement.setting(self, "Edit按钮")).click()
            self.dr.implicitly_wait(10)
            self.dr.execute_script(ReadElement.setting(self, "save按钮")).click()
            time.sleep(0.5)
        except:
            print(function.by_ccs(self, ReadElement.setting(self, "Time zone")).text)
            print(function.by_ccs(self, ReadElement.setting(self, "时区点")).text)
            function.save_img(self, sys._getframe().f_code.co_name)
            self.assertEqual(function.by_ccs(self, ReadElement.setting(self, "Restore提示语")).text,
                             "Restored to company default settings")
            self.assertEqual(function.by_ccs(self, ReadElement.setting(self, "Time zone")).text, "Asia/Shanghai")
            self.assertEqual(function.by_ccs(self, ReadElement.setting(self, "时区点")).text, "GMT +08:00")

    @pytest.mark.setting
    @BeautifulReport.add_test_img('test_005_General_setting_baidu_map')
    def test_005_General_setting_baidu_map(self):
        '''General settings设置百度地图'''
        try:
            function.by_ccs(self, ReadElement.setting(self, "settings图标")).click()
            time.sleep(1)
            self.dr.execute_script(ReadElement.setting(self, "Generalsettings")).click()
            time.sleep(0.5)
            self.dr.execute_script(ReadElement.setting(self, "Edit按钮")).click()
            time.sleep(0.5)
            self.dr.execute_script(ReadElement.setting(self, "下拉选择MAP")).click()
            time.sleep(0.5)
            self.dr.implicitly_wait(10)
            function.by_ccs(self, ReadElement.setting(self, "选择百度地图")).click()
            self.dr.implicitly_wait(10)
            self.dr.execute_script(ReadElement.setting(self, "save按钮")).click()
            time.sleep(0.5)
            print(self.dr.execute_script(ReadElement.setting(self, "断言当前地图")))
            time.sleep(0.5)
            self.assertEqual(self.dr.execute_script(ReadElement.setting(self, "断言当前地图")),
                             "Baidu Map")
        except:
            function.save_img(self, sys._getframe().f_code.co_name)
            assert self.dr.execute_script(ReadElement.setting(self, "断言当前地图")) == "Baidu Map"

    @pytest.mark.setting
    @BeautifulReport.add_test_img('test_006_General_setting_googlemap')
    def test_006_General_setting_googlemap(self):
        '''General settings设置谷歌地图'''
        try:
            function.by_ccs(self, ReadElement.setting(self, "settings图标")).click()
            time.sleep(1)
            self.dr.execute_script(ReadElement.setting(self, "Generalsettings")).click()
            time.sleep(0.5)
            self.dr.execute_script(ReadElement.setting(self, "Edit按钮")).click()
            time.sleep(0.5)
            self.dr.execute_script(ReadElement.setting(self, "下拉选择MAP")).click()
            time.sleep(0.5)
            self.dr.implicitly_wait(10)
            function.by_ccs(self, ReadElement.setting(self, "选择谷歌地图")).click()
            self.dr.implicitly_wait(10)
            self.dr.execute_script(ReadElement.setting(self, "save按钮")).click()
            time.sleep(0.5)
            print(self.dr.execute_script(ReadElement.setting(self, "断言当前地图")))
            time.sleep(0.5)
            self.assertEqual(self.dr.execute_script(ReadElement.setting(self, "断言当前地图")),
                             "Google Map")
        except:
            function.save_img(self, sys._getframe().f_code.co_name)
            assert self.dr.execute_script(ReadElement.setting(self, "断言当前地图")) == "Google Map"

    @pytest.mark.setting
    @BeautifulReport.add_test_img('test_007_General_setting_Weightunit')
    def test_007_General_setting_Weightunit(self):
        '''General settings设置Weight unit为Imperial'''
        try:
            function.by_ccs(self, ReadElement.setting(self, "settings图标")).click()
            time.sleep(1)
            self.dr.execute_script(ReadElement.setting(self, "Generalsettings")).click()
            time.sleep(0.5)
            self.dr.execute_script(ReadElement.setting(self, "Edit按钮")).click()
            time.sleep(0.5)
            self.dr.execute_script(ReadElement.setting(self, "WeightImperial")).click()
            self.dr.implicitly_wait(10)
            self.dr.execute_script(ReadElement.setting(self, "save按钮")).click()
            time.sleep(0.5)
            print(self.dr.execute_script(ReadElement.setting(self, "Weightunit单位")))
            time.sleep(0.5)
            self.assertEqual(self.dr.execute_script(ReadElement.setting(self, "Weightunit单位")),
                             "Imperial")
        except:
            function.save_img(self, sys._getframe().f_code.co_name)
            assert self.dr.execute_script(ReadElement.setting(self, "Weightunit单位")) == "Imperial"

    @pytest.mark.setting
    @BeautifulReport.add_test_img('test_008_General_setting_Weightunit')
    def test_008_General_setting_Weightunit(self):
        '''General settings设置Weight unit为Metric'''
        try:
            function.by_ccs(self, ReadElement.setting(self, "settings图标")).click()
            time.sleep(1)
            self.dr.execute_script(ReadElement.setting(self, "Generalsettings")).click()
            time.sleep(0.5)
            self.dr.execute_script(ReadElement.setting(self, "Edit按钮")).click()
            time.sleep(0.5)
            self.dr.execute_script(ReadElement.setting(self, "WeightMetric")).click()
            self.dr.implicitly_wait(10)
            time.sleep(2)
            self.dr.execute_script(ReadElement.setting(self, "save按钮")).click()
            time.sleep(0.5)
            print(self.dr.execute_script(ReadElement.setting(self, "Weightunit单位")))
            time.sleep(0.5)
        except:
            function.save_img(self, sys._getframe().f_code.co_name)
            assert self.dr.execute_script(ReadElement.setting(self, "Weightunit单位")) == "Metric"

    @pytest.mark.setting
    @BeautifulReport.add_test_img('test_009_General_setting_Only_admin_active')
    def test_009_General_setting_Only_admin_active(self):
        '''admin用户设置GeneralSetting时仅该用户生效该设置'''
        try:
            function.by_ccs(self, ReadElement.setting(self, "settings图标")).click()
            time.sleep(1)
            self.dr.execute_script(ReadElement.setting(self, "Generalsettings")).click()
            time.sleep(0.5)
            self.dr.execute_script(ReadElement.setting(self, "Edit按钮")).click()
            time.sleep(0.5)
            self.dr.execute_script(ReadElement.setting(self, "WeightImperial")).click()
            self.dr.implicitly_wait(10)
            time.sleep(2)
            self.dr.execute_script(ReadElement.setting(self, "save按钮")).click()
            time.sleep(0.5)
            print(self.dr.execute_script(ReadElement.setting(self, "Weightunit单位")))
            assert self.dr.execute_script(ReadElement.setting(self, "Weightunit单位")) == "Imperial"
            time.sleep(0.5)
            self.click(ReadElement.setting(self, "用户登陆标识"))
            self.click(ReadElement.setting(self, "退出登陆"))
            function.login(self, ReadData.Basic_data(self, "TMXuser用户"), ReadData.Basic_data(self, "TMXuser密码"))
            time.sleep(1)
            print(self.execute_script(ReadElement.setting(self, "用户登陆标识TEXT")))
            self.assertEqual(self.execute_script(ReadElement.setting(self, "用户登陆标识TEXT")), "CW")
            function.by_ccs(self, ReadElement.setting(self, "settings图标")).click()
            time.sleep(1)
            self.dr.execute_script(ReadElement.setting(self, "Generalsettings")).click()
            assert self.dr.execute_script(ReadElement.setting(self, "Weightunit单位")) == "Metric"
        except:
            function.save_img(self, sys._getframe().f_code.co_name)
            assert self.dr.execute_script(ReadElement.setting(self, "Weightunit单位")) == "Metric"
    @pytest.mark.setting
    @BeautifulReport.add_test_img('test_010_General_setting_Only_user_active')
    def test_010_General_setting_Only_user_active(self):
        '''user用户设置GeneralSetting时仅该用户生效该设置'''
        try:
            function.by_ccs(self, ReadElement.setting(self, "settings图标")).click()
            time.sleep(1)
            self.dr.execute_script(ReadElement.setting(self, "Generalsettings")).click()
            time.sleep(0.5)
            print(self.dr.execute_script(ReadElement.setting(self, "断言当前地图")))
            time.sleep(0.5)
            self.assertEqual(self.dr.execute_script(ReadElement.setting(self, "断言当前地图")),
                             "Google Map")
            time.sleep(0.5)
            self.click(ReadElement.setting(self, "用户登陆标识"))
            self.click(ReadElement.setting(self, "退出登陆"))
            function.login(self, ReadData.Basic_data(self, "TMXuser用户"), ReadData.Basic_data(self, "TMXuser密码"))
            time.sleep(1)
            print(self.execute_script(ReadElement.setting(self, "用户登陆标识TEXT")))
            self.assertEqual(self.execute_script(ReadElement.setting(self, "用户登陆标识TEXT")), "CW")
            time.sleep(1)
            function.by_ccs(self, ReadElement.setting(self, "settings图标")).click()
            time.sleep(1)
            self.click(ReadElement.setting(self, "user用户Edit按钮"))
            time.sleep(0.5)
            self.dr.execute_script(ReadElement.setting(self, "下拉选择MAP")).click()
            time.sleep(0.5)
            self.dr.implicitly_wait(10)
            function.by_ccs(self, ReadElement.setting(self, "选择百度地图")).click()
            self.dr.execute_script(ReadElement.setting(self, "save按钮")).click()
            time.sleep(0.5)
            print(self.dr.execute_script(ReadElement.setting(self, "断言当前地图")))
            time.sleep(0.5)
            self.assertEqual(self.dr.execute_script(ReadElement.setting(self, "断言当前地图")),
                             "Baidu Map")
        except:
            function.save_img(self, sys._getframe().f_code.co_name)
            self.assertEqual(self.dr.execute_script(ReadElement.setting(self, "断言当前地图")),
                             "Baidu Map")

    @pytest.mark.setting
    @BeautifulReport.add_test_img('test_011_General_setting_Dashboard_Device_Management')
    def test_011_General_setting_Dashboard_Device_Management(self):
        '''设置Dashboard Setting-Device Management检查'''
        try:
            function.by_ccs(self, ReadElement.setting(self, "settings图标")).click()
            time.sleep(1)
            self.dr.execute_script(ReadElement.setting(self, "Generalsettings")).click()
            time.sleep(0.5)
            self.dr.execute_script(ReadElement.setting(self, "Edit按钮")).click()
            time.sleep(1)
            self.dr.execute_script(ReadElement.setting(self, "选择Management仪表盘")).click()
            time.sleep(1)
            self.click(ReadElement.setting(self, "选择group仪表盘"))
            time.sleep(1)
            self.dr.execute_script(ReadElement.setting(self, "save按钮")).click()
            time.sleep(1)
            self.click(ReadElement.setting(self, "Asset下拉操作"))
            time.sleep(0.5)
            self.click_xpath(ReadElement.setting(self, "DeviceManagement"))
            self.sleep(0.5)
            self.dr.execute_script(ReadElement.setting(self, "点击group")).click()
            self.sleep(0.5)
            self.click(ReadElement.setting(self, "点击ManagementDashboard"))
            self.sleep(2)
            self.refresh()
            self.click(ReadElement.setting(self, "点击ManagementDashboard"))
            self.sleep(1)
            self.click('.dashboard-box')
            self.sleep(1)
            self.dr.execute_script(ReadElement.setting(self, "滑动滚动条"))
            self.sleep(1)
            print(self.dr.execute_script(ReadElement.setting(self, "断言group仪表盘最后一个的名称")))
            self.assertEqual(self.dr.execute_script(ReadElement.setting(self, "断言group仪表盘最后一个的名称")), 'pie')
        except:
            function.save_img(self, sys._getframe().f_code.co_name)
            self.assertEqual(self.dr.execute_script(ReadElement.setting(self, "断言group仪表盘最后一个的名称")), 'pie')


    # @classmethod
    def tearDown(self):  # 每个用例执行之后
        self.T = "用例执行完成时间:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        print(self.T)
        self.dr.quit()

if __name__ == '__main__':
    pytest.main(["-v", "test_settings.py --demo_mode"])
    # unittest.main()
