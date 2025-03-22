create database userauthdb;
USE userauthdb;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    role VARCHAR(20) NOT NULL DEFAULT 'student',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE users ADD COLUMN role VARCHAR(20) NOT NULL DEFAULT 'student';



	CREATE TABLE grades (
    grade_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    subject VARCHAR(50),
    grade VARCHAR(5),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
select * from grades;
select * from users;