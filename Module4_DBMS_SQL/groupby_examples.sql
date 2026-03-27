SELECT class, COUNT(*) AS total_students
FROM students
GROUP BY class;