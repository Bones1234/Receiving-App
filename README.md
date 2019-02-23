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