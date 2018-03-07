#encoding: utf-8

from flask import *
import time
import sys
import requests
reload(sys)
sys.setdefaultencoding('utf-8')
MOVIES_FILENAME = 'movies.txt'
#常量，存的是电影信息的文件名
USER_FILENAME = 'user.txt'
#常量，存的是存储用户信息的文件名
LOG_FILENAME = 'movie.log'
#常量，存的是日志文件名


#文件操作
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

def write_file(filename,content):
    '''
    用来读取文件内容，返回一个字典
    :param filename: 文件名
    :return: 文件N内容的字典
    '''
    with open(filename,'a+') as fw:
        fw.seek(0)
        fw.truncate()
        fw.write(str(content))


app = Flask(__name__)
app.config['DEBUG'] = True


#主页相关函数
@app.route('/')
def index():
    context = {
        'username': u'dddd',
        'gender': u'man',
        'age': 18
    }
    return render_template('index.html',**context)


#测试相关函数
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



#电影相关函数
@app.route('/movie_show', methods=['get'])
def get_movie_show():

    movies = read_file(MOVIES_FILENAME)  # 获取电影信息
    movie = movies[0]

    return render_template('movie_show.html',**movie)

@app.route('/movie_show',methods=['get'])
def get_movie_show0():

    movies = read_file(MOVIES_FILENAME)  # 获取电影信息
    movie = movies[0]

    return render_template('movie_show.html', **movie)


@app.route('/movie_list', methods=['get'])
def get_movie_list():
    n = 0
    movies = read_file(MOVIES_FILENAME)  # 获取电影信息
    movie0 = {}
    movie1 = {}
    movie2 = {}
    movie3 = {}
    movie4 = {}
    movie5 = {}
    movie6 = {}
    movie7 = {}
    movie8 = {}
    movie9 = {}

    movie0 = movies[n]
    movie1 = movies[n+1]
    movie2 = movies[n+2]
    movie3 = movies[n+3]
    movie4 = movies[n+4]
    movie5 = movies[n+5]
    movie6 = movies[n+6]
    movie7 = movies[n+7]
    movie8 = movies[n+8]
    movie9 = movies[n+9]

    return render_template('movie_list.html', **locals())

@app.route('/movie_list_2', methods=['get'])
def get_movie_list_2():
    n = 10
    movies = read_file(MOVIES_FILENAME)  # 获取电影信息
    movie0 = {}
    movie1 = {}
    movie2 = {}
    movie3 = {}
    movie4 = {}
    movie5 = {}
    movie6 = {}
    movie7 = {}
    movie8 = {}
    movie9 = {}

    movie0 = movies[n]
    movie1 = movies[n+1]
    movie2 = movies[n+2]
    movie3 = movies[n+3]
    movie4 = movies[n+4]
    movie5 = movies[n+5]
    movie6 = movies[n+6]
    movie7 = movies[n+7]
    movie8 = movies[n+8]
    movie9 = movies[n+9]

    return render_template('movie_list_2.html', **locals())


@app.route('/movie_list_3', methods=['get'])
def get_movie_list_3():
    n = 20
    movies = read_file(MOVIES_FILENAME)  # 获取电影信息
    movie0 = {}
    movie1 = {}
    movie2 = {}
    movie3 = {}
    movie4 = {}
    movie5 = {}
    movie6 = {}
    movie7 = {}
    movie8 = {}
    movie9 = {}

    movie0 = movies[n]
    movie1 = movies[n + 1]
    movie2 = movies[n + 2]
    movie3 = movies[n + 3]
    movie4 = movies[n + 4]
    movie5 = movies[n + 5]
    movie6 = movies[n + 6]
    movie7 = movies[n + 7]
    movie8 = movies[n + 8]
    movie9 = movies[n + 9]

    return render_template('movie_list_3.html', **locals())


@app.route('/movie_list_4', methods=['get'])
def get_movie_list_4():
    n = 30
    movies = read_file(MOVIES_FILENAME)  # 获取电影信息
    movie0 = {}
    movie1 = {}
    movie2 = {}
    movie3 = {}
    movie4 = {}
    movie5 = {}
    movie6 = {}
    movie7 = {}
    movie8 = {}
    movie9 = {}

    movie0 = movies[n]
    movie1 = movies[n + 1]
    movie2 = movies[n + 2]
    movie3 = movies[n + 3]
    movie4 = movies[n + 4]
    movie5 = movies[n + 5]
    movie6 = movies[n + 6]
    movie7 = movies[n + 7]
    movie8 = movies[n + 8]
    movie9 = movies[n + 9]

    return render_template('movie_list_4.html', **locals())


@app.route('/movie_list_5', methods=['get'])
def get_movie_list_5():
    n = 40
    movies = read_file(MOVIES_FILENAME)  # 获取电影信息
    movie0 = {}
    movie1 = {}
    movie2 = {}
    movie3 = {}
    movie4 = {}
    movie5 = {}
    movie6 = {}
    movie7 = {}
    movie8 = {}
    movie9 = {}

    movie0 = movies[n]
    movie1 = movies[n + 1]
    movie2 = movies[n + 2]
    movie3 = movies[n + 3]
    movie4 = movies[n + 4]
    movie5 = movies[n + 5]
    movie6 = movies[n + 6]
    movie7 = movies[n + 7]
    movie8 = movies[n + 8]
    movie9 = movies[n + 9]

    return render_template('movie_list_5.html', **locals())

#用户登录相关函数
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

#用户注册相关函数
@app.route('/register', methods=['get'])
def get_register():
    return render_template('register.html')

@app.route('/register', methods=['post'])
def submit_register():
    users = read_file(USER_FILENAME)
    user = {}
    logo = {}
    n = 0
    user['username'] = request.form['username']
    user['password'] = request.form['password']
    if user['username'] != '' and user['password'] != '':
        for u in users:
            n = n + 1
            if user['username'] == u['username'] :
                #注册失败
                logo['logo'] = u'用户名已经存在'
                return render_template('register_result.html', **logo)
                break
            if (n == len(users)):
                logo['logo'] = u'注册成功'
                users.append(user)
                write_file(USER_FILENAME, users)
                return render_template('register_result.html', **logo)

    else:
        logo['logo'] = u'用户名或密码不能为空'
        return render_template('register_result.html', **logo)


if __name__ == '__main__':
    app.run(host='127.0.0.1')