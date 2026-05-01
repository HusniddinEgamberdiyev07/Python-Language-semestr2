import mysql.connector as sql
from mysql.connector import Error

conn = sql.connect(
    host="127.0.0.1",
    user="egamberdiyevhusniddin",
    password="mysqlhuse0708",
    database="siut"
)


if conn.is_connected(): print("Connected")
else: print("Something went wrong")

mycursor = conn.cursor()
mycursor.execute("SELECT * FROM students")

studentsTable = mycursor.fetchall()