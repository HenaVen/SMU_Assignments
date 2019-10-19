
-- 3. List the manager of each department with the following information:
-- department number, department name, the manager's employee number, last -- and start and end employment dates.
select 
	dm.dept_no
	,dept_name
	,dm.emp_no
	,last_name
	,first_name
	,dm.from_date
	,dm.to_date
	
from
employees as e 
join dept_manager dm
on e.emp_no=dm.emp_no
join departments d
on dm.dept_no=d.dept_no
order by e.last_name asc;