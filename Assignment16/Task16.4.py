UPDATE Books
SET available = FALSE
WHERE book_id = 110;

DELETE FROM Members
WHERE member_id = 3;
DELETE FROM Members
WHERE member_id = 3;

SELECT * FROM Loans
WHERE member_id = 3 AND return_date IS NULL;
