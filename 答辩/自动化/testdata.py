import xlrd
import pymysql


class testdata:
    # 读取excel表格的方法
    data = []
    wb = xlrd.open_workbook(filename='测试用例.xlsx', encoding_override=True)
    st = wb.sheet_by_index(0)
    rows = st.nrows
    row = st.row_values(0)[:3]
    for i in range(1, rows):
        row1 = (st.row_values(i)[:3])
        b = (dict(zip(row, row1)))
        data.append(b)

    #  读取数据库的方法

    con = pymysql.connect(host='localhost', user='root', password='root', database='hkr')

    # 创建控制台

    cursor = con.cursor()

    # 输入sql语句

    sql = "select * from t_user"

    # 执行sql语句

    cursor.execute(sql)

    # 提取数据,fetchall提取所有,    fetchone 提取第一条,     fetchmany()根据输入的值，决定提取的数据的条数

    data1 = cursor.fetchmany(5)  # 提取数据库里面所有的用户数据给data1

    data2 = []  # 切片出表头里面的username和password，即字典的键

    data3 = []  # 切片出来的表内的所有用户名和密码数据，即字典的值

    data4 = []  # 最终整理好的数据

    for i in range(2, 5, 2):  # i循环两次，值分别为2，4， 其中第一项是起始值，第二项为最大值，但不能等于最大值，第三项为步长
        data2.append(list(cursor.description[i][:1]))  # cursor.description是表头所有的信息，因为i等于2，4，所以读出表头的第2，4项
    data2 = sum(data2, [])  # 使大列表内的小列表合并，即[[1],[2]] = [1,2]

    for x in range(0, len(data1)):  # 循环出所有的用户数据
        data3 = (list(data1[x][2:5:2]))  # 将用户数据切片，得到要用到的用户名和密码
        data4.append(dict(zip(data2, data3)))  # 将得到的表头的第2，4项，与所有的用户数据，压缩成字典的形式，即：{loginname : 1，password : 1}
    print(data4)
    # 提交到数据库

    con.commit()

    # 关闭资源

    cursor.close()
    con.close()
