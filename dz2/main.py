from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = 'ce602efccb8559483be2b58e17982bc77b481a38dbfdb6ed6a85f5cc6dc7f890'


@app.route('/', methods=['GET', 'POST'])
def login():
    context = {
        'login': 'Авторизация'
    }
    if request.method == 'POST':
        session['name'] = request.form.get('name')
        session['email'] = request.form.get('email')
        return redirect(url_for('access'))
    return render_template('login.html', **context)


@app.route('/access/', methods=['GET', 'POST'])
def access():
    if 'name' in session:
        context = {
            'name': session['name'],
            'email': session['email'],
            'title': 'Добро пожаловать'
        }
        if request.method == 'POST':
            session.pop('name', None)
            session.pop('email', None)
            return redirect(url_for('login'))
        return render_template('access.html', **context)
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
