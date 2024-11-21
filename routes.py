from flask import request
from app import app, db
from model import User

@app.route('/signup', methods=['POST'])
def signup():
    # Get form data
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')  # In a real app, hash passwords before saving!

    # Save data to the database
    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('/log'))


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        session['username'] = user.username
        return redirect(url_for('home'))
    flash('Invalid credentials.', 'danger')
    return redirect(url_for('/'))