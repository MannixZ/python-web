import pymysql

conn = pymysql.connect(host="192.168.31.45", port=3306, user='root', passwd="test1234", charset='utf8', db="unicom")
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

cursor.execute("select * from admin where id > %s", [2, ])
data_list = cursor.fetchone()
print(data_list)

# 4.关闭
cursor.close()
conn.close()