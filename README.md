IMPORTANT: Once I add the database, you will need to do this first to install everything you need:

`pip3 install -r requirements.txt`


# Requested Fields:

## Appointment time/date 

(Pulled from database)

## Time-in 

(Time stamped on submission)

## PO number: (Purchase Order Number)

This is the ID associated with the driver's "Bill of lading" which is essentially a document showing all of the product that is on the back of the truck. NOTE: Driver's can have multiple PO's so we will need to be able to enter multiple PO's. PO numbers are 5 digits long. (Maybe have a safegaurd that won't allow submission of the form if the PO number is more than 5 characters.)

Note: https://stackoverflow.com/questions/10281962/is-there-a-minlength-validation-attribute-in-html5

Note: https://stackoverflow.com/questions/14853779/adding-input-elements-dynamically-to-form

## Trailer Number (Number on the driver's trailer)

## Driver's Name

We will need two pages. One for submissions and one for admins which will serve as a work queue. The admin page will list submissions from the submission page and will have an uploaded document that can be accessed through either a shared folder or a server.

## Status of submission 

will be listed on this page and updatable from this page. Statuses inlude (Pending, Complete, and Staging [Parked in the parking lot])
- We may also need to be able to filter a the list of submissions based on the above mentioned "Statuses"

## WILL CONTINUE TO UPDATE

# Starting and Stopping server
- Control+c to stop server
- python3 app.py/or/filename to start

# Workflow for GIT
- git add .
- git commit -am "Message"
- git push 
- git pull
- pip3 install -r requirements.txt

Just updating you on the app. We’ll be working with the actual Americold IT people to get it actually done. The prototype will serve as a template for them to work on.


https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

**To create the models in the database:**

Open a python intepreter with `python3` , import `db` and run `db.create_all()`

```
python3
from setup import db
db.create_all()
```


#http://docs.sqlalchemy.org/en/latest/orm/query.html#sqlalchemy.orm.query.Query.limit

#THIS IS NOT NECESSARY. First, run 'sqlite3 database.db < schema.sql' from the terminal to generate the database.db file from the schema file.

#select * from customer where dateofbirth < date('now','-30 years');

#User.birthday <= '1988-01-17

#from app.py import db. db.create_all()
#2016-01-01 10:20:05.123

# QUERIES
https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/

**Retrieve a appointment by driver name:**
Appointments.query.filter_by(driver_name="Sarah Jones").first()

**Ordering appointments by something:**
Appointments.query.order_by(Appointments.driver_name).all()

**Limiting appointments:**
Appointments.query.limit(1).all()

**Getting user by primary key:**
Appointments.query.get(1)

**Selecting a bunch of users by a more complex expression:**
Appointments.query.filter(Appointments.driver_name.endswith('s')).all()

