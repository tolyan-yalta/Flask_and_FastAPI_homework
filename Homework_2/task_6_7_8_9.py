# Задание №6
# * Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# * При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.

# Задание №7
# * Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# * При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.

# Задание №8
# * Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# * При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".

# Задание №9
# * Создать страницу, на которой будет форма для ввода имени
# и электронной почты
# * При отправке которой будет создан cookie файл с данными
# пользователя
# * Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# * На странице приветствия должна быть кнопка "Выйти"
# * При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.

from flask import Flask, flash, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'


@app.route("/")
def index():
    return render_template("index.html")


# задание №6
@app.post('/check/')
def check():
    name = request.form.get('name')
    age = request.form.get("age")
    if age != "" and 0 < int(age) <= 100:
        return redirect(url_for('result_age', name=name, age=age))
    else:
        return render_template("index.html", error=True)


@app.route("/result age/<name> <age>")
def result_age(name, age):
    return render_template("result_age.html", name=name, age=age)


# Задание №7
@app.post("/square number/")
def square_number():
    num = request.form.get("number")
    res = int(num) ** 2
    return redirect(url_for("result_square", num=num, res=res))

@app.route("/result square/<num> <res>")
def result_square(num, res):
    return render_template("result_square.html", num=num, res=res)


# Задание №8
@app.route('/flash/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get("name")
        message = f"Привет, {name}!"
        flash(message, 'success')
        return redirect(url_for('form'))
    return render_template('flash.html')


# Задание №9
@app.post("/create cookie/")
def create_cookie():
    name = request.form.get("name")
    email = request.form.get("email")
    response = make_response(redirect(url_for("hello_user")))
    response.headers['new_head'] = 'New value'
    response.set_cookie('user', name)
    response.set_cookie('email', email)
    return response


@app.route("/hello user/")
def hello_user():
    name = request.cookies.get('user')
    email = request.cookies.get("email")
    response = make_response(render_template("hello_user.html", name=name, email=email))
    return response


@app.post("/exit/")
def exit():
    responce = make_response(redirect(url_for("index")))
    responce.delete_cookie("email")
    responce.delete_cookie("user")
    
    return responce


if __name__ == "__main__":
    app.run(debug=True)
"""
http://127.0.0.1:5000
"""
