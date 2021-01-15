from flask import Flask, render_template, url_for, request, redirect, session, g
import model
import datetime


app = Flask(__name__)
app.secret_key='#2508#31052010tnt'
data=[]

username = ''
user = model.check_users()

@app.route('/admin', methods = ['GET','POST'])
def admin():
    if request.method == 'GET':
        return render_template('admin.html')
    else:
        user=request.form['admin']
        user_password= request.form['admin_password']
        if user == 'admin' and user_password == 'admin':
            message = 'You are logged in as administrator!'
            return render_template('dashboard.html', message=message)

    return render_template('admin.html')

@app.route('/usersinfo')
def usersinfo():
    message = model.check_users()
    return render_template('dashboard.html', message = message)

@app.route('/total')
def total():
    nr = model.usr_total()
    message = 'Users in Database:'
    return render_template('dashboard.html', message = message, nr = nr)

@app.route('/del_user/<email>', methods= ['GET'])
def del_user(email):
    if request.method == 'GET':
        todel= request.form['email']
        model.DelUsr(todel)

    message= 'User Deleted!'
    return render_template('dashboard.html', message = message)

@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/', methods = ['GET','POST'])
def home():
    if 'username' in session:
        g.user = session['username']
        return render_template('todo.html')
    else:return render_template('index.html', title='Home Page')
    #return render_template('index.html', title='Home Page')
    return ''

@app.route('/about', methods= ['GET'])
def about():
    return render_template('about.html', title= 'About Me')

@app.before_request
def before_request():
    g.username = None
    if 'username' in session:
        g.username = session['username']
        session.pop('username')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('username', None)
        is_user = request.form['email']
        #db_users = model.check_users()
        pwd = model.check_pw(is_user)############################
        if request.form['password']== pwd:# and is_user in db_users:
            session['username'] = request.form['email']
            return render_template('todo.html')
        else:
            message='Please Register!'
            return render_template('index.html', message= message)
    else: return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        message = 'Please Sign UP!'
        return render_template('Signup.html', message= message)
    else:
        session.pop('username', None)
        email = request.form['email']
        password = request.form['password']
        message = model.signup(email, password)
        return render_template('index.html', message= message)

@app.route('/todopg', methods = ['GET', 'POST'])
def todopg():
    if request.method == 'POST':
        todo = request.form['todo']
        if todo in data:
            message='Todo Item Already Exists'
            return message
        else:
            data.append(todo)
            date=datetime.date.today()
            end_date = request.form['end_date']

            #email = request.form['email']
            #todo = request.form['todo']
            #model.add_todo(email,todo)

            return render_template('todo.html', data = data, date = date, end_date = end_date)

        #return render_template('todo.html', data = data)

@app.route('/sterge/<todo>')
def sterge(todo):
    data.remove(todo)
    return render_template('todo.html', data=data)

@app.route('/delete')
def delete():
    for todo in data:
        data.remove(todo)
    #mesaj= 'List Deleted'
    return render_template('todo.html',data= data)#, mesaj=mesaj)

@app.route('/save')
def save():
    #email = request.form['email']
    #todo = request.form['todo']
    #model.add_todo(email,todo)
    date= str(datetime.date.today())
    with open('list.txt', 'w+') as l:
        for todo in data:
            l.write(todo)
            l.write('\n')
            l.write(date)
    return render_template('todo.html')
""" """
@app.route('/getsession')
def getsession():
    if 'username' in session:
        return session['username']
    return redirect(url_for('todopg'))

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))
    #return render_template('index.html')

@app.route('/open_dir', methods=['get'])
def open_dir():
    import os
    #path = 'C:/Users/geo home/Desktop/py/acurs/flask/homework#5'
    #path = os.path.realpath(path)
    #file = os.startfile(path)
    path = os.path.abspath(os.getcwd())
    file = os.startfile(path)
    return render_template('todo.html', file=file)

if __name__ == '__main__':
    app.run(port=7000, debug = True)