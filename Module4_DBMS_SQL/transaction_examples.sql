START TRANSACTION;

INSERT INTO students VALUES (10,'Rohan',14,'8B','Indore');

SAVEPOINT sp1;

UPDATE students SET age = 15 WHERE student_id = 10;

ROLLBACK TO sp1;

COMMIT;