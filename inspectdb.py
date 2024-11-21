import sqlite3

# Function to initialize the database and create the required table
def init_db():
    try:
        with sqlite3.connect('users.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS user (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )
            ''')
            conn.commit()
            print("Database initialized and 'user' table created.")
    except sqlite3.Error as e:
        print(f"Error initializing the database: {e}")

if __name__ == '__main__':
    init_db()
