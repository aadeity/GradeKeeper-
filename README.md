## User Authentication & Document Sharing System

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/) 
[![Flask 2.0+](https://img.shields.io/badge/Flask-2.0%2B-green.svg)](https://flask.palletsprojects.com/) 
[![MySQL](https://img.shields.io/badge/MySQL-Database-orange.svg)](https://www.mysql.com/) 
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

This project demonstrates how to implement a Flask-based web application using MySQL for user authentication, profile management, and secure document sharing. It also features **role-based access** so that faculty members can update grades, while students can only view them.

## Key Functionalities  
- **User Registration & Login**: Securely store credentials in a MySQL database.  
- **Profile Management**: Update personal details and reset passwords.  
- **Document Sharing**: Upload and manage documents if you have the necessary privileges.  
- **Role-Based Grade Management**:  
  - **Faculty**: Add or update student grades.  
  - **Students**: View grades without edit privileges.

## Installation & Setup
1. Make sure you have **Python 3.8+** and **MySQL** installed.  
2. Clone this repository or download it to your local machine.  
3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
4. Create a MySQL database and run the provided schema.sql script to set up tables.

5.In your Flask app file (e.g., app.py), update the MySQL configuration (host, user, password, db).

6. Start the Flask server:
   ```bash
   python app.py
7. Open your browser at http://127.0.0.1:5000/.
   
## Usage

New Users: Click “Signup” to create an account.

Returning Users: Log in with your credentials.

Faculty: Add or update grades from the “Add Grades” section (only visible to faculty).

Students: View your grades in read-only mode.

Documents: Upload or share files if enabled.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


