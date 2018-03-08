# -*- coding: UTF-8 -*-
import time
USER_FILENAME = 'users'
#常量，存的是存储用户信息的文件名
LOG_FILENAME = 'movie.log'
#常量，存的是日志文件名
PRODUCT_FILENAME = 't.txt'
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


def login():
    '''
    登录函数，如果登录成功返回登录用户名，登录失败返回None
    :return:
    '''
    print('欢迎进入电影分享社区'.center(50,'*'))
    username = raw_input('请输入用户名：')
    password = raw_input('请输入密码：')
    #strip用于移除头尾指定字符
    user_dic = read_file(USER_FILENAME)#获取到所有的用户信息
    if username=='' or password =='':
        print('账号或者密码不能为空！')
    else:
        if username in user_dic:
            if user_dic[username]['password'] == password:  # 登录成功
                write_log(username, '登录成功！')
                return username
            else:
                write_log(username, '密码不正确！')
                print('密码不对！')

        else:
            print('用户不存在')


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


def add_movie():
    movies = read_file(PRODUCT_FILENAME)#获取电影信息
    movie = {}
    movie['title'] = raw_input('请输入电影名称：')
    movie['cover'] = raw_input('请输入电影封面:')
    movie['screenshot'] = raw_input('请输入电影截图:')
    movie['year'] = raw_input('请输入电影年代:')
    movie['country'] = raw_input('请输入电影产地:')
    movie['category'] = raw_input('请输入电影类别：')
    movie['douban_rating'] = raw_input('请输入电影豆瓣评分:')
    movie['duration'] = raw_input('请输入电影片长')
    movie['director'] = raw_input('请输入电影导演')
    movie["profile"] = raw_input('请输入电影简介')
    movie['down_load'] = raw_input('请输入电影下载地址')

    #p_name = raw_input('请输入电影名称：')
    #p_id = raw_input('请输入电影id：')
    #p_price = raw_input('请输入电影价格：')
    if movie['title'] != '' :
        # if和elif都是条件为真的时候才走的
        for x in movies:
            if movie['title'] == x['title']:
                print('电影已存在！')
            elif not is_time(movie['year']):
                # not True是flase，指定走不到这里
                # not Flase，就是true，就走这了
                print('电影价格不合法！')
            else:
                movies.append(movie)
                #products_dic[p_name] = {'id': p_id, 'price': p_price}
                # products是存最新所有商品，给这个字典添加商品
                write_file(PRODUCT_FILENAME,movies)
                #调用写文件的函数，把商品信息写入到文件中
                write_log(username,'添加了电影信息 电影名【%s】 '
                         %(movie['title']))
                print('电影添加成功')
                break
    else:
        print('电影名称、电影id、电影价格都不能为空')

def del_movie():
    '''
    删除商品
    :return:
    '''
    movies = read_file(PRODUCT_FILENAME)  # 获取电影信息
    movie = {}
    #print('可以删除的有',products_dic.keys())
    movie['title'] = raw_input('请输入你要删除的电影名称：')
    y = 0
    if movie['title'] !='':
        for x in movies:
            if  movie['title'] == x['title']:
                #products_dic.pop(p_name)
                del movies[y]
                write_file(PRODUCT_FILENAME,movies)
                print('删除成功')
                write_log(username,'删除了【%s】'%movie['title'])
                break
            if (y == len(movies)):
                print('电影名称不存在！')
            y = y + 1
    else:
        print('电影名称不能为空')
def query_movie():
    '''
    查询电影
    :return:
    '''
    movies = read_file(PRODUCT_FILENAME)  # 获取电影信息
    movie = {}
    y = 0
    movie['title'] = raw_input('请输入你要查询的电影名称：')
    if movie['title'] != '':
        for x in movies:
            y = y + 1
            if movie['title'] == x['title']:
                '''
                p_id = products_dic[p_name]['id']
                p_price = products_dic[p_name]['price']
                '''
                msg = '电影名称是:【%s】' % (movie['title'])
                print(x)
                write_log(username,msg)
                break
            if (y == len(movies) ):
                print('你输入的电影名称不存在')
    else:
        print('你输入的电影名称不能为空')
def n_exit():
    exit('程序退出')

def add_user():
    users_dic = read_file(USER_FILENAME)#获取用户信息
    username = raw_input('用户名：')
    passwd = raw_input('用户密码：')
    blance = raw_input('用户的钱：')
    if username != '' and passwd != '' and blance != '':
        # if和elif都是条件为真的时候才走的
        if username in users_dic:
            print('用户名已存在！')
        elif not is_time(blance):
            # not True是flase，指定走不到这里
            # not Flase，就是true，就走这了
            print('钱不合法！')
        else:
            users_dic[username] = {'password': passwd, 'price': blance}
            # products是存最新所有商品，给这个字典添加商品
            write_file(USER_FILENAME,users_dic)
            #调用写文件的函数，把商品信息写入到文件中
            write_log(username,'添加了用户信息 用户名【%s】 钱是【%s】'
                      %(username,blance))
            print('用户添加成功')

def del_user():
    '''
     删除用户
     :return:
     '''
    users_dic = read_file(USER_FILENAME)  # 获取商品信息
    print('可以删除的有', users_dic.keys())
    username = raw_input('请输入你要删除的用户名：')
    if username != '':
        if username in users_dic:
            if username!='admin':
                users_dic.pop(username)
                write_file(USER_FILENAME, users_dic)
                print('删除成功')
                write_log(username, '删除了【%s】' % username)
            else:
                print('admin用户不能被删除！')
        else:
            print('用户不存在！')
    else:
        print('用户名不能为空')

def modify_user():
    users_dic = read_file(USER_FILENAME)  # 获取商品信息
    username = raw_input('请输入要修改的用户名:')
    blance = raw_input('请输入你要修改的金额：')
    passwd = raw_input('请输入你要修改的密码：')
    if username!='' and (blance!='' or passwd!=''):
        if username in users_dic:
            if blance!='':
                users_dic[username]['moeny']=blance
            elif passwd!='':
                users_dic[username]['password'] = passwd
            else:
                users_dic[username]['money'] = blance
                users_dic[username]['password'] = passwd
            write_file(USER_FILENAME,users_dic)#写用户信息
            write_log(username,'修改了%s用户'%username)
        else:
            print('用户不存在')
    else:
        print('用户名不能为空，金额和密码至少一个不能为空！')

def modify_user():
    users_dic = read_file(USER_FILENAME)  # 获取商品信息
    username = raw_input('请输入要修改的用户名:')
    blance = raw_input('请输入你要修改的金额：')
    passwd = raw_input('请输入你要修改的密码：')
    if username!='' and (blance!='' or passwd!=''):
        if username in users_dic:
            if blance!='':
                users_dic[username]['moeny']=blance
            elif passwd!='':
                users_dic[username]['password'] = passwd
            else:
                users_dic[username]['money'] = blance
                users_dic[username]['password'] = passwd
            write_file(USER_FILENAME,users_dic)#写用户信息
            write_log(username,'修改了%s用户'%username)
        else:
            print('用户不存在')
    else:
        print('用户名不能为空，金额和密码至少一个不能为空！')

def manager_user():
    choice = raw_input('1、添加用户 2、删除 3、修改用户 0退出：')
    if choice in manager_user_menu:
        manager_user_menu[choice]()
    else:
        print('请请输入0-3的选项！')

manager_user_menu  = {
    "1":add_user,
    "2":del_user,
    "3":modify_user,
    "0":n_exit
}#这个用户管理函数做的映射
movies_manger = {
    "1":add_movie,
    "2":del_movie,
    "3":query_movie,
    "0":n_exit,
}#这个是电影管理
admin_menu = {"4":manager_user}
admin_menu.update(movies_manger)
#admin的菜单，为了普通用户操作用户管理


def welcome():
    global username
    username = login()#调用登录函数，获取登录状态

    if username:
        if username=='admin':
            choice = raw_input('1 添加电影、2删除电影、3查询电影、4用户管理、0退出')
            if choice in admin_menu:
                admin_menu[choice]()
            else:
                print('请请输入0-4的选项！')
        else:
            choice = raw_input('1 添加电影、2删除电影、3查询电影、0退出:')
            if choice in movies_manger:
                movies_manger[choice]()
            else:
                print('请请输入0-3的选项！')


welcome()#运行程序程序