import xlrd


class aaa:
    bbb = []
    wd = xlrd.open_workbook(filename='测试用例.xlsx', encoding_override=True)
    st = wd.sheet_by_index(0)
    rows = st.nrows
    row = st.row_values(0)[:3]
    for i in range(1, rows):
        row1 = (st.row_values(i)[:3])  # 提取表格内除标题外的所有行的前三项的值
        b = (dict(zip(row, row1)))  # 将键和值压缩成为一个字典
        bbb.append(b)  # 使空的列表内包含上字典
