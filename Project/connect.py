import mysql.connector

# Connect to the MySQL database
cnx = mysql.connector.connect(
host ="localhost",
user ="tableshalini",
password ="Z004@2025",
database = "student"
)

# Create a cursor to execute SQL queries
cursor = cnx.cursor()

# Execute a query
cursor.execute('SELECT * FROM student')

# Fetch the results
rows = cursor.fetchall()
print(rows)
# Close the cursor and connection
cursor.close()
cnx.close()
