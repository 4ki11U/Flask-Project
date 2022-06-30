from flask import Flask, request, render_template, redirect, url_for
from database.flask_db import select_data, insert_data


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/authorization', methods=['GET', 'POST'])
def form_authorization():
    if request.method == 'POST':
        login = request.form.get('Login')
        password = request.form.get('Password')

        auth = select_data(login)

        try:
            if auth[0] != password:
                return render_template('authorization_and_registration/auth_bad.html')
        except:
            return render_template('authorization_and_registration/auth_bad.html')

        return redirect(url_for('start'))

    return render_template('authorization_and_registration/authorization.html')


@app.route('/registration', methods=['GET', 'POST'])
def form_registration():
    if request.method == 'POST':
        login = request.form.get('Login')
        password = request.form.get('Password')

        registration_data = insert_data(login, password)

        return render_template('authorization_and_registration/successregis.html')

    return render_template('authorization_and_registration/registration.html')


@app.route('/comments/')
def comments():
    return render_template('comments.html')


@app.route('/start/')
def start():
    return render_template('start.html', title='Про Фласк')


@app.route('/about/')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run()
