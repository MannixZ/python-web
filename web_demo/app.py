from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def index():
    users = ['666', 777, 888]
    return render_template('index.html', title='test', data_list=users)


if __name__ == '__main__':
    app.run()
