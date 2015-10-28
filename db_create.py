# INSERT Command
# import the sqlite3 library
import sqlite3
from _config import DATABASE_PATH

# Creating the population table
with sqlite3.connect(DATABASE_PATH) as connection:
  c = connection.cursor()
  # If we want to create a new table, uncomment the next two lines
  c.execute("DROP TABLE IF EXISTS tasks")
  # Create the table
  c.execute("""CREATE TABLE tasks
			  (task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, 
        due_date TEXT NOT NULL,
        priority INTEGER NOT NULL,
        status INTEGER NOT NULL)
			  """)
  # insert multiple records using a tuple
  tasks = [
   ("Finish this tutorial", "03/25/2015", 10, 1),
   ("Finish Real Python Course 2", "03/25/2015", 10, 1)
  ]

  # insert data into table
  c.execute(
    'INSERT INTO tasks (name, due_date, priority, status)'
    'VALUES("Finish this tutorial", "03/25/2015", 10, 1)'
  )
  c.execute(
   'INSERT INTO tasks (name, due_date, priority, status)'
   'VALUES("Finish Real Python Course 2", "03/25/2015", 10, 1)'
  )
  
  c.execute("SELECT task_id, name, due_date, priority, status from tasks")

  # fetchall() retrieves all records from the query
  rows = c.fetchall()
  # output the rows to the screen, row by row
  for r in rows:
    print r[0], r[1], r[2], r[3], r[4] 

