# 进阶2:条件查询
/*
语法:
select 查询列表 from 表名 where 筛选条件;

分类:
	一,条件表达式筛选
	条件运算符:
		> < = != <> >= <= <=>安全等于
	二,逻辑表达式筛选
	逻辑运算符:
		&& || !
		and or not
	三,模糊查询
	like
	特点:
	1,一般和通配字符搭配使用
		% 任意多个字符,包含0个字符
		_任意单个字符
	between and
		1. 提高sql简洁度
		2. 包含临界值
		3. 两个临界值不可调换顺序
	in
		1.提高sql简洁度
	is null
		1. 仅仅可以判断null值
		<=>:既可以判断null值又可以判断数值
*/
# 案例1:查询工资>12000的员工信息
SELECT * FROM employees WHERE salary > 12000;

# 案例2:查询部门编号不等于90的员工和部门编号
SELECT * FROM employees WHERE department_id != 90;

# 案例3: 查询工资在10000到20000之间的员工名,工资以及奖金
SELECT last_name,salary,commission_pct FROM employees WHERE salary >= 10000 AND salary <= 20000;

# 案例4: 查询员工名字中包含字符a的员工信息
SELECT * FROM employees WHERE last_name LIKE '%a%';

# 案例5: 查询员工名中第三个字符为n,第5个字符为l的员工名和工资
SELECT last_name,salary FROM employees WHERE last_name LIKE '__n_l%';

# 案例6: 查询员工名第二个字符为_的员工名
SELECT last_name FROM employees WHERE last_name LIKE '_\_%';

# 案例7: between and 查询员工编号在100到120之间的员工信息

SELECT * FROM employees WHERE employee_id BETWEEN 100 AND 120;

# 案例8: 查询员工的工种编号是it_prog,ad_vp,ad_pres的员工名和工种编号
SELECT last_name,job_id FROM employees WHERE job_id IN ('IT_PROT','AD_VP','AD_PRES');

# 案例9: 查询没有奖金的员工名和奖金率
SELECT last_name,commission_pct FROM employees WHERE commission_pct IS NULL;
SELECT last_name,commission_pct FROM employees WHERE commission_pct IS NOT NULL;
