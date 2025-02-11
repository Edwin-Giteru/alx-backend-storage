-- a script that creates a viev that lists all students that have score < 80

CREATE VIEW need_meeting AS
SELECT name FROM students
WHERE score < 80 AND(last_meeting IS NULL OR last_meeting > 1);
