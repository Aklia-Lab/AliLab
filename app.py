from flask import Flask, render_template, url_for
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app) # Compliant

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='test ali'))

if __name__ == '__main__':
    app.run(port=5000)