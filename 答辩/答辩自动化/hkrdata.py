import xlrd


class HkrData:
    data1 = []
    wb = xlrd.open_workbook(filename="测试用例.xlsx", encoding_override=True)
    st = wb.sheet_by_index(0)
    row = st.nrows
    rows = st.row_values(0)[:3]
    for i in range(1, row):
        row1 = st.row_values(i)[:3]
        data1.append(dict(zip(rows, row1)))
