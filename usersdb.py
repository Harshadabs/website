import sqlite3

# Create a new SQLite database file
connection = sqlite3.connect('database.db')
print("Database created successfully!")
connection.close()
