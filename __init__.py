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
admin = 'admin'


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
def write_log(username,operation):
    '''
    写日志函数
    :param username:用户名
    :param operation:用户的操作信息
    :return:
    '''
    w_time = time.strftime('%Y-%m-%d %H%M%S')
    with open(LOG_FILENAME,'a+') as fw:
        log_content = '%s %s %s \n'%(w_time,username,operation)
        fw.write(log_content)

app = Flask(__name__)
app.config['DEBUG'] = True

def is_time(s):
    '''
    这个函数的作用是用来判断价格是否合法，
    :param s:
    :return:
    '''

    s = str(s)
    if s.count('.')==1:#判断小数点个数
        sl = s.split('.')#按照小数点进行分割
        left = sl[0]#小数点前面的
        right = sl[1]#小数点后面的
        if left.startswith('-') and left.count('-')==1 and right.isdigit():
            lleft = left.split('-')[1]#按照-分割，然后取负号后面的数字
            if lleft.isdigit():
                return False
        elif left.isdigit() and right.isdigit():
            #判断是否为正小数
            return True
    elif s.isdigit():
        s = int(s)
        if s!=0:
            return True
    return False

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
'''
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
'''



#查看全部电影函数
@app.route('/base', methods=['get'])
def get_movie_all():

    return render_template('movie_all.html')

#电影发布函数
@app.route('/index', methods=['get'])
def get_movie_publish():

    return render_template('movie_publish.html')

@app.route('/movie_publish', methods=['post'])
def post_movie_publish():

    movie = {}
    logo = {}
    movies = read_file(MOVIES_FILENAME)
    y = 0
    movie['title'] = request.form['title']
    movie['year'] = request.form['year']
    movie['country'] = request.form['country']
    movie['category'] = request.form['category']
    movie['duration'] = request.form['duration']
    movie['director'] = request.form['director']
    movie['profile'] = request.form['profile']
    movie['screenshot'] = ''
    movie['cover'] = ''
    movie['down_load'] = ''
    movie['douban_rating'] = ''
    if movie['title'] != '':
        for x in movies:
            if movie['title'] == x['title']:
                logo['logo'] = u'输入的电影已经存在'
                return render_template('movie_result.html',**logo)
            if not is_time(movie['year']):
                logo['logo'] = u'输入的电影年代不合法'
                return render_template('movie_result.html',**logo)
            y = y + 1
            if (y == len(movies)):
                write_log(admin,'添加了电影信息 电影名【%s】 '%(movie['title']))
                logo['logo'] = u'发布电影成功'
                movies.insert( 0, movie)
                write_file(MOVIES_FILENAME,movies)
                logo['logo'] = u'电影发布成功'

                return render_template('movie_result.html',**logo)
    else:
        logo['logo'] = u'电影名称不能为空'
        return render_template('movie_result.html,**logo')

#电影删除函数
@app.route('/movie_delete', methods=['get'])
def get_movie_delete():

    return render_template('movie_delete.html')

@app.route('/movie_delete', methods=['post'])
def post_movie_delete():

    movies = read_file(MOVIES_FILENAME)
    movie = {}
    logo = {}
    movie['title'] = request.form['title']
    y = 0
    if movie['title'] !='':
        for x in movies:
            if movie['title'] == x['title']:
                del movies[y]
                write_log(admin,'删除了电影信息 电影名【%s】' %movie['title'])
                write_file(MOVIES_FILENAME,movies)
                logo['logo'] = u'删除电影成功'
                return render_template('movie_result.html', **logo)
            if  (y == len(movies)):
                logo['logo'] = u'删除的电影不存在'
                return render_template('movie_result.html', **logo)
            y = y + 1
    else :
        logo['logo'] = u'删除的电影名称不能为空'
        return render_template('movie_result.html', **logo)

@app.route('/movie_list',methods = ['post'])
def get_movie_show_id():

    movie = {}
    movies = read_file(MOVIES_FILENAME)  # 获取电影信息
    x = request.form['id'].encode("utf-8")
    x = int(x)
    movie = movies[x]

    return render_template('movie_show.html', **movie)

@app.route('/base',methods=['post'])
#电影查询函数
def get_movie():

    movie = {}
    logo = {}
    movies = read_file(MOVIES_FILENAME)  # 获取电影信息
    y = 0
    movie['title'] = request.form['q']
    if movie['title'] != '':
        for x in movies:
            if movie['title'] == x['title']:
                movie = movies[y]
                return render_template('movie_show.html', **movie)
            y = y + 1
            if (y == len(movies) ):
                logo['logo'] = u'输入的电影不存在'
                return render_template('movie_result.html', **logo)
    else:
        logo['logo'] = u'输入的电影名称不能为空'
        return render_template('movie_result.html', **logo)


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
                write_log(user['username'], '登录成功！')
                #登录成功
                return render_template('index.html', **user)
            if (n == len(users)):
                logo['logo'] = u'用户名或密码错误'
                return render_template('movie_result.html', **logo)
    else:
        logo['logo'] = u'用户名或密码不能为空'
        return render_template('movie_result.html', **logo)

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
                return render_template('movie_result.html', **logo)
                break
            if (n == len(users)):
                write_log(user['username'], '注册成功！')
                logo['logo'] = u'注册成功'
                users.append(user)
                write_file(USER_FILENAME, users)
                return render_template('movie_result.html', **logo)

    else:
        logo['logo'] = u'用户名或密码不能为空'
        return render_template('movie_result.html', **logo)


if __name__ == '__main__':
    app.run(host='127.0.0.1')