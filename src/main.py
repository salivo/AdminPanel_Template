from flask import Flask, render_template, session, redirect, request, url_for

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4rjojoejo%^&*@(*U@)UU@VF&@*9hg9ujhb8287TF@&FG*&@g9&^@g2yg8727286@%^%#$!&*Q8z\n\xec]/'


@app.route('/')
def index():
    return render_template('user.html')

@app.route('/admin/<page>')
def admin(page):
    return render_template('adminpanel.html', page=page)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('admin',page="Dashboard"))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

app.run(host='0.0.0.0')