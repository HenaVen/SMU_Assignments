
-- 7. List all employees in the Sales and Development departments, 
-- including their employee number, last name, first name, and department name.
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
where dept_name in ('Sales','Development')
order by e.last_name asc;