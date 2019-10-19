select 
	last_name
	,first_name
	from
employees as e 
where 
first_name like 'Hercules'
and
last_name like 'B%'

order by e.last_name asc;