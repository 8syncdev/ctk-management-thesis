INSERT INTO account (name, email, role, password) VALUES
('Nguyễn Văn Mạnh', 'nguyenvanmanh@example.com', 'teacher', 'password1'),
('Trần Thị Hương', 'tranthihuong@example.com', 'teacher', 'password2'),
('Phạm Minh Tuấn', 'phamminhtuan@example.com', 'teacher', 'password3'),
('Lê Thị Mai', 'lethimai@example.com', 'teacher', 'password4'),
('Hoàng Văn Hùng', 'hoangvanhung@example.com', 'teacher', 'password5'),
('Trần Minh Hải', 'tranminhhai@example.com', 'teacher', 'password6'),
('Nguyễn Thị Lan', 'nguyenthilan@example.com', 'teacher', 'password7'),
('Phan Thanh Tùng', 'phanthanhtung@example.com', 'teacher', 'password8'),
('Ngô Hải Yến', 'ngohaiyen@example.com', 'teacher', 'password9'),
('Vũ Thị Hà', 'vuthiha@example.com', 'teacher', 'password10'),
('Nguyễn Thùy Linh', 'linh@example.com', 'student', 'password11');

-- INSERT INTO task (name, group_id, progress, deadline) VALUES
-- ('Task 1', 1, 0.2, '2024-03-31 09:00:00'),
-- ('Task 2', 2, 0.4, '2024-04-05 14:00:00'),
-- ('Task 3', 3, 0.6, '2024-04-10 12:00:00'),
-- ('Task 4', 4, 0.8, '2024-04-15 16:00:00'),
-- ('Task 5', 5, 1.0, '2024-04-20 10:00:00'),
-- ('Task 6', 1, 0.3, '2024-04-25 11:00:00'),
-- ('Task 7', 2, 0.5, '2024-04-30 13:00:00'),
-- ('Task 8', 3, 0.7, '2024-05-05 15:00:00'),
-- ('Task 9', 4, 0.9, '2024-05-10 17:00:00'),
-- ('Task 10', 5, 1.0, '2024-05-15 18:00:00');

INSERT INTO criterion (name, description) VALUES
('Formulation', 'The clarity and specificity of the problem statement.'),
('Methodology', 'The appropriateness and effectiveness of the research method.'),
('Results', 'The quality and significance of the research findings.'),
('Discussion', 'The depth and insightfulness of the research discussion.'),
('References', 'The relevance and reliability of the cited sources.'),
('Presentation', 'The organization and delivery of the research presentation.'),
('Creativity', 'The originality and innovation of the research work.'),
('Relevance', 'The significance and applicability of the research topic.'),
('Quality', 'The overall quality and coherence of the research work.'),
('Contribution', 'The contribution and impact of the research to the field.');


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


INSERT INTO thesis (account_id, group_id, name, score, deadline) VALUES
(1, 1, 'Web Application for Online Shopping', 0.0, '2024-03-31 09:00:00'),
(2, 2, 'Predictive Model for Stock Prices', 0.0, '2024-04-05 14:00:00'),
(3, 3, 'Mobile App for Health Monitoring', 0.0, '2024-04-10 12:00:00'),
(4, 4, 'Data Analysis for Marketing Strategies', 0.0, '2024-04-15 16:00:00'),
(5, 5, 'Network Security for E-commerce Websites', 0.0, '2024-04-20 10:00:00'),
(6, 6, 'Smart Contracts for Supply Chain Management', 0.0, '2024-04-25 11:00:00'),
(7, 7, 'Natural Language Processing for Chatbots', 0.0, '2024-04-30 13:00:00'),
(8, 8, 'Cloud Infrastructure for Online Services', 0.0, '2024-05-05 15:00:00'),
(9, 9, 'IoT Device Programming for Smart Homes', 0.0, '2024-05-10 17:00:00'),
(10, 10, 'Data Analysis for Business Intelligence', 0.0, '2024-05-15 18:00:00');


