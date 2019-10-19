-- List the following details of each employee:
-- employee number, last name, first name, gender, and salary.
select 
e.emp_no
,last_name
,first_name
,gender
,salary
from
employees as e 
left join
salaries as s 
on e.emp_no=s.emp_no