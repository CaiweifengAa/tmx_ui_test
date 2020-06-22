# coding:utf-8
import unittest
import HTMLTestRunnerChinese
from test_cases.Portal import test_PortalCase
from test_cases.Asset.Devicelist import test_devicelist
from test_cases.test_Setting import test_settings
from BeautifulReport import BeautifulReport

#编写一个函数构造测试用例集：
def test_case_all():
    #方法1：输出测试报告1
    # suite=unittest.TestSuite()
    # #makeSuite()方法，一次性加载一个类文件下所有测试用例到suite中去
    # suite.addTest(unittest.makeSuite(test_01_login.Test1))#添加test_01_login模块下面的类
    # filename = 'D:\\Report\\test_Report22.html'  # 生成报告所存放的路径
    # f=open(filename,'wb')
    # yy = HTMLTestRunnerChinese.HTMLTestRunner(stream=f, title='TMX接口测试报告',
    #                                    description='测试用例执行结果')
    # yy.run(suite)
    #方法2：输出测试报告2
    suite = unittest.TestSuite()
    # #makeSuite()方法，一次性加载一个类文件下所有测试用例到suite中去
    # 添加devicelist模块下面的类
    # suite.addTest(unittest.makeSuite(devicelist.DevicelistCase))
    # 添加TMX_login_case模块下面的类
    suite.addTest(unittest.makeSuite(test_settings.TestSettingsCase))
    # suite.addTest(unittest.makeSuite(devicelist.DevicelistCase))
    # suite.addTest(unittest.makeSuite(settingsCase))
    BeautifulReport(suite).report(filename='TMX_UI_Test_result', description='TMX自动化测试',
                                        log_path='.')  # log_path='.'把report放到当前目录下
if __name__=='__main__':
    test_case_all()