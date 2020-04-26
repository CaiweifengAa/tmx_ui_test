# ui_test: to test thingsmartix website.
# 环境搭建：
* 1、Python：3.5+，pip要升级到最新版本:
```bash
python -m pip install -U pip
```
* 2、git安装,cmd进入工作目录，将代码克隆到本地：git clone https://github.com/thingsmatrix/ui_test
* 3、在pycharm中，打开克隆到本地的项目
* 4、在pycharm中设置项目的解释器，file -> settings -> project -> python inerpreter
* 5、打开pycharm的终端terminal，执行：pip install –r requirements.txt，在执行上述命令前，先确保pip是最新版本
* 6、设置pytest为默认运行器：file -> settings -> tools -> python integrated tools -> testing选择pytest，点击OK
* 7、在pycharm终端中，安装webdriver，seleniumbase install geckodriver，或单独下载webdriver，
并在系统环境变量中设置webdriver的路径，或拷贝到[虚拟环境]\Lib\site-packages\seleniumbase\drivers
* 8、cd到examples文件夹，执行：pytest test_login.py
