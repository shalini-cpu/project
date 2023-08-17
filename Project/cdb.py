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

# creating table
studentRecord = """CREATE TABLE STUDENT (
				NAME VARCHAR(20) NOT NULL,
				BRANCH VARCHAR(50),
				ROLL INT NOT NULL,
				SECTION VARCHAR(5),
				AGE INT
				)"""

# table created
cursorObject.execute(studentRecord)

# disconnecting from server
dataBase.close()
