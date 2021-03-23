# 进阶3:排序查询
/*
select * from employees;

语法:
	select 查询列表
	from 表
	[where 筛选条件]
	order by 排序列表 [asc|desc]
特点:
	1. asc代表升序,desc代表降序
	2. order by子句中可以支持单个字段,多个字段,表达式,函数,别名
	3. order by子句一般放在最后,limit子句除外
*/

# 案例1: 查询员工信息,要求工资从高到底排序
SELECT * FROM employees ORDER BY salary;

# 案例2: 查询部门编号>=90的员工信息,按入职时间先后进行排序[添加筛选条件]
SELECT * 
FROM employees
WHERE department_id >= 90
ORDER BY hiredate;

# 案例3: 按年薪高低显示员工的信息和年薪[按表达式排序]
SELECT *,salary*12*(1+IFNULL(commission_pct,0)) AS 年薪
FROM employees
ORDER BY salary*12*(1+IFNULL(commission_pct,0));

# 案例4: 按年薪高低显示员工的信息和年薪[按别名排序]
SELECT *,salary*12*(1+IFNULL(commission_pct,0)) AS 年薪
FROM employees
ORDER BY 年薪;

# 案例5: 按姓名的长度显示员工的姓名和工资[按函数排序]
SELECT LENGTH(last_name) AS 姓名长度,last_name,salary FROM employees ORDER BY LENGTH(last_name) DESC;

# 案例6: 查询员工信息,要求先按工资排序,再按员工编号排序[按多个字段排序]
SELECT * FROM employees ORDER BY salary ASC,employee_id DESC;
