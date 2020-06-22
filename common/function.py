import time
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from selenium import webdriver
import time
import xlrd
from selenium.webdriver.support.ui import WebDriverWait
from common import function
from common import ReadElement, ReadData
import os
from HTMLreport.img import img_path
import sys


# 封装方法
def scrollTop(self, scrollTopvalue):
    js = "var q=document.body.scrollTop='%s'" % (scrollTopvalue)
    self.dr.execute_script(js)


def set_content(self, text):
    js = "document.getElementById('content_ifr').contentWindow.document.body.innerText = '%s'" % (text)
    print(js)
    self.dr.execute_script(js)


# 登录
def login(self, user_name, password):
    self.dr.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/div/form[1]/div[1]/div/div/input').clear()
    self.dr.find_element_by_xpath(
        '//*[@id="app"]/div/div/div/div/div[2]/div/div/form[1]/div[1]/div/div/input').send_keys(
        user_name)
    time.sleep(1)
    self.dr.find_element_by_xpath(
        '//*[@id="app"]/div/div/div/div/div[2]/div/div/form[1]/div[2]/div/div/input').send_keys(
        password)
    self.dr.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/div/div/form[1]/div[4]/div/button').click()
    # self.by_id('ivu-input ivu-input-default')[1].send_keys(password)
    # self.by_id('wp-submit').click()


def by_id(self, the_id):
    return self.dr.find_element_by_id(the_id)


def by_ccs(self, css):
    return self.dr.find_element_by_css_selector(css)


def by_ptext(self, text):
    return self.dr.find_element_by_partial_link_text(text)


def by_text(self, text):
    return self.dr.find_element_by_link_text(text)


# 方法二：
# def by_css(self, ele_name):
#     return self.dr.find_element_by_css_selector(ReadElement.device_ele(self, ele_name))


def by_name(self, name):
    return self.dr.find_element_by_name(name)


def by_xpath(self, xpath):
    return self.dr.find_element_by_xpath(xpath)


def by_class(self, Classname):
    return self.dr.find_element_by_class_name(Classname)


def by_tagName(self, tagName):
    return self.dr.find_element_by_tag_name(tagName)


def Time(self):
    # T = "日期::" + time.strftime("%Y-%m-%d", time.localtime(time.time()))
    T = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    return T


def success_png(self,  casename):
    # 截图
    # 保存文件时不能使用冒号，修改后则保存成功。 包括 ‘’ : / \ ? * < > | 都不可使用
    return self.dr.get_screenshot_as_file('D:\\workspace\\tmx_ui_test\\screenshot\\%s%s%s.png' % (
    casename, "用例执行success-", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))))


def error_png(self, casename):
    # 截图
    # 保存文件时不能使用冒号，修改后则保存成功。 包括 ‘’ : / \ ? * < > | 都不可使用,注意时间格式
    return self.dr.get_screenshot_as_file(
        'D:\\04_TMXtest\\03_UItest\\TMX_ui_test\\Htmlreport\\img\\%s%s%s.png' % (casename, "用例执行error-", Time(self)))


# 显性等待
def get_ele_times(self, driver, times, func):  # func输入的是查找元素的函数
    return WebDriverWait(driver, times).until(func)
# WebDriverWait(self.dr, 10).until(
    #         lambda driver: self.by_xpath('//div[@class="ivu-table-fixed-body"]/table/tbody/tr/td[2]/div/span').text)
    #     # 通过匿名函数像until传入一个方法，这里千万不能直接传定位的元素对象，必须是方法，这句代码就是循环检测百度搜索框有没有出现，若在10秒内加载出现此元素，自动继续后面的操作，若没有出现，则抛异常
    #


def save_img(self, img_name):
    return self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path.imgPath()), img_name))


def open_tmx(self):
    self.dr = self.driver
    self.open(ReadData.Basic_data(self, "url地址"))
    self.dr.maximize_window()
    # # 设置默认的等待时长
    self.dr.implicitly_wait(15)
    return self.dr
