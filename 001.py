# 1.完成衣服销售数据的统计和分析
# 1.1计算总销售额
# 1.2计算平均每日销售数量
# 1.3 计算每个种类月销售量占比
import xlrd

wd = xlrd.open_workbook(filename='2020年每个月的销售情况.xlsx', encoding_override=True)


def total():
    x = 0
    for q in range(12):
        st = wd.sheet_by_index(q)
        cold = st.col_values(2, 1)
        cold1 = st.col_values(4, 1)
        for j in range(len(cold)):
            y = cold[j] * cold1[j]
            x += y
    return print('%.0f' % x)


def average():
    z = 0
    y = 0
    x = 0
    o = 0
    for q in range(12):
        st = wd.sheet_by_index(q)
        cold = st.col_values(4, 1)
        # x=sum(cold)
        # z=x / len(cold)
        # y=y+z
        for i in range(len(cold)):
            x = cold[i] + o
            y = x / len(cold)
            z += y
    print(round(z / 12))


def ratio():
    for q in range(12):
        st = wd.sheet_by_index(q)
        s1 = set(st.col_values(1, 1))
        t1 = list(s1)
        for i in t1:
            num = 0
            flag = 0
            for j in st.col_values(1, 1):
                flag += 1
                if i == j:
                    num += st.cell_value(flag, 4)
            print(i, '的', q + 1, '月销量占比：{:.2%}'.format(num / (sum(st.col_values(4, 1)))))
        print()
    '''
    x=0
    y=0
    z=0
    yf=['羽绒服','牛仔裤','风衣','皮草','T血','马甲','小西装','皮衣','卫衣','棉衣','铅笔裤','休闲裤',]
    for q in range(12):
        x = 0
        st = wd.sheet_by_index(q)
        cold = st.col_values(1, 1)
        cold1 = st.col_values(4, 1)
        for j in range(len(yf)):

            for i in range(len(cold)):
                z += cold1[i]
                if yf[j] == cold[i]:
                    x+=cold1[i]
                    y=x/z*100
            print(q+1,'月',yf[j],'%.2f%%'%y)
'''


q = int(input('num'))
if q == 1:
    print('总销售额：')
    total()
if q == 2:
    average()
if q == 3:
    ratio()