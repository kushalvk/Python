import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="msc_it"
)

mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")
mycursor.execute("select * from student")

# result = mycursor.fetchall()
result = mycursor.fetchone()

for i in result:
    print(i)