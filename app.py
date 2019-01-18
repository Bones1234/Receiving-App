from flask import Flask,render_template
from datetime import datetime

app = Flask(__name__)

#todays date
time_in_stamp = datetime.today()
print("TIME-IN:  "+ str(time_in_stamp))

@app.route('/')
def index():
    name = 'Aaron Smith'
    age = 27
    return render_template('index.html',name=name,age=age)

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