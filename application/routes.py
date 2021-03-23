from flask import render_template, flash, redirect
from application import app
from application.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Felipe'}
    posts = [
        {
            'author': {'username': 'Ana'},
            'body': 'É um belo dia para salvar vidas!'
        },

        {
            'author': {'username':'Pedro'},
            'body': 'Viva o carnaval!'
        }
    ]
    return render_template('index.html', user = user, posts = posts, title = "Home")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requisitado para o usuário {}, rememberMe={}'.format(
            form.username.data, form.rememberMe.data
        ))
        return redirect ('/index')
    return render_template('login.html', title = 'Login', form = form)
