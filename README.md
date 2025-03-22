## User Authentication & Document Sharing System

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/) 
[![Flask 2.0+](https://img.shields.io/badge/Flask-2.0%2B-green.svg)](https://flask.palletsprojects.com/) 
[![MySQL](https://img.shields.io/badge/MySQL-Database-orange.svg)](https://www.mysql.com/) 
[![Bootstrap](https://img.shields.io/badge/Bootstrap-Responsive%20UI-purple.svg)](https://getbootstrap.com/)
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
## Demo
**students side**
![image](https://github.com/user-attachments/assets/85357c37-f60c-4eae-95d8-7f80a6764e9b)
![image](https://github.com/user-attachments/assets/4a3d4f70-ef33-4888-9627-5674470aec58)
![image](https://github.com/user-attachments/assets/9f99a5ce-d58f-481d-a403-bf0c26e6c62a)
![image](https://github.com/user-attachments/assets/068edcd8-bc1f-441a-9116-24ab77c360af)
![image](https://github.com/user-attachments/assets/6dcb73c1-6219-42d0-8adf-3f109f2ba448)
**teachers side**
![image](https://github.com/user-attachments/assets/bdecdd7d-9798-45fe-8012-59f978c81821)
![image](https://github.com/user-attachments/assets/9368d105-3022-425a-a4ef-1cc6c9d87281)
![image](https://github.com/user-attachments/assets/5294957d-4d9c-4cd8-91b7-52d21e5c4b64)
![image](https://github.com/user-attachments/assets/7b8440ca-abb5-4200-9a8f-b5ad7acd3549)
**students side**
![image](https://github.com/user-attachments/assets/8ca1ff9a-4ecd-41c2-ac6c-828ef6b97530)









## Usage

New Users: Click “Signup” to create an account.

Returning Users: Log in with your credentials.

Faculty: Add or update grades from the “Add Grades” section (only visible to faculty).

Students: View your grades in read-only mode.

Documents: Upload or share files if enabled.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


