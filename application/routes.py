from application import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Felipe'}
    return '''

<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Olá, ''' + user['username'] + '''!</h1>
    </body>
</html>

'''