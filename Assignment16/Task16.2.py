INSERT INTO Members (member_id, name, email, join_date) VALUES
(1, 'Mahvish', 'abc@123.gmail.com', '2025-10-16'),
(2, 'Harshitha', 'def@gmail.com', '2025-10-10'),
(3, 'Anjali', 'ghi@gmail.com', '2025-10-24');

INSERT INTO Books (book_id, title, author, available) VALUES
(110, 'Atomic Habits', 'James Clear', TRUE),
(120, 'Rich Dad Poor Dad', 'Robert Kiyosaki', TRUE),
(130, 'The Power of Habit', 'Charles Duhigg', FALSE),
(140, 'The Alchemist', 'Paulo Coelho', TRUE);

INSERT INTO Loans (loan_id, member_id, book_id, loan_date, return_date) VALUES
(1, 1, 130, '2025-10-10', NULL),
(2, 2, 110, '2025-10-12', '2025-10-20'),
(3, 3, 120, '2025-10-15', NULL);
