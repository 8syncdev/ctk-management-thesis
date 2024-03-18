INSERT INTO account (account_id, name, email, role, password) VALUES
('acc_001', 'Nguyễn Văn Mạnh', 'nguyenvanmanh@example.com', 'student', 'password1'),
('acc_002', 'Trần Thị Hương', 'tranthihuong@example.com', 'teacher', 'password2'),
('acc_003', 'Phạm Minh Tuấn', 'phamminhtuan@example.com', 'student', 'password3'),
('acc_004', 'Lê Thị Mai', 'lethimai@example.com', 'student', 'password4'),
('acc_005', 'Hoàng Văn Hùng', 'hoangvanhung@example.com', 'teacher', 'password5'),
('acc_006', 'Trần Minh Hải', 'tranminhhai@example.com', 'student', 'password6'),
('acc_007', 'Nguyễn Thị Lan', 'nguyenthilan@example.com', 'student', 'password7'),
('acc_008', 'Phan Thanh Tùng', 'phanthanhtung@example.com', 'student', 'password8'),
('acc_009', 'Ngô Hải Yến', 'ngohaiyen@example.com', 'teacher', 'password9'),
('acc_010', 'Vũ Thị Hà', 'vuthiha@example.com', 'student', 'password10');

INSERT INTO task (name, group_id, progress, deadline) VALUES
('Task 1', 1, 0.2, '2024-03-31 09:00:00'),
('Task 2', 2, 0.4, '2024-04-05 14:00:00'),
('Task 3', 3, 0.6, '2024-04-10 12:00:00'),
('Task 4', 4, 0.8, '2024-04-15 16:00:00'),
('Task 5', 5, 1.0, '2024-04-20 10:00:00'),
('Task 6', 1, 0.3, '2024-04-25 11:00:00'),
('Task 7', 2, 0.5, '2024-04-30 13:00:00'),
('Task 8', 3, 0.7, '2024-05-05 15:00:00'),
('Task 9', 4, 0.9, '2024-05-10 17:00:00'),
('Task 10', 5, 1.0, '2024-05-15 18:00:00');


INSERT INTO "group" (name, account_id) VALUES
('Group 1', 1),
('Group 2', 2),
('Group 3', 3),
('Group 4', 4),
('Group 5', 5),
('Group 6', 6),
('Group 7', 7),
('Group 8', 8),
('Group 9', 9),
('Group 10', 10);


INSERT INTO thesis (account_id, task_id, group_id, technology_category, name, criteria, score, deadline) VALUES
(1, 1, 1, 'Web Development', 'Thesis 1', 'Criteria 1', 0.8, '2024-04-30 09:00:00'),
(2, 2, 2, 'Machine Learning', 'Thesis 2', 'Criteria 2', 0.7, '2024-05-05 14:00:00'),
(3, 3, 3, 'Mobile App Development', 'Thesis 3', 'Criteria 3', 0.6, '2024-05-10 12:00:00'),
(4, 4, 4, 'Data Science', 'Thesis 4', 'Criteria 4', 0.9, '2024-05-15 16:00:00'),
(5, 5, 5, 'Cybersecurity', 'Thesis 5', 'Criteria 5', 1.0, '2024-05-20 10:00:00'),
(6, 6, 1, 'Blockchain', 'Thesis 6', 'Criteria 6', 0.7, '2024-05-25 11:00:00'),
(7, 7, 2, 'Artificial Intelligence', 'Thesis 7', 'Criteria 7', 0.8, '2024-05-30 13:00:00'),
(8, 8, 3, 'Cloud Computing', 'Thesis 8', 'Criteria 8', 0.9, '2024-06-05 15:00:00'),
(9, 9, 4, 'Internet of Things', 'Thesis 9', 'Criteria 9', 0.6, '2024-06-10 17:00:00'),
(10, 10, 5, 'Big Data', 'Thesis 10', 'Criteria 10', 0.8, '2024-06-15 18:00:00');


INSERT INTO technology_category (name) VALUES
('Web Development'),
('Machine Learning'),
('Mobile App Development'),
('Data Science'),
('Cybersecurity'),
('Blockchain'),
('Artificial Intelligence'),
('Cloud Computing'),
('Internet of Things'),
('Big Data');


INSERT INTO technology_requirement (name, description) VALUES
('Front-end Development', 'Develop user interfaces for websites or web applications.'),
('Neural Networks', 'Implement neural network models for machine learning tasks.'),
('iOS App Development', 'Create mobile applications for iOS devices.'),
('Data Visualization', 'Represent data in graphical or pictorial format for easy understanding.'),
('Network Security', 'Ensure the security of computer networks from unauthorized access or attacks.'),
('Smart Contracts', 'Write smart contracts for blockchain applications.'),
('Natural Language Processing', 'Analyze and process natural language data for AI applications.'),
('Cloud Infrastructure', 'Set up and manage cloud-based infrastructure for applications or services.'),
('IoT Device Programming', 'Develop software for Internet of Things devices.'),
('Data Analysis', 'Analyze large datasets to extract useful insights and patterns.');


INSERT INTO thesis_requirement (thesis_id, technology_requirement_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);
