from flask import Flask, render_template, session, redirect, request, url_for
import sqlite3
import configparser
import re
import bcrypt

 
config = configparser.ConfigParser()
config.read('config.conf')
min_username_size = int(config['register.settings']['min_username_size'])
max_username_size = int(config['register.settings']['max_username_size'])
min_fullname_size = int(config['register.settings']['min_fullname_size'])
max_fullname_size = int(config['register.settings']['max_fullname_size'])
min_password_size = int(config['register.settings']['min_password_size'])
max_password_size = int(config['register.settings']['max_password_size'])
app = Flask(__name__)

connection = sqlite3.connect("server.db", check_same_thread=False)
cursor = connection.cursor()

app.secret_key = b'_5#y2L"F4rjojoejo%^&*@(*U@)UU@VF&@*9hg9ujhb8287TF@&FG*&@g9&^@g2yg8727286@%^%#$!&*Q8z\n\xec]/'

levels = {
    0 : "default",
    7 : "admin"
}

def returnlevel(username):
    res = cursor.execute("SELECT username, level FROM users")
    for userdata in res.fetchall():
        if username in userdata:
            return userdata[1]
def returnall(username):
    res = cursor.execute("SELECT username, email, fullname, verified, level FROM users")
    for userdata in res.fetchall():
        if username in userdata:
            return (userdata[1], userdata[2], userdata[3], userdata[4])
@app.route('/')
def index():
    if session['username']:
        return redirect(url_for('logined', page="Home"))
    else:
        return redirect(url_for('login'))

@app.route('/<page>')
def logined(page="Home"):
    if session['username']:
        return render_template('logined.html', page=page, permsjs=levels[returnlevel(session['username'])], fullname = returnall(session['username'])[1])
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        emailoraddres = request.form['email-or-username']
        password = request.form['password']

        if "@" in emailoraddres:
            #find by email in db and get username
            session['username'] = emailoraddres
            print("email")
        else:
            #find by username
            res = cursor.execute("SELECT username FROM users")
            users = res.fetchall()
            is_in_usernames = False
            for user in users:
                print(user, emailoraddres)
                if emailoraddres in user:
                    is_in_usernames = True
            if not is_in_usernames:
                return render_template("auth.html", register="false", 
                    error = "User with that username not exists!",
                    error_desc = "You can create a new accaunt or you have a mistake"
                    )
            res = cursor.execute("SELECT username, password, salt FROM users")
            for userdata in res.fetchall():
                if emailoraddres in userdata:
                    saved_password = userdata[1]
                    saved_salt = userdata[2]
            check_hashed = bcrypt.hashpw(bytes(request.form['password'], "utf-8"), saved_salt)
            if not check_hashed == saved_password:
                return render_template("auth.html", register="false", 
                    error = "Wrong password!",
                    error_desc = "Try again!"
                    )
            #TODO: fast request block 

            session['username'] = emailoraddres
            print("username")

        print(password)

        return redirect(url_for('index'))
    return render_template("auth.html", register="false")
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        

        # TODO: save data and password-hash to DB 
        res = cursor.execute("SELECT username FROM users")
        users = res.fetchall()
        # FullName Check
        if len(request.form['fullname']) < min_username_size:
            return render_template("auth.html", register="true", 
                error = "Full name is too short!",
                error_desc = "Please choose another full name"
            )
        if len(request.form['fullname']) > max_username_size:
            return render_template("auth.html", register="true", 
                error = "Full name is too long!",
                error_desc = "Please choose another full name"
            )
        # UserName Check
        for user in users:
            if request.form['username'] in user:
                return render_template("auth.html", register="true", 
                    error = "User with that username already exists!",
                    error_desc = "You can choose a new username or log in under one"
            )
        if len(request.form['username']) < min_username_size:
            return render_template("auth.html", register="true", 
                error = "Username is too short!",
                error_desc = "Please choose another username"
            )
        if len(request.form['username']) > max_username_size:
            return render_template("auth.html", register="true", 
                error = "Username is too long!",
                error_desc = "Please choose another username"
            )
        # TODO: email check
        # password Check
        if request.form['password'] != request.form['retyped-password']:
            return render_template("auth.html", register="true", 
                error = "Passwords are not same!",
                error_desc = "Try again"
            )
        if len(request.form['password']) < min_password_size:
            return render_template("auth.html", register="true", 
                error = "Password is too short!",
                error_desc = "Please choose another password"
            )
        if len(request.form['password']) > max_password_size:
            return render_template("auth.html", register="true", 
                error = "password is too long!",
                error_desc = "Please choose another password"
            )
        elif not re.search("[a-z]", request.form['password']):
            return render_template("auth.html", register="true", 
                error = "password must have at least one lowercase letter!",
                error_desc = "Please choose another password"
            )
        elif not re.search("[A-Z]", request.form['password']):
            return render_template("auth.html", register="true", 
                error = "password must have at least one capital letter!",
                error_desc = "Please choose another password"
            )
        elif not re.search("[0-9]", request.form['password']):
            return render_template("auth.html", register="true", 
                error = "password must have at least one capital number!",
                error_desc = "Please choose another password"
            )
        # Saving all to database
        password = bytes(request.form['password'], 'utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password, salt)

        data = [(request.form['username'], request.form['email'], request.form['fullname'], hashed, salt, False, 0)]
        # print("username", "email", "fullname", "password", "salt", "verified", "level")
        # print(data)
        cursor.executemany("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?)", data)
        connection.commit()
        session['username'] = request.form['username']
        #all good! can redirect to index
        return redirect(url_for('index'))
    return render_template("auth.html", register="true")


@app.route('/logout')
def logout():
    session['username'] = None
    return redirect(url_for('index'))
app.run(host='0.0.0.0')