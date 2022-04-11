import xlrd


class InitPage:
    success_data = []
    wb = xlrd.open_workbook(filename='HKR.xlsx', encoding_override=True)
    st = wb.sheet_by_index(0)
    rows = st.nrows  # 获取行数
    row = st.row_values(0)[:3]  # 提取表格内的前三个标题
    for i in range(1, rows):
        row1 = (st.row_values(i)[:3])  # 提取表格内除标题外的所有行的前三项的值
        b = (dict(zip(row, row1)))  # 将键和值压缩成为一个字典
        success_data.append(b)  # 使空的列表内包含上字典

    error_data = []
    wb = xlrd.open_workbook(filename='HKR.xlsx', encoding_override=True)
    st = wb.sheet_by_index(1)
    rows = st.nrows  # 获取行数
    row = st.row_values(0)[:3]
    for x in range(1, rows):
        row2 = (st.row_values(x)[:3])
        b = (dict(zip(row, row2)))
        error_data.append(b)
