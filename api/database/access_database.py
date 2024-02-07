import sqlite3

# Connect to the database
conn = sqlite3.connect('my_database.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a query to retrieve names
cursor.execute("SELECT name FROM my_table")

# Fetch all the names
names = cursor.fetchall()

# Print the names
for name in names:
    print(name[0])

# Close the cursor and connection
cursor.close()
conn.close()
