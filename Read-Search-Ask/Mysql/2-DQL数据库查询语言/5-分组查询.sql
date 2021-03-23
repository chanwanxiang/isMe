# 分组查询
/*

语法:
	SELECT 分组函数,列(要求出现在group by后面)
	from 表
	[where 筛选条件]
	group by 分组的列表
	[order by 子句]
	
注意:
	查询列表必须特殊,要求是分组函数和group by后出现的字段

特点:
	1. 分组查询中的筛选条件分为两类
		数据源:			位置			关键字
	分组前筛选:原始表		group by 语句之前	where
	分组后筛选:分组后的结果集	group by 语句之后	having

	1,分组函数做条件肯定放在having子句中
	2,能用分组前筛选的尽量使用分组前筛选
	
	2. group by子句支持单个字段分组,多个字段分组(多个字段使用逗号隔开)
	3. 添加排序放在整个分组查询之后
*/

# 案例:查询每个组的平均工资
SELECT AVG(salary),department_id FROM employees GROUP BY department_id;

# 案例:查询每个工种的最高工资
SELECT MAX(salary) AS 最高工资,job_id
FROM employees
GROUP BY job_id;

# 案例: 查询每个位置上的部门个数
SELECT COUNT(*),location_id
FROM departments
GROUP BY location_id;

# 案例:查询邮箱中包含0字符的,每个部门的平均工资
SELECT AVG(salary),department_id,email
FROM employees
WHERE email LIKE '%a%'
GROUP BY department_id;

# 案例:查询有奖金的每个领导下属员工最高工资
SELECT MAX(salary),manager_id
FROM employees
WHERE commission_pct IS NOT NULL
GROUP BY manager_id;

# 添加复杂筛选条件
# 案例:查询部门员工个数大于2(分组后的结果(having))
#	1. 查询每个部门员工个数
SELECT COUNT(*),department_id FROM employees GROUP BY department_id;
#	2. 根据1的结果进行筛选,查询那个部门员工个数大于2
SELECT COUNT(*),department_id FROM employees GROUP BY department_id HAVING COUNT(*)>2;

# 案例:查询每个工种有奖金的员工的最高工资>12000的工种编号和最高工资
# 1. 查询每个工种有奖金的员工的最高工资
SELECT MAX(salary),job_id FROM employees WHERE commission_pct IS NOT NULL GROUP BY job_id HAVING MAX(salary)>12000;
# 2. 根据1的结果继续筛选,最高工资大于12000

# 案例: 查询领导编号>102的每个领导手下最低工资>5000的领导编号,以及其最低工资
SELECT manager_id,MIN(salary) FROM employees WHERE manager_id>102 GROUP BY manager_id HAVING MIN(salary)>5000;

# 按表达式分组
# 案例:按员工姓名的长度分组,查询每一组员工个数,筛选员工个数>5的
SELECT LENGTH(last_name),COUNT(*) FROM employees GROUP BY LENGTH(last_name) HAVING COUNT(*)>5;

# 按多个字段分组
# 案例:查询每个部门,每个工种的平均工资
SELECT department_id,job_id,AVG(salary) FROM employees GROUP BY department_id,job_id;

# 添加排序
SELECT department_id,job_id,AVG(salary)
FROM employees 
WHERE department_id IS NOT NULL
GROUP BY department_id,job_id
HAVING AVG(salary) > 12000
ORDER BY AVG(salary);
