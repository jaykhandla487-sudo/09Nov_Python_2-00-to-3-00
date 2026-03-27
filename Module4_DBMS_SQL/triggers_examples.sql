CREATE TABLE log_table (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    message VARCHAR(100)
);

DELIMITER //

CREATE TRIGGER student_insert
AFTER INSERT ON students
FOR EACH ROW
BEGIN
    INSERT INTO log_table(message)
    VALUES('New student added');
END //

DELIMITER ;