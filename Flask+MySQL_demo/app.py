import functools
import pymysql
from flask import Flask, render_template, request

app = Flask("__name__")


# conn = pymysql.connect(port=3306, user='root', host="192.168.31.45", passwd='test1234', charset='utf8', db='unicom')
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

def conn_mysql():
    conn = pymysql.connect(port=3306, user='root', host="192.168.31.45", passwd='test1234', charset='utf8',
                           db='unicom')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    return conn, cursor


@app.route("/add/user", methods=["GET", "POST"])
def add_user():
    if request.method == "GET":
        return render_template('add_user.html')
    else:
        conn, cursor = conn_mysql()
        username = request.form.get('username')
        pwd = request.form.get('pwd')
        mobile = request.form.get('mobile')
        sql = "insert into admin(username , pwd, mobile) value (%s, %s, %s)"
        cursor.execute(sql, [username, pwd, mobile])
        conn.commit()
        close_mysql(conn, cursor)
        return render_template('add_user.html')

@app.route("/get/user", methods=["GET"])
def get_user():
    conn, cursor = conn_mysql()
    sql = "select * from admin"
    cursor.execute(sql)
    data_list = cursor.fetchall()
    close_mysql(conn, cursor)
    return render_template('add_user.html', data_list=data_list)

@app.route("/delete/user", methods=["POST"])
def delete_user():
    # if request.method == "post":
    conn, cursor = conn_mysql()
    id = request.form.get('id')
    cursor.execute('delete from admin where id = %s', [id, ])
    conn.commit()
    close_mysql(conn, cursor)
    return render_template('add_user.html')


def close_mysql(conn, cursor):
    cursor.close()
    conn.close()


if __name__ == '__main__':
    app.run(debug=True)
