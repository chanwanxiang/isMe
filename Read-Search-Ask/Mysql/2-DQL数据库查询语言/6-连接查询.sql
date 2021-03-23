# 进阶6:
/*
含义:多表查询

笛卡尔乘积的错误情况:当查询多个表时,没有添加有效的连接条件,表间完成完全连接.
表1有m行,表2有n行,结果=m*n行


发生原因:没有有效的连接条件
如何避免:添加有效的连接条件

分类:
	按年代分类
	sql92标准:仅仅支持内连接
		等值
		非等值
		自连接
	sql99标准[推荐]:
	
	按功能分类:
		内连接:
			等值连接
			非等值连接
			自连接
		外连接:
			左外连接
			右外连接
			全外连接
		交叉连接:

*/
SELECT * FROM beauty;
SELECT * FROM boys;
SELECT `name`,boyname FROM beauty,boys WHERE beauty.`boyfriend_id` = boys.`id`;

# 案例1: 查询女生和对应的男生
# 等值连接
/*

1. 多表等值连接结果为多表交集部分
2. n表连接至少需要n-1个连接条件
3. 多表的顺序没有要求
4. 一般需要为表起别名
5. 可以搭配前面介绍的所有子句

*/
SELECT `name`,boyname 
FROM beauty,boys 
WHERE beauty.`boyfriend_id` = boys.`id`;

# 案例2: 查询员工名和对应部门名
SELECT last_name,department_name 
FROM employees,departments 
WHERE employees.`department_id` = departments.`department_id`;

# 案例3: 为表取别名,提高语句简洁度
# 查询员工名,工种号,工种名
SELECT last_name,e.job_id,job_title 
FROM employees AS e,jobs
WHERE e.`job_id` = jobs.`job_id`;

# 案例4: 添加筛选,查询有奖金的员工名,部门名
SELECT last_name,department_name FROM employees AS e,departments WHERE e.`department_id` = departments.`department_id` AND e.`commission_pct` IS NOT NULL;

#案例5: 查询城市名中第二个字符为o的部门名和城市名
SELECT city,department_name 
FROM locations,departments 
WHERE locations.`location_id` = departments.`location_id` 
AND city LIKE '_o%';

# 添加分组,
# 案例6: 查询每个城市的部门个数
SELECT city,COUNT(*) AS 个数 
FROM locations,departments 
WHERE locations.`location_id` = departments.`location_id` 
GROUP BY city;

# 案例7: 查询有奖金的每个部门的部门名称和领导编号和该部门的最低工资
SELECT department_name,departments.manager_id,MIN(salary) AS 最低工资
FROM departments,employees
WHERE departments.`department_id` = employees.`department_id`
AND commission_pct IS NOT NULL
GROUP BY department_name;

# 案例8: 添加排序查询每个工种的工种名和员工个数,并且按员工个数降序
SELECT job_title,COUNT(*) AS 员工个数
FROM jobs,employees
WHERE jobs.`job_id` = employees.`job_id`
GROUP BY job_title
ORDER BY COUNT(*) DESC;

# 案列9: 三表连接,查询员工名,部门名和所在的城市,且城市首字母为S
SELECT last_name,department_name,city
FROM employees,departments,locations
WHERE employees.`department_id` = departments.`department_id` 
AND departments.`location_id` = locations.`location_id`
AND city LIKE 'S%';

# 2. 非等值连接
# 案例1: 查询员工的工资和工资级别

CREATE TABLE job_grades
(grade_level VARCHAR(3),
lowest_sal INT,
highest_sal INT);

INSERT INTO job_grades
VALUES ('A',1000,2999);

INSERT INTO job_grades
VALUES ('B',3000,5999);

INSERT INTO job_grades
VALUES ('C',6000,9999);

INSERT INTO job_grades
VALUES ('D',10000,14999);

INSERT INTO job_grades
VALUES ('E',15000,24999);

INSERT INTO job_grades
VALUES ('F',25000,40000);

SELECT last_name,salary,grade_level
FROM employees AS e,job_grades AS j
WHERE salary BETWEEN j.`lowest_sal` AND j.`highest_sal`;

# 3. 自连接
# 案例: 查询员工名和上级名称
SELECT e.employee_id,e.last_name,m.employee_id,m.last_name
FROM employees e,employees m
WHERE e.`manager_id` = m.`employee_id`;

# sql99语法
/*
语法:
	select 查询列表
	from 表1 别名 [连接类型]
	join 表2 别名
	on 连接条件
	[where 筛选条件]
	[group by 分组]
	[having 筛选条件]
	[order by 排序列表]

内连接(*):inner
外连接
	左外(*):left
	右外(*):right
	全外:full
交叉连接:cross

*/

# 内连接
/*
select 查询列表
form 表1 别名
inner join 表2 别名
on 连接条件

分类:
等值
非等值
自连接

*/

# 1. 查询员工名,部门名
SELECT last_name,department_name
FROM employees e,departments d
WHERE e.`department_id` = d.`department_id`;

SELECT last_name,department_name
FROM employees e
INNER JOIN departments d
ON e.`department_id` = d.`department_id`;

# 2. 查询名字中包含e的员工名和工种名(筛选)
SELECT last_name,job_title 
FROM employees e,jobs j
WHERE e.`job_id` = j.`job_id`
AND last_name LIKE '%e%';

SELECT last_name,job_title
FROM employees e
INNER JOIN jobs j
ON e.`job_id` = j.`job_id`
WHERE last_name LIKE '%e%';

# 3. 查询部门个数>3的城市名和部门个数(分组+筛选)
SELECT city,COUNT(*) 部门个数
FROM locations l,departments d
WHERE l.`location_id` = d.`location_id`
GROUP BY city
HAVING 部门个数>3;

SELECT city,COUNT(*) 部门个数
FROM locations l
INNER JOIN departments d
ON l.`location_id` = d.`location_id`
GROUP BY city
HAVING 部门个数>3;

# 4. 查询哪个部门的部门员工个数>3的部门名和员工个数,并按个数降序
SELECT department_name,COUNT(*) 员工个数
FROM departments d,employees e
WHERE d.`department_id` = e.`department_id`
GROUP BY d.department_name
HAVING 员工个数>3
ORDER BY 员工个数 DESC;

SELECT department_name,COUNT(*) 员工个数
FROM departments d
INNER JOIN employees e
ON d.`department_id` = e.`department_id`
GROUP BY department_name
HAVING 员工个数>3
ORDER BY 员工个数 DESC;

# 5. 查询员工名,部门名,工种名,并按照部门名降序
SELECT last_name,department_name,job_title
FROM employees e,departments d,jobs j
WHERE e.`department_id` = d.`department_id`
AND e.`job_id` = j.`job_id`
ORDER BY department_name DESC;

SELECT last_name,department_name,job_title
FROM employees e
INNER JOIN departments d ON e.`department_id` = d.`department_id`
INNER JOIN jobs j ON e.`job_id` = j.`job_id`
ORDER BY department_name DESC;

# 非等值连接
# 查询员工的工资级别
SELECT last_name,salary,grade_level
FROM employees AS e
JOIN job_grades AS j
ON salary BETWEEN j.`lowest_sal` AND j.`highest_sal`;

SELECT grade_level,COUNT(*) 个数
FROM employees AS e
JOIN job_grades AS j
ON salary BETWEEN j.`lowest_sal` AND j.`highest_sal`
GROUP BY grade_level
HAVING 个数>15
ORDER BY 个数 DESC;


# 自连接,查询员工和上级的姓名
SELECT e.`last_name`,m.`last_name`
FROM employees AS e
JOIN employees AS m
ON e.`manager_id` = m.`employee_id`;

# 外连接
/*

应用场景:查询一个表中有一个表中没有的内容(主从关系)
特点:
1. 外连接的查询结果为主表中的所有记录
	如果从表中有和它匹配的,则显示匹配的值
	如果从表中没有和它匹配的,则显示null
	外连接查询结果=内连接结果+主表中有而从表中没有的记录
2. 左外连接,left join左边是从表
   右外连接,right join右边是从表
3. 左外和右外交换两个表的顺序可以实现相同效果
4. 全外连接=内连接+表1中有但表2没有+表2中有但表1中没有
5. 交叉连接:使用99语法实现笛卡尔乘积.
*/
# 引入:查询男友不再男生表的女生
SELECT * FROM beauty;
SELECT * FROM boys;

SELECT be.name
FROM beauty be
LEFT OUTER JOIN boys bo ON be.`boyfriend_id` = bo.`id`
WHERE bo.id IS NULL;

# 案例1:查询哪个部门没有员工
SELECT department_name
FROM departments d
LEFT OUTER JOIN employees e
ON d.`department_id`=e.`department_id`
WHERE e.`employee_id` IS NULL;

# 全外连接
# mysql不支持
SELECT b.*,boys.*
FROM beauty b
FULL OUTER JOIN boys
ON b.`boyfriend_id` = boys.`id`;

# 交叉连接
SELECT b.*,bo.*
FROM beauty b
CROSS JOIN boys bo;

# sql92 sql99
# 功能:sql99支持较多
# 可读性:sql99实现连接条件的分离,可读性较高

# 案例一:查询编号>3的女生的男友信息,如果有则列出详细,没有用null填充
SELECT beauty.`name`,boys.*
FROM beauty
LEFT OUTER JOIN boys
ON beauty.`boyfriend_id` = boys.`id`
WHERE beauty.`id`>3;

# 案例二:查询哪个城市没有部门
SELECT city
FROM locations
LEFT OUTER JOIN departments
ON locations.`location_id` = departments.`department_id`
WHERE departments.`department_id` IS NULL;

# 案例三:查询部门名为SAL或IT的员工信息
SELECT department_name,employees.*
FROM employees
JOIN departments
ON employees.`department_id` = departments.`department_id`
WHERE departments.`department_name` = 'SAL' OR departments.`department_name` = 'IT';
