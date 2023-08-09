# Задание №8
# * Создать базовый шаблон для всего сайта, содержащий
# общие элементы дизайна (шапка, меню, подвал), и
# дочерние шаблоны для каждой отдельной страницы.
# * Например, создать страницу "О нас" и "Контакты",
# используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {'title': 'Главная'}
    return render_template('index.html', **context)

@app.route('/about/')
def about():
    context = {'title': 'О нас'}
    return render_template('about.html', **context)


@app.route('/contacts/')
def contacts():
    context = {'title': 'Контакты'}
    return render_template('contacts.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
# 127.0.0.1:5000/about/
# 127.0.0.1:5000/contacts/
