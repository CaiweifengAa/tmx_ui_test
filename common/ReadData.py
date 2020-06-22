import xlrd
#获取定位元素，调用ele_value方法，并输入（self，元素名称）
from testdata import uidata_path
#读取Portal表格元素
def Basic_data(self,name):
        self.data = xlrd.open_workbook(uidata_path.filePath("uidata.xlsx"))
        self.table = self.data.sheet_by_name("Basic")
        # # 获取第一行作为key值
        # self.keys = self.table.row_values(0)
        # 获取第一列作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j=1
            for i in range(self.rowNum-1):

                # 从第二行取对应values值
                values = self.table.row_values(j)
                r.append(values)
                j+=1
        #把列表转为字典
        self.dict_data =dict(r)
        self.name = self.dict_data[name]
        return self.name

















# #方法二
# import xlrd
# #获取定位元素，调用ele_value方法，并输入元素名称
# class ReadExcel():
#     def __init__(self, excelPath ="D:\\04_TMXtest\\03_UItest\\TMX_ui_test\\elementdata\\HomeElement.xlsx", sheetName="Home"):
#         self.data = xlrd.open_workbook(excelPath)
#         self.table = self.data.sheet_by_name(sheetName)
#         # # 获取第一行作为key值
#         # self.keys = self.table.row_values(0)
#         # 获取第一列作为key值
#         self.keys = self.table.row_values(0)
#         # 获取总行数
#         self.rowNum = self.table.nrows
#         # 获取总列数
#         self.colNum = self.table.ncols
#
#     def ele_value(self,elename):
#         if self.rowNum <= 1:
#             print("总行数小于1")
#         else:
#             r = []
#             s ={}
#             j=1
#             for i in range(self.rowNum-1):
#
#                 # 从第二行取对应values值
#                 values = self.table.row_values(j)
#                 # print(values)
#                 # for x in range(self.colNum)
#
#                 r.append(values)
#                 j+=1
#         #把列表转为字典
#         dict_data =dict(r)
#         element = dict_data[elename]
#         return element
#
# if __name__ == "__main__":
# # #     filepath = "D:\\04_TMXtest\\03_UItest\\TMX_ui_test\\elementdata\\HomeElement.xlsx"
#     key =  ReadExcel().ele_value("密码输入框")
#     print(key)

#方法3
# import xlrd
#
# class ReadExcel():
#     def __init__(self, excelPath ="D:\\04_TMXtest\\03_UItest\\TMX_ui_test\\elementdata\\HomeElement.xlsx", sheetName="Home"):
#         self.data = xlrd.open_workbook(excelPath)
#         self.table = self.data.sheet_by_name(sheetName)
#         # # 获取第一行作为key值
#         # self.keys = self.table.row_values(0)
#         # 获取第一列作为key值
#         self.keys = self.table.row_values(0)
#         # 获取总行数
#         self.rowNum = self.table.nrows
#         # 获取总列数
#         self.colNum = self.table.ncols
#
#     def list_data(self):
#         if self.rowNum <= 1:
#             print("总行数小于1")
#         else:
#             r = []
#             s ={}
#             j=1
#             for i in range(self.rowNum-1):
#
#                 # 从第二行取对应values值
#                 values = self.table.row_values(j)
#                 # print(values)
#                 # for x in range(self.colNum)
#
#                 r.append(values)
#                 j+=1
#         #把列表转为字典
#         dict_data =dict(r)
#         print(dict_data)
#         return dict_data
#
#
#
#
# if __name__ == "__main__":
#     filepath = "D:\\04_TMXtest\\03_UItest\\TMX_ui_test\\elementdata\\HomeElement.xlsx"
#     data = ReadExcel(filepath)
#     key = data.list_data()
#     print(key["登陆按钮"])