CREATE DATABASE proj_db;

USE proj_db;

CREATE TABLE Activities (
    activity_id INT AUTO_INCREMENT PRIMARY KEY,
    activity_type VARCHAR(100) NOT NULL,
    activity_duration INT NOT NULL, -- duration in hours
    student_group VARCHAR(100) NOT NULL,
    staff_name VARCHAR(100) NOT NULL,
    module_name VARCHAR(100) NOT NULL
);

INSERT INTO Activities (activity_type, activity_duration, student_group, staff_name, module_name) VALUES
('Lecture', 1, 'Group A', 'Alice Smith', 'Mathematics'),
('Seminar', 2, 'Group B', 'Bob Jones', 'Physics'),
('Lab', 3, 'Group C', 'Carol White', 'Chemistry'),
('Workshop', 1, 'Group D', 'David Brown', 'Biology'),
('Lecture', 2, 'Group A', 'Eve Black', 'Computer Science'),
('Seminar', 3, 'Group B', 'Alice Smith', 'Mathematics'),
('Lab', 1, 'Group C', 'Bob Jones', 'Physics'),
('Workshop', 2, 'Group D', 'Carol White', 'Chemistry'),
('Lecture', 3, 'Group A', 'David Brown', 'Biology'),
('Seminar', 1, 'Group B', 'Eve Black', 'Computer Science'),
('Lab', 2, 'Group C', 'Alice Smith', 'Mathematics'),
('Workshop', 3, 'Group D', 'Bob Jones', 'Physics'),
('Lecture', 1, 'Group A', 'Carol White', 'Chemistry'),
('Seminar', 2, 'Group B', 'David Brown', 'Biology'),
('Lab', 3, 'Group C', 'Eve Black', 'Computer Science'),
('Workshop', 1, 'Group D', 'Alice Smith', 'Mathematics'),
('Lecture', 2, 'Group A', 'Bob Jones', 'Physics'),
('Seminar', 3, 'Group B', 'Carol White', 'Chemistry'),
('Lab', 1, 'Group C', 'David Brown', 'Biology'),
('Workshop', 2, 'Group D', 'Eve Black', 'Computer Science');
