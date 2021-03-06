from flask import Flask,render_template,request,jsonify
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.debug = True
# FOR TOOLBAR
# app.config['SECRET_KEY'] = "itsasecret"
# toolbar = DebugToolbarExtension(app)

# DATABASE LOGIC for MYSQL (not using now)
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

#get todays date
time_in_stamp = datetime.today()
print("TIME-IN:  "+ str(time_in_stamp))

@app.route('/')
def index():
    name = 'Aaron Smith'
    id = "HHA27-2882GW-74BA983"
    time_in = datetime.today()
    return render_template('index.html',name=name,id=id,time_in=time_in)

@app.route('/hello')
def hello():
    return render_template('test.html')

@app.route('/output',methods=["GET","POST"])
def output():
    data = request.form.to_dict()
    return render_template('output.html',data=data)

if __name__ =="__main__":
    app.run()