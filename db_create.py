# INSERT Command

from views import db
from models import Task
from datetime import date

# Creating the population table
db.create_all()

# insert data into table
db.session.add(Task("Finish this tutorial", date(2015, 3, 13), 10, 1))
db.session.add(Task("Finish Real Python Course 2", date(2015, 3, 13), 10, 1))

# commit the changes
db.session.commit()
  

