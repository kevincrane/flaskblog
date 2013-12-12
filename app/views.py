from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Kevin'}  # fake user
    posts = [
        {
            'author': {'nickname': 'Steven'},
            'body': 'Beautiful day in Seattle!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)
