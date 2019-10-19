-- 8. In descending order, 
-- list the frequency count of employee last names, i.e., how many employees share each last name.
select 
		last_name,count(last_name) as frequencyln	
from
employees as e 
group by last_name
order by e.last_name desc;