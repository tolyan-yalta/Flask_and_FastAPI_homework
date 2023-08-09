# Задание №9
# * Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню,
# подвал), и дочерние шаблоны для страниц категорий
# товаров и отдельных товаров.
# * Например, создать страницы "Одежда", "Обувь" и "Куртка",
# используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {'title': 'Главная'}
    return render_template('index.html', **context)


@app.route('/clothes/')
def clothes():
    context = {'title': 'Одежда'}
    return render_template('clothes.html', **context)


@app.route('/clothes/jackets/')
def jackets():
    context = {'title': 'Зимняя одежда',
                "assortments": [
                   {"name": "куртка", "size": 42, "price": 250.5},
                   {"name": "пальто", "size": 45, "price": 310.0},
                   {"name": "шуба", "size": 43, "price": 190.2}
               ]}
    return render_template('assortment.html', **context)


@app.route('/footwear/')
def footwear():
    context = {'title': 'Обувь'}
    return render_template('footwear.html', **context)


@app.route('/footwear/winter shoes/')
def winter_shoes():
    context = {'title': 'Зимняя обувь',
               "assortments": [
                   {"name": "boots", "size": 42, "price": 250.5},
                   {"name": "valenki", "size": 45, "price": 310.0},
                   {"name": "rubber boots", "size": 43, "price": 190.2}
               ]}
    return render_template('assortment.html', **context)


@app.route('/footwear/summer shoes/')
def summer_shoes():
    context = {'title': 'Летняя обувь',
               "assortments": [
                   {"name": "vyetnamki", "size": 42, "price": 250.5},
                   {"name": "sandals", "size": 45, "price": 310.0},
                   {"name": "sneakers boots", "size": 43, "price": 190.2}
               ]}
    return render_template('assortment.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
# 127.0.0.1:5000
# 127.0.0.1:5000/clothes/
# 127.0.0.1:5000/footwear/
# 127.0.0.1:5000/footwear/winter shoes/
