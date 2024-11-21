from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'IHATEMONGODB'  # Required for sessions

DATABASE = 'users.db'

# Database setup
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
    print("Database initialized!")

# Route: Home
@app.route('/')
def home():
    if 'user' in session:
        return render_template('home.html', user=session['user'])
    return redirect(url_for('login'))

# Route: Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with sqlite3.connect(DATABASE) as conn:
            user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
            if user and check_password_hash(user[2], password):
                session['user'] = username
                flash('Login successful!', 'success')
                return redirect(url_for('home'))
            else:
                flash('Invalid username or password.', 'danger')

    return render_template('login.html')

# Route: Signup
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        try:
            with sqlite3.connect(DATABASE) as conn:
                conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
                conn.commit()
                flash('Signup successful! Please log in.', 'success')
                return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username already exists.', 'danger')

    return render_template('signup.html')

# Route: Logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

def add_user(username, email, password):
    hashed_password = generate_password_hash(password, method='sha256')
    try:
        users_collection.insert_one({
            "username": username,
            "email": email,
            "password": hashed_password
        })
        return True
    except Exception as e:
        print(f"Error adding user: {e}")
        return False

def get_user_by_email(email):
    return users_collection.find_one({"email": email})

def update_user_email(current_email, new_email):
    result = users_collection.update_one(
        {"email": current_email},
        {"$set": {"email": new_email}}
    )
    return result.modified_count > 0

def delete_user(email):
    result = users_collection.delete_one({"email": email})
    return result.deleted_count > 0



@app.route('/mobilelegends')
def mobilelegends():
    return render_template('mobilelegends.html', packages=diamond_packages)

diamond_packages = [
    {"title": "5 diamonds", "price": "₹ 13"},
    {"title": "11 diamonds", "price": "₹ 25"},
    {"title": "14 diamonds", "price": "₹ 30"},
    {"title": "22 diamonds", "price": "₹ 45"},
    {"title": "42 diamonds", "price": "₹ 75"},
    {"title": "56 diamonds", "price": "₹ 95"},
    {"title": "86 diamonds", "price": "₹ 135"},
    {"title": "122 diamonds", "price": "₹ 175"},
    {"title": "172 diamonds", "price": "₹ 275"},
    {"title": "257 diamonds", "price": "₹ 380"},
    {"title": "344 diamonds", "price": "₹ 530"},
    {"title": "429 diamonds", "price": "₹ 650"},
    {"title": "514 diamonds", "price": "₹ 730"},
    {"title": "706 diamonds", "price": "₹ 960"},
    {"title": "1050 diamonds", "price": "₹ 1420"},
    {"title": "1135 diamonds", "price": "₹ 1800"},
    {"title": "1412 diamonds", "price": "₹ 1980"},
    {"title": "2195 diamonds", "price": "₹ 3100"},
    {"title": "2901 diamonds", "price": "₹ 3850"},
    {"title": "3600 diamonds", "price": "₹ 4850"},
    {"title": "5532 diamonds", "price": "₹ 6650"},
    {"title": "9288 diamonds", "price": "₹ 10800"},
]

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/Honkai')
def Honkai():
    return render_template('honkai star rail.html', packages=shards_packages)

shards_packages = [
    {"title": "60 shards", "price": "₹ 13"},
    {"title": "11 shards", "price": "₹ 25"},
    {"title": "14 shards", "price": "₹ 30"},
    {"title": "22 shards", "price": "₹ 45"},
    {"title": "42 shards", "price": "₹ 75"},
    {"title": "56 shards", "price": "₹ 95"},
]

@app.route('/GenshinImpact')
def GenshinImpact():
    return render_template('genshin.html', packages=Genesis_packages)

Genesis_packages = [
        {"title": "60", "price": "₹ 80"},
        {"title": "330", "price": "₹ 390"},
        {"title": "1090", "price": "₹ 1140"},
        {"title": "2240", "price": "₹ 2450"},
        {"title": "3880", "price": "₹ 3750"},
        {"title": "8080", "price": "₹ 7500"},
    ]


@app.route('/log')
def log():
    return render_template('login.html')

@app.route('/sign')
def sign():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
