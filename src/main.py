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
can_change_perms_level = int(config['permission.settings']['can_change_perms_level'])
app = Flask(__name__)

connection = sqlite3.connect("server.db", check_same_thread=False)
cursor = connection.cursor()

app.secret_key = b'_5#y2L"F4rjojoejo%^&*@(*U@)UU@VF&@*9hg9ujhb8287TF@&FG*&@g9&^@g2yg8727286@%^%#$!&*Q8z\n\xec]/'

levels = {
    0 : "default",
    6 : "admin",
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

def CheckCreatedPassword(password, retyped_password):

    if password != retyped_password:
        error = "Passwords are not same!",
        error_desc = "Try again"
        return (error, error_desc)

    if len(password) < min_password_size:
        error = "Password is too short!",
        error_desc = "Please choose another password"
        return (error, error_desc)
    
    if len(password) > max_password_size:
        error = "password is too long!",
        error_desc = "Please choose another password"
        return (error, error_desc)

    elif not re.search("[a-z]", password):
        error = "password must have at least one lowercase letter!",
        error_desc = "Please choose another password"
        return (error, error_desc)

    elif not re.search("[A-Z]", password):
        error = "password must have at least one capital letter!",
        error_desc = "Please choose another password"
        return (error, error_desc)

    elif not re.search("[0-9]", password): 
        error = "password must have at least one capital number!",
        error_desc = "Please choose another password"
        return (error, error_desc)

    return ("", "")




@app.route('/')
def index():

    session['info'] = ""
    session['error'] = ""

    if not 'username' in session:
        return redirect(url_for('login'))
    if not session['username']:
        return redirect(url_for('login'))
    return redirect(url_for('logined', page="Home"))
        

@app.route('/<page>')
def logined(page="Home"):
    error = session['error']
    info = session['info']
    
    session['error'] = ""
    session['info'] = ""

    if session['username']:
        return render_template('logined.html', page=page, permsjs=levels[returnlevel(session['username'])], fullname = returnall(session['username'])[1], username = session['username'], error=error, info=info)
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        emailoraddres = request.form['email-or-username']
        password = request.form['password']

        if "@" in emailoraddres:
            #find by email in db and get username
            res = cursor.execute("SELECT email FROM users")
            emails = res.fetchall()
            is_in_emails = False
            for email in emails:
                if emailoraddres in email:
                    is_in_emails = True
            if not is_in_emails:
                return render_template("auth.html", register="false", 
                    error = "User with that email not exists!",
                    error_desc = "You can create a new accaunt or you have a mistake"
                    )
            res = cursor.execute("SELECT email, username, password, salt FROM users")
            for userdata in res.fetchall():
                if emailoraddres in userdata:
                    saved_username = userdata[1]
                    saved_password = userdata[2]
                    saved_salt = userdata[3]
            check_hashed = bcrypt.hashpw(bytes(request.form['password'], "utf-8"), saved_salt)
            if not check_hashed == saved_password:
                return render_template("auth.html", register="false", 
                    error = "Wrong password!",
                    error_desc = "Try again!"
                    )
            session['username'] = saved_username
            
        else:
            #find by username
            res = cursor.execute("SELECT username FROM users")
            users = res.fetchall()
            is_in_usernames = False
            for user in users:
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
            session['username'] = saved_username
            #TODO: block many request per time
        return redirect(url_for('index'))

    return render_template("auth.html", register="false")




@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
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
        # FIXME:   in username can't be @ symbol it will brake anything
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
        error, error_desc = CheckCreatedPassword(request.form['password'],request.form['retyped-password'])
        if error:
            return render_template("auth.html", register="true", 
                    error = error,
                    error_desc = error_desc
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

@app.route('/setpermslevel', methods=['POST'])
def setpermslevel():
    if request.method == 'POST':

        if can_change_perms_level <= returnlevel(session['username']): 
            res = cursor.execute("SELECT username FROM users")
            users = res.fetchall()
            toadd = request.form['username']
            isintable = False
            for user in users:
                if toadd in user:
                    isintable = True
            if isintable:
                new_level = int(request.form['level'])
                cursor.execute("UPDATE users SET level = ? WHERE username = ?", (new_level, toadd))
                connection.commit()
                session['info'] = """Successfully set """ + request.form['level'] + """ permission level for """ + toadd
                return redirect(url_for('logined', page="AdminSettings"))
            else:
                session['error'] = """cannot find user with that username"""
                return redirect(url_for('logined', page="AdminSettings"))
        else:
            session['error'] = """You cannot perform it! Not enough rights"""
            return redirect(url_for('logined', page="AdminSettings")) 
@app.route('/setfullname', methods=['POST'])
def setfullname():
    if request.method == 'POST': 
            new_fullname = request.form['new_fullname']
            cursor.execute("UPDATE users SET fullname = ? WHERE username = ?", (new_fullname, session['username']))
            connection.commit()
            session['info'] = """Successfully set """ + new_fullname
            return redirect(url_for('logined', page="Settings"))
@app.route('/setnewpass', methods=['POST'])
def setnewpass():
    if request.method == 'POST':
        error, error_desc = CheckCreatedPassword(request.form['password'],request.form['retyped-password'])
        if error:
            session['error'] = error
            return redirect(url_for('logined', page="Settings"))
        new_password = bytes(request.form['password'], 'utf-8')
        new_salt = bcrypt.gensalt()
        new_hashed = bcrypt.hashpw(new_password, new_salt)
        cursor.execute("UPDATE users SET password = ?, salt = ? WHERE username = ?", (new_hashed, new_salt, session['username']))
        connection.commit()
        session['info'] = """Successfully set new password!"""
        return redirect(url_for('logined', page="Settings"))




app.run(host='0.0.0.0')
connection.close()