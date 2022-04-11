# import xlrd
#
#
# class moviedata:
#     data0 = []
#     wb = xlrd.open_workbook(filename="001.xlsx", encoding_override=True)
#     st = wb.sheet_by_index(0)
#     lie = st.nrows
#     key = st.row_values(0)[:11]
#     for i in range(1, lie):
#         data0.append(dict(zip(key, st.row_values(i))))
#     print(data0)
# 1.给出一个string， 倒叙输出该句子，其中的每个单词本身并不会翻转， 比如 "I love China" ->“China love I”
#
# str = i love china
#
# print(format(str))
#
#


str1 = 'i love china'
a = str1.split()
a = a[::-1]
print(" ".join(a))

# 2.将一个数组中的元素，每三个为一组，进行输出[1,2,3,4,5,6] ->[[1,2,3], [4,5,6]]输入一个数组:[1,2,3,4,5,6]输出：[[1,2,3], [4,5,6]]
#
#
# sqlite3
# aa = input("请输入数组：")
# b = aa.split()
# print(b)
# #
#
# 3.实现字符串的indexof方法
str = 'abcdefg'
aa = input()
for i in range(len(str)):
    if str[i] == aa:
        print("您查找的字符串在第", i + 1, "个位置")

