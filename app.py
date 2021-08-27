from flask import Flask, flash, redirect, render_template, \
     request, url_for
from src.db import dao
from src import config


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
db_provider = dao


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    error = None
    email = request.form['email']
    token = request.form['token']

    if email == '' or token == '' or token.startswith('"') or token.endswith('"'):
        error = 'Invalid Data.'

    if not email.endswith(config.ALLOWED_EMAIL_DOMAINS):
        error = 'not valid email for the service.'

    if error is not None:
        return render_template('index.html', error=error)

    if not db_provider.insert_token(email, token):
        flash('something\'s wrong with service ...')

    flash('your token has been submitted successfully')

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
