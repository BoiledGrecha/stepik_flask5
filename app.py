from flask import Flask, render_template, request, session, redirect, url_for
import json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import *
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from random import shuffle
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stepik.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "super_secret_random_string"
db = SQLAlchemy(app)
migrate = Migrate(app, db) # needed?
admin = Admin(app)

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Order, db.session))
admin.add_view(ModelView(Meal, db.session))

def inside_cart():
    if not session.get("cart"):
        return None
    else:
        total = 0
        tmp = json.loads(session["cart"])
        for i in tmp.items(): 
            total += Meal.query.filter(Meal.id == int(i[0])).first().price * int(i[1])
        return (sum(tmp.values()), total)
        
@app.route("/")
def first():
    categories = Category.query.all()
    for i in categories:
        shuffle(i.meals)
    cart = inside_cart()
    if not cart:
        cart = "Пусто"
    else:
        cart = "{} блюда {}руб.".format(cart[0], cart[1])
            
    return render_template("main.html", categories=categories, cart = cart)

@app.route("/addtocart/<id>")
def add_cart(id):
    if not session.get("cart"):
        session["cart"] = dict()
    else:
        session["cart"] = json.loads(session["cart"])
    session["cart"][id] = session["cart"].get(id, 0) + 1
    session["cart"] = json.dumps(session["cart"])
    return redirect(url_for("cart"))

#delete <-----------------
@app.route("/kill_cart/")
def kill_cart():
    session.pop("cart")
    return "OK"
    
@app.route("/cart/")
def cart():
    tmp = inside_cart()
    if not tmp:
        cart = "Пусто"
        cart2 = "Корзина пуста"
    else:
        cart = "{} блюда {}руб.".format(tmp[0], tmp[1])
        cart2 = "{} блюда в корзине".format(tmp[0])
    
    return render_template("cart.html", cart = cart, cart2 = cart2)

@app.route("/account/")
def account():
    return render_template("account.html")

@app.route("/login/")
def login():
    
    return render_template("login.html")

@app.route("/register/", methods = ["GET", "POST"])
def rergister():
    
    return render_template("register.html")

@app.route("/logout/", methods = ["GET", "POST"])
def logout():
    
    return render_template("auth.html")


@app.route("/ordered/", methods = ["GET", "POST"])
def ordered():
    
    return render_template("ordered.html")
            
if __name__ == "__main__":
	app.run(debug=True)