"""txt文件
excel
冒泡
"""
import xlrd
import openpyxl


# txt = open(file='001.txt', mode='r', encoding='utf-8')
# for i in txt.readlines():
#     print(i)
# txt.close()


# data = openpyxl.load_workbook('002.xlsx')
# s = data["lll"]
# s.cell(1, 1, 1234)
# data.save("002.xlsx")


# a = [2, 1, 3, 5, 7, 8, 2, 6, 3, 5, 7, 8, 2]
# for i in range(0, len(a)):
#     for y in range(0, len(a) - i - 1):
#         if a[y] > a[y + 1]:
#             a[y], a[y + 1] = a[y + 1], a[y]
# print(a)


# l = [3, 4, 5, 7, 8, 9, 93, 1, 2, 5, 7]
# b = 0
# for i in l:
#     if i % 2 != 0:
#         b = b + i
# print(b)


class creature:
    name = "小明"

    def cry(self):
        print(self.name, "在哭 呜呜呜呜呜！")


class creature1(creature):
    age = "18"

    def age1(self):
        print(creature().name, "今年", self.age, "岁啦")


c = creature()
b = creature1()
b.age1()
b.cry()

# b = [2, 3, 5, 2, 1, 9, 10, 5, 6, 3, 4, 1]
# for i in range(0, len(b)):
#     for n in range(0, len(b) - i - 1):
#         if b[n] > b[n + 1]:
#             b[n], b[n + 1] = b[n + 1], b[n]
# print(b)

# list = [1,2,3,4,5,6,7,8,9]
# list2 = []
# print(list[::-1])
#
# for i in range(len(list)):
#     list2.append(list.pop())
# print(list2)


# wj = open(file="001.txt", mode="r", encoding="utf-8")
# mh = wj.readlines()
# print(mh)
# wj.close()

# wd = xlrd.open_workbook(filename="002.xlsx", encoding_override="true")
# sh = wd.sheet_by_name("lll")
# x = sh.row_values(0)
# y = sh.col_values(0)
# cel = sh.cell_value(0, 0)
# print(cel)


# l = [2, 3, 2, 6, 7, 8, 6, 5, 4, 3, 22, 2, 1]
# for i in range(len(l)-1):
#     if l[i] > l[i+1]:
#         l[i], l[i+1] = l[i+1], l[i]
# print(l)
