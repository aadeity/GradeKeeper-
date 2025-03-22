from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

# Set a secret key for session management
app.secret_key = 'your secret key'

# MySQL configurations – update these with your actual MySQL credentials
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your password'
app.config['MYSQL_DB'] = 'userauthdb'  # Ensure this matches your database name

mysql = MySQL(app)

# landing page
@app.route('/')
def index():
    return render_template('index.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        account = cursor.fetchone()
        if account:
            # Save user details and role in session
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            session['role'] = account['role']  # teacher or student
            flash('Logged in successfully!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Incorrect username or password!', 'danger')
    return render_template('login.html')

# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST' and all(k in request.form for k in ('username', 'password', 'email', 'role')):
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        role = request.form['role']  # teacher or student
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        account = cursor.fetchone()
        if account:
            flash('Account already exists!', 'warning')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash('Invalid email address!', 'warning')
        elif not re.match(r'[A-Za-z0-9]+', username):
            flash('Username must contain only characters and numbers!', 'warning')
        else:
            cursor.execute('INSERT INTO users (username, password, email, role) VALUES (%s, %s, %s, %s)',
                           (username, password, email, role))
            mysql.connection.commit()
            flash('You have successfully registered!', 'success')
            return redirect(url_for('login'))
    elif request.method == 'POST':
        flash('Please fill out the form!', 'warning')
    return render_template('signup.html')

# Dashboard route
@app.route('/dashboard')
def dashboard():
    if 'loggedin' in session:
        return render_template('dashboard.html', username=session['username'])
    return redirect(url_for('login'))

# Logout route
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    session.pop('role', None)
    flash('You have been logged out!', 'info')
    return redirect(url_for('login'))

# Update Profile route
@app.route('/update_profile', methods=['GET', 'POST'])
def update_profile():
    if 'loggedin' in session:
        user_id = session['id']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        if request.method == 'POST':
            email = request.form['email']
            if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                flash('Invalid email address!', 'warning')
            else:
                cursor.execute('UPDATE users SET email = %s WHERE id = %s', (email, user_id))
                mysql.connection.commit()
                flash('Profile updated successfully!', 'success')
                return redirect(url_for('dashboard'))
        cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
        account = cursor.fetchone()
        return render_template('update_profile.html', account=account)
    return redirect(url_for('login'))

# Reset Password route
@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if 'loggedin' in session:
        user_id = session['id']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        if request.method == 'POST' and 'current_password' in request.form and 'new_password' in request.form:
            current_password = request.form['current_password']
            new_password = request.form['new_password']
            cursor.execute('SELECT * FROM users WHERE id = %s AND password = %s', (user_id, current_password))
            account = cursor.fetchone()
            if account:
                cursor.execute('UPDATE users SET password = %s WHERE id = %s', (new_password, user_id))
                mysql.connection.commit()
                flash('Password updated successfully!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Current password is incorrect!', 'danger')
        return render_template('reset_password.html')
    return redirect(url_for('login'))

# view-only page for users to see their grades
@app.route('/grades')
def grades():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        if session.get('role') == 'teacher':
            # Teachers see all grades along with the student's username
            cursor.execute('''
                SELECT g.subject, g.grade, u.username AS student 
                FROM grades g 
                JOIN users u ON g.user_id = u.id
            ''')
        else:
            # Students see only their own grades
            user_id = session['id']
            cursor.execute('SELECT subject, grade FROM grades WHERE user_id = %s', (user_id,))
        grades = cursor.fetchall()
        return render_template('grades.html', grades=grades)
    return redirect(url_for('login'))

# - accessible only for teachers, with a dropdown list of students.
# After adding a grade, it stays on the same page and shows a flash message.
@app.route('/add_grade', methods=['GET', 'POST'])
def add_grade():
    if 'loggedin' in session and session.get('role') == 'teacher':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        if request.method == 'POST':
            user_id = request.form['user_id']
            subject = request.form['subject']
            grade = request.form['grade']
            cursor.execute('INSERT INTO grades (user_id, subject, grade) VALUES (%s, %s, %s)',
                           (user_id, subject, grade))
            mysql.connection.commit()
            flash('Grade added successfully!', 'success')
            # Redirect back to the same add grade page
            return redirect(url_for('add_grade'))
        else:
            # GET: Retrieve all students to populate the dropdown
            cursor.execute("SELECT id, username FROM users WHERE role = 'student'")
            students = cursor.fetchall()
            return render_template('add_grade.html', students=students)
    else:
        flash('Unauthorized access. Only teachers can add grades.', 'danger')
        return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
