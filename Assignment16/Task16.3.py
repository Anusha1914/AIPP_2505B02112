SELECT*from Members WHERE join_date > '2025-09-01';
SELECT * FROM Members;
SELECT * FROM Books;
SELECT * FROM Loans;
SELECT 
    Books.book_id,
    Books.title,
    Books.author,
    Loans.loan_date,
    Loans.return_date
FROM Loans
JOIN Books ON Loans.book_id = Books.book_id
JOIN Members ON Loans.member_id = Members.member_id
WHERE Members.name = 'Anusha';
