from flask import Flask, render_template , redirect , url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class Product_Forms(FlaskForm):
    name = StringField('Название вашего товара')
    description = StringField('Описание о товаре')
    price = StringField('цена товара')
    submit = SubmitField('Добавить')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\admin\\PycharmProjects\\flask-python-connect\\test.db'
app.config['SECRET_KEY']='DAULETKHAN'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(20), nullable=False)
    adress_ = db.Column(db.String(10), nullable=False)
    number = db.Column(db.Integer, nullable=False)


class Product(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)


@app.route('/add',methods = ['GET','POST'])
def add_products():
    form = Product_Forms()
    if form.validate_on_submit():
        new_product = Product(name = form.name.data,description =form.description.data,price = form.price.data)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('shop'))
    return render_template('add.html',form = form)
@app.route('/')
def home():
    today = datetime.today().date()
    now = datetime.now()
    return render_template('home.html', now=now, today=today)

@app.route('/about')
def about():
    employees = ['Иван', 'Петр', 'Мария', 'Анна']  # Пример списка сотрудников
    return render_template('about.html', employees=employees)

@app.route('/shop')
def shop():
    products = Product.query.all()
    return render_template('shop.html', products=products)

@app.route('/shop/<category_name>')
def category(category_name):
    return render_template('category.html', category=category_name)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

