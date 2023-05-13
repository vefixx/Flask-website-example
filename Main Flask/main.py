from flask import Flask, render_template, request, url_for, redirect
import database

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def default():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(f'Login: {username} ; Password: {password}')
        check = database.check_login_pass(username,password)
        if check == True:
            return f'<h1>Вы вошли как {username}</h1>'
        else:
            return f'<h1>Неверный логин или пароль</h1>'

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        acc = database.check_login_pass(username,password)
        if acc == True:
            return f'<h1>Вы уже имеете аккаунт</h1>'
        else:
            database.add_user(username,password)
            print('Add user', username, password)
            return '<h1>Successful register</h1>'

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
