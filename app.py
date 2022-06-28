from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def start_app():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/comments/')
def comments():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]
    return render_template('comments.html', comments=comments)


@app.route('/create/', methods=('GET', 'POST'))
def create():
    return render_template('create.html')
