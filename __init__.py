#encoding: utf-8

from flask import *
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
PRODUCT_FILENAME = 'movies.txt'
#常量，存的是电影信息的文件名
USER_FILENAME = 'user.txt'
#常量，存的是存储用户信息的文件名

def read_file(filename):
    '''
    用来读取文件内容，返回一个字典
    :param filename: 文件名
    :return: 文件N内容的字典
    :
    '''
    with open(filename,'a+') as fr:
        fr.seek(0)    #2从末尾开始
        content = fr.read()
        print content
        if len(content):#这里判断文件内容是否为空的，如果不为0的话就为是真
           return eval(content)
        return []

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    context = {
        'username': u'dddd',
        'gender': u'man',
        'age': 18
    }
    return render_template('index.html',**context)

@app.route('/form', methods=['post'])
def submit_form():

    a = {}
    a['name'] = request.form['name']
    a['nickname'] = request.form['nickname']
    a['birthday'] = request.form['birthday']
    return render_template('form2.html', **a)

@app.route('/form', methods=['get'])
def get_form():
    return render_template('form.html')

@app.route('/movie_show', methods=['get'])
def get_movie_show():

    movies = read_file(PRODUCT_FILENAME)  # 获取电影信息
    movie = movies[0]

    return render_template('movie_show.html',**movie)

@app.route('/login', methods=['get'])
def get_login():
    return render_template('login.html')

@app.route('/login', methods=['post'])
def submit_login():
    users = read_file(USER_FILENAME)
    user = {}
    logo = {}
    n = 0
    user['username'] = request.form['username']
    user['password'] = request.form['password']
    if user['username'] != '' and user['password'] != '':
        for u in users:
            n = n + 1
            if user['username'] == u['username'] and user['password'] == u['password']:
                #登录成功
                return render_template('movie_list.html', **user)
                break
            if (n == len(users)):
                logo['logo'] = u'用户名或密码错误'
                return render_template('login_result.html', **logo)
    else:
        logo['logo'] = u'用户名或密码不能为空'
        return render_template('login_result.html', **logo)


if __name__ == '__main__':
    app.run(host='127.0.0.1')