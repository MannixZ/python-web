import pymysql

# 1.连接MySql
conn = pymysql.connect(host="192.168.31.45", port=3306, user='root', passwd="test1234", charset='utf8', db="unicom")
# 2.创建游标
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 3.发送指令
# 3.1 数据插入1
# cursor.execute("insert into admin(username, pwd, mobile) values ('haha', '123', '2131232367')")
# 3.2 数据插入2
# sql = "insert into admin(username, pwd, mobile) values (%s, %s, %s)"
# cursor.execute(sql, ['xixi', 456, '231234566123'])
# 3.3 数据插入3
sql = "insert into admin(username, pwd, mobile) values (%(n1)s, %(n2)s, %(n3)s)"
cursor.execute(sql, {"n1":'张三', "n2": '123123', 'n3':"asdd"})

conn.commit()

# 4.关闭
cursor.close()
conn.close()