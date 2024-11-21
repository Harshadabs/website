from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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

@app.route('/login', methods=['POST'])
def login():
    # Extract form data
    username = request.form.get('username')
    password = request.form.get('password')

    # Check if username exists in the database
    user = users_collection.find_one({"username": username})

    if user:
        # Verify the password using bcrypt
        if bcrypt.check_password_hash(user['password'], password):
            # Successful login
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            # Incorrect password
            flash('Invalid password. Please try again.', 'danger')
    else:
        # Username not found
        flash('Username not found. Please register.', 'danger')

    # Redirect to login page in case of error
    return redirect(url_for('login'))
@app.route('/log')
def log():
    return render_template('login.html')

@app.route('/Sign')
def Sign():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)