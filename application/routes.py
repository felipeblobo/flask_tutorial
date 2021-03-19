from application import app
from flask import render_template

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