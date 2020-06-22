import yaml
import os
#获取元素表格路径
# os.path.realpath(__file__)获取当前执行脚本的绝对路径 #D:\workspace\ui_test\common\configuration\configuration.py
# os.path.dirname()：去掉脚本的文件名，返回目录。
# os.path.dirname(os.path.realname(__file__))：指的是，该语句所在py文件的绝对路径，__file__为内置属性。
# os.path.join()函数：连接两个或更多的路径名组件
# yaml_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../config.yml")#这是两个点“..”，也就是上级目录的表示方法../../上上级
# D:\workspace\ui_test\common\configuration\../../config.yml
# 1.如果各组件名首字母不包含’/’，则函数会自动加上
# 2.如果有一个组件是一个绝对路径，则在它之前的所有组件均会被舍弃
# 3.如果最后一个组件为空，则生成的路径以一个’/’分隔符结尾
def filePath(filename):
    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)
    # print(file)
    # print(os.path.dirname(os.path.realpath(__file__)))
    return file

if __name__ == '__main__':
    # 传入建打印值

    print(filePath("uidata.xlsx"))