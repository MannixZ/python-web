from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        user = request.form.get("user")
        pwd = request.form.get("pwd")
        sex = request.form.get("sex")
        hobby = request.form.getlist("hobby")
        city = request.form.get("city")
        skill = request.form.getlist("skill")
        more = request.form.get("more")

        return "<html><h1>POST注册成功/h1></html>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        print(user, pwd)
        return "注册成功"


if __name__ == '__main__':
    app.run()
