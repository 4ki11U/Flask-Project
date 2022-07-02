import os

from flask import Flask, request, render_template, redirect, url_for, send_from_directory, send_file
from werkzeug.utils import secure_filename

from database.flask_db import select_data, insert_data
from forms import CourseForm, UserCreate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cb02820a3e94d72c9f950ee10ef7e3f7a35b3f5b'

UPLOAD_FOLDER = r'D:\Python Projects\Flask\downloads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if 'username' in session:
#         username = session['username']
#         return 'Logged in as ' + username + '<br>' + "<b><a href = '/logout'>click here to log out</a></b>"
#     return "You are not logged <br><a href = '/authorization'></b>" + "click here to log in</b></a>"
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


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


@app.route('/courses/', methods=['GET', 'POST'])
def courses():
    form = CourseForm()
    if form.validate_on_submit():
        print(form.title.data, form.description.data, form.price.data, form.available.data, form.level.data)
        return redirect(url_for('courses'))
    return render_template('courses.html', form=form)


@app.route('/start/')
def start():
    return render_template('start.html', title='Про Фласк')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/create/')
def create():
    form = UserCreate()
    if request.method == 'POST':
        task_name = request.form.get('task_name')
        name = request.form.get('name')
        surname = request.form.get('surname')
        message = request.form.get('message')
        print(task_name)
        print(name)
        print(surname)
        print(message)
        # здесь логика базы данных
        print("\nData received. Now redirecting ...")
        return redirect(url_for('comments'))

    return render_template('create.html')


@app.route('/user_create/', methods=['GET', 'POST'])
def user_create():
    form = UserCreate()
    if request.method == 'POST':
        task_number = request.form.get('task_number')
        user_name = request.form.get('user_name')
        user_surname = request.form.get('user_surname')
        callway_number = request.form.get('callway_number')
        project = request.form.get('project')
        DeskControl = request.form.get('DeskControl')
        gorodok = request.form.get('gorodok')
        mail = request.form.get('mail')
        SmartBox = request.form.get('SmartBox')
        VPN = request.form.get('VPN')

        print(f'{task_number=}-{user_name=}-{user_surname=}-{callway_number=}-{project=}-{DeskControl=}-{gorodok=}-{mail=}-{SmartBox=}-{VPN=}')


        name_for_file = f"{task_number}.txt"


        file_name_and_path = f'D:\Python Projects\Flask\downloads\{name_for_file}'
        print(file_name_and_path)

        with open(f"{file_name_and_path}", "w+") as file:
            file.write(task_number)

        #file_path = filedialog.askdirectory()
        #return send_file(f'{file_name_and_path}', download_name=f"{task_number}.txt")
        return send_file(file_name_and_path, as_attachment=True)

        # return redirect(url_for('about'))

    return render_template('user_create.html', form=form)



if __name__ == "__main__":
    app.run()
