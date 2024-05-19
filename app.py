from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    today = datetime.today().date()
    now = datetime.now()
    return render_template('home.html', now=now, today=today)

@app.route('/about')
def about():
    employees = [
        'dauxan',
        'tlek',
        'marlen',
        'kantemir'
    ]
    return render_template('about.html', employees=employees)

@app.route('/shop')
def shop():
    categories = [
        'Смартфон',
        'телефон',
        'пылесос',
        'телик'
    ]
    return render_template('shop.html', categories=categories)

@app.route('/shop/<category_name>')
def category(category_name):
    return render_template('category.html', category=category_name)

if __name__ == '__main__':
    app.run(debug=True)

