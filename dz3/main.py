# Урок 3. Дополнительные возможности Flask
# Задание
# Создать форму для регистрации пользователей на сайте. Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться". При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.


import binascii
import random
from flask import Flask, render_template, request
from models import db, Users
from forms import RegisterForm
from flask_wtf.csrf import CSRFProtect
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_user.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        password = form.password.data
        dk = hashlib.pbkdf2_hmac(hash_name="sha256", password=bytes(
            password, "utf-8"), salt=b"bad_salt", iterations=100000,)
        password = binascii.hexlify(dk)
        user = Users(firstname=firstname, lastname=lastname,
                     email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return f"Вы зарегистрированы"
    return render_template('register.html', form=form)


@app.route('/users/', methods=['GET', 'POST'])
def get_users():
    users = Users.query.all()
    return f"{list(users)}"


# @app.get("/book/")
# def get_book():
#     books = Book.query.all()
#     context = {
#         "books": books
#     }
#     return render_template("books.html", **context)


if __name__ == '__main__':
    app.run(debug=True)
