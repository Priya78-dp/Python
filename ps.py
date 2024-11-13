import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="rkce"
)
c=mydb.cursor()
c.execute("insert into employee values (407, 'sravani', 2080)")
mydb.commit()