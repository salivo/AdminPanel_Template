from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('user.html')

@app.route('/admin/<page>')
def admin(page):
    return render_template('adminpanel.html', page=page)

app.run(host='0.0.0.0')