# coding: utf-8
import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select  # 导入列表操作模块Select一定大写
from common import function
from common import ReadElement


class LoginCase(unittest.TestCase):
    @classmethod  # 让用例执行时，只打开一次浏览器
    def setUpClass(self):  # 每个用例执行之前执行
        print('开始执行用例')
        self.dr = webdriver.Chrome()
        self.dr.get('http://10.10.16.213/#/login')
        self.dr.implicitly_wait(15)
        # cls.dr.implicitly_wait(10)  # 在规定时间会自动搜索，超出时间，抛出异常(消耗时间是固定的)
        # 当使用了隐性等待执行测试的时候，如果 WebDriver没有在 DOM中找到元素，将继续等待，超出设定时间后则抛出找不到元素的异常
        # 相当于设置全局的等待，在定位元素时，对所有元素设置超时时间。隐式等待是等页面加载，而不是元素加载！！！（隐式等待就是针对页面的，显式等待是针对元素的。）
        self.dr.maximize_window()
        time.sleep(2)
        # 调用function.login方法’
        try:
            function.login(self,user_name="admin", password="admin")
            time.sleep(1)
            # 断言是否登录成功
            print(self.dr.find_element_by_xpath(ReadElement.Portal_ele(self, "Asset定位")).text)
        except:
            print("登录失败")
            # 截图
            function.error_png(self,'test_1_login')
            self.assertEqual(self.dr.find_element_by_xpath(ReadElement.Portal_ele(self, "Asset定位")).text, "Asset")
            # 新增设备

    def test_1_add_device(self):
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
            tt=self.dr.find_element_by_xpath(ReadElement.device_ele(self, "设备列表第一个sn")).text
            self.assertEqual(tt,'9786545356768')
        except:
            sn = self.dr.find_element_by_xpath(ReadElement.device_ele(self, "设备列表第一个sn")).text
            print(sn)
            function.error_png(self, 'test_1_add_device')
            self.assertEqual(sn, '9786545356768')

    # 查询设备
    def test_2_query_device(self):
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
            time.sleep(0.5)
            print(self.dr.find_element_by_css_selector(".ivu-page-total").text)
            self.assertEqual(self.dr.find_element_by_css_selector(".ivu-page-total").text,"Total 1 item")

        except:
            print(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "设备个数")).text)
            function.error_png(self, 'test_2_query_device')
            self.assertEqual(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "设备个数")).text,
                             "Total 1 item")
    # 筛选设备
    def test_3_add_device(self):
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
            time.sleep(0.5)
            print(self.dr.find_element_by_css_selector(".ivu-page-total").text)
            self.assertEqual(self.dr.find_element_by_css_selector(".ivu-page-total").text, "Total 1 item")

        except:
            print(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "设备个数")).text)
            function.error_png(self, 'test_2_add_device')
            self.assertEqual(self.dr.find_element_by_css_selector(ReadElement.device_ele(self, "设备个数")).text,
                             "Total 1 item")


    #
    # # 删除设备
    # def test_4_del_device(self):
    #     data = "No data yet,please add device first"
    #     self.by_xpath(
    #         '//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div[2]/div/div/div[4]/div[2]/table/tbody/tr[1]/td[2]/div/span').click()
    #     self.by_xpath(
    #         '//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div[1]/form/div[6]/div[4]/div[1]/i').click()
    #     time.sleep(0.5)
    #     self.by_xpath('/html/body/div[20]/div[2]/div/div/div/div/div[3]/button[2]/span').click()
    #     time.sleep(2)
    #     WebDriverWait(self.dr, 10).until(lambda driver: self.by_class('noData-text').text)
    #     # 断言是否删除成功
    #     try:
    #         self.assertEqual(self.by_class('noData-text').text, data)  # No data yet,please add device first是否出现
    #         print("test_4_del_device用例执行成功")
    #     except:
    #         print("test_4_del_device用例执行失败")


    @classmethod
    def tearDownClass(self):  # 每个用例执行之后
        self.T = "用例执行时间:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        print(self.T)
        print('用例执行完成')
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()
