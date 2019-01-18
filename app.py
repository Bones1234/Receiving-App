from flask import Flask,render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)

# DATABASE LOGIC for MYSQL (not uisng now)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)

#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

#     def __repr__(self):
#         return '<User %r>' % self.username

# admin = User('admin', 'admin@example.com')
# db.create_all() # In case user table doesn't exists already. Else remove it.    
# db.session.add(admin)
# db.session.commit() # This is needed to write the changes to database
# User.query.all()
# User.query.filter_by(username='admin').first()

#todays date
time_in_stamp = datetime.today()
print("TIME-IN:  "+ str(time_in_stamp))

@app.route('/')
def index():
    name = 'Aaron Smith'
    age = 27
    time_in_stamp = datetime.today()
    return render_template('index.html',name=name,age=age,time=time_in_stamp)

@app.route('/hello')
def hello():
    return render_template('test.html')

@app.route('/world')
def world():
    a = 1
    b = 2
    return render_template('world.html',sum=a+b)

if __name__ =="__main__":
    app.run(debug=True)