#encoding: utf-8
from flask import *

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




if __name__ == '__main__':
    app.run(host='127.0.0.1')