from flask import Flask, render_template, session, redirect, request, url_for
import json
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4rjojoejo%^&*@(*U@)UU@VF&@*9hg9ujhb8287TF@&FG*&@g9&^@g2yg8727286@%^%#$!&*Q8z\n\xec]/'


@app.route('/')
def index():
    return redirect(url_for('logined', page="Home"))

@app.route('/<page>')
def logined(page="Home"):
    return render_template('logined.html', page=page, permsjs="default")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('admin',page="Dashboard"))
    return render_template("auth.html", register="false")
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('admin',page="Dashboard"))
    return render_template("auth.html", register="true")

app.run(host='0.0.0.0')