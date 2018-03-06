#encoding: utf-8

from flask import *
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
PRODUCT_FILENAME = 'movies.txt'
#常量，存的是电影信息的文件名

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



if __name__ == '__main__':
    app.run(host='127.0.0.1')