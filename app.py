from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.secret_key = 'T7<QE3aZ'

# Initialize LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Name of the login route

# Initialize database
db = SQLAlchemy(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Corrected: use `user_id` instead of `id`

# Define the User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

# Route: Signup
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Check if username or email already exists
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            flash('Username or email already exists!', 'danger')
            return redirect(url_for('signup'))

        # Directly store the plain-text password (not secure)
        new_user = User(username=username, email=email, password=password)
        
        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))  # Redirect to login page
    
    return render_template('signup.html')  # Render the registration page

# Route: Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Query the user by username and password (plain text)
        user = User.query.filter_by(username=username, password=password).first()

        if user:  # User exists and password matches
            login_user(user)
            return redirect(url_for('profile'))  # Redirect to profile page
        else:
            flash('Invalid username or password', 'danger')  # Feedback on failed login

    return render_template('login.html')  # Render login page if GET request

# Route: Profile
@app.route('/profile')
@login_required  # Ensure the user is logged in
def profile():
    return render_template('index.html', user=current_user)

# Route: Logout
@app.route('/logout')
@login_required  # Only logged-in users can log out
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

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


if __name__ == '__main__':
    app.run(debug=True)
