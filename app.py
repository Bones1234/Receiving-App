from flask import Flask, render_template, request, g, redirect, url_for, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
LIMIT = 30
#Bootstrap(app)

class Appointments(db.Model):
  __tablename__='Appointments'
  id = db.Column(db.Integer, primary_key=True)
  driver_name = db.Column(db.String(80), nullable=False)
  phone_number = db.Column(db.String(15))
  po_number = db.Column(db.String(80))
  link = db.Column(db.String(200))
  comment = db.Column(db.String(200))
  status = db.Column(db.String(80))
  trailer_number = db.Column(db.String(80))
  carrier = db.Column(db.String(80))
  door_number = db.Column(db.String(80))
  date_created = db.Column(db.DateTime, default=datetime.utcnow)
  assignee_id = db.Column(db.Integer, db.ForeignKey('assignees.id'))

class Assignees(db.Model):
  __tablename__='assignees'
  id = db.Column(db.Integer, primary_key=True)
  assignee_name = db.Column(db.String(50))
  appointments = db.relationship('Appointments', backref='assignee')

@app.route("/")
def index():
  hello_text = "Appointments"
  appts = Appointments.query.order_by(text('driver_name desc')).limit(LIMIT).all()
  assignees = [assignee.assignee_name for assignee in Assignees.query.all()]
  return render_template('index.html', appts=appts,assignees=assignees)

@app.route('/create', methods=['POST', 'GET'])
def create():
  if request.method == 'POST':
    driver = request.form['driver_name']
    phone = request.form['phone_number']
    po = request.form['po_number']
    status = request.form['status']
    trailer_number = request.form['trailer_number']
    carrier = request.form['carrier']
    door_number = request.form['door_number']
    date = datetime.now()
    link = request.form['link']
    comment = request.form['comment']
    assignee = Assignees(assignee_name=request.form['assignee'])
    signature = Appointments(driver_name=driver,date_created=date,phone_number=phone,po_number=po,status=status,trailer_number=trailer_number,carrier=carrier,door_number=door_number,link=link,comment=comment)
    # signature.assignee = Assignees(assignee_name="Raphael")
    signature.assignee = assignee
    try:
      db.session.add(signature)
      db.session.commit()
      return redirect(url_for('index'))
      flash('updated')
    except:
      return 'There was an issue adding your appointment'

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Appointments.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that appintment'

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    appt = Appointments.query.get_or_404(id) # appt = Appointments.query.filter_by(id = id).first()
    print(request.args)

    if request.method == 'POST':
      appt.driver_name = request.form['driver_name']
      appt.phone_number = request.form['phone_number']
      appt.po_number = request.form['po_number']
      appt.status = request.form['status']
      appt.trailer_number = request.form['trailer_number']
      appt.carrier = request.form['carrier']
      appt.door_number = request.form['door_number']
      appt.date_created = datetime.now()
      appt.link = request.form['link']
      appt.comment = request.form['comment']
      try:
          db.session.commit()
          flash('updated')
          return redirect('/')
      except:
          return 'There was an issue updating your appointment'

    else:
        return render_template('edit.html', appt=appt)

@app.route('/appointment/<int:id>', methods=['GET', 'POST'])
def appointment(id):
    try:
        appt = Appointments.query.get_or_404(id) # appt = Appointments.query.filter_by(id = id).first()
    except:
        return 'There was an issue finding your appointment'

    else:
        return render_template('show.html', appt=appt)

@app.route('/api')
def output():
  data = request.get_json()
  return jsonify(data)

if __name__=='__main__':
  app.run(debug=True)
  