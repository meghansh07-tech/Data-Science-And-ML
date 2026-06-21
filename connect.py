import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="mydatabase"
)

cursor = db.cursor()

sql = "INSERT INTO student VALUES (%s, %s)"
values = (3, "Anant")

cursor.execute(sql, values)

db.commit()

print("Data inserted!")