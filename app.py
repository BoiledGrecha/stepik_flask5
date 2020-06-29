from flask import Flask, render_template, request
import json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stepik.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route("/")
def first():
        
    return render_template("main.html")

@app.route("/cart/")
def cart():
    
    return render_template("cart.html")

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