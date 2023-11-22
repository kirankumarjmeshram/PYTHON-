import sqlite3

# conn = sqlite3.connect(':memory:') #Temporaly store in memory
#connect to db
conn = sqlite3.connect('customer.db')
#create a cursor
c = conn.cursor()

#create a table
c.execute("""CREATE TABLE customers (
           first_name text,
           last_name text,
           email text
)""")

# c.execute("""CREATE TABLE customers (  first_name DATATYPE, last_name DATATYPE, email DATATYPE)""")

#commit our command
conn.commit()

#close our connection
conn.close()