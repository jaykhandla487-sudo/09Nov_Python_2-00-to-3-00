DECLARE
   CURSOR student_cursor IS
   SELECT student_name FROM students;

   s_name students.student_name%TYPE;

BEGIN
   OPEN student_cursor;

   LOOP
      FETCH student_cursor INTO s_name;
      EXIT WHEN student_cursor%NOTFOUND;

      DBMS_OUTPUT.PUT_LINE(s_name);
   END LOOP;

   CLOSE student_cursor;
END;
/