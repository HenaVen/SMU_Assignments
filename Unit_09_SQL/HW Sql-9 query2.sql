
-- 2. List employees who were hired in 1986.

select 
	emp_no
	,last_name
	,first_name
	,gender
	,hire_date
	,date_part('year',hire_date)
from
employees as e 
where date_part('year',hire_date)
='1986'