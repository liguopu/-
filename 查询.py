import pymysql

con = pymysql.connect(host="localhost",user="root",password="root",database="company")

# 创建控制台
cursor = con.cursor()

sql = "select * from t_employees where  sal > 4000"

cursor.execute(sql)


# 提取数据

data = cursor.fetchmany(6)

for i in data:
    print(i)




# 提交到数据库
con.commit()

# 关闭资源
cursor.close()
con.close()