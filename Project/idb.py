# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
host ="localhost",
user ="tableshalini",
passwd ="Z004@2025",
database = "student"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

sql = "INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION, AGE)\
VALUES (%s, %s, %s, %s, %s)"
val = ("Shiva", "ISE", "90", "A", "20")

cursorObject.execute(sql, val)
dataBase.commit()

# disconnecting from server
dataBase.close()
