B站地址:https://www.bilibili.com/video/BV12b411K7Zu?from=search&seid=11400090157120907821

#进阶1:基础查询
/*
语法:
select 查询列表 
from 表名;

特点:
1. 查询列表可以是:表中的字段,常量值,表达式,函数
2. 查询的结果是一个虚拟的表格
*/

USE myemployees;

#1. 查询单个字段
SELECT last_name FROM employees;

#2. 查询表中多个字段
SELECT last_name,salary,email FROM employees;

#3. 查询表中的所有字段
SELECT * FROM employees;

#4. 查询常量值
SELECT 100;
SELECT 'mars';

#5. 查询表达式
SELECT 100%98;

#6. 查询函数
SELECT VERSION();

#7. 起别名

# 方式一
SELECT 100%98 AS 结果;
SELECT last_name AS 姓,first_name AS 名 FROM employees;
# 方式二
SELECT last_name 姓,first_name 名 FROM employees;

# 案例:查询salary,显示结果为out put
SELECT salary AS 'out put' FROM employees;

#8. 去重
# 案例:查询员工表中设计到所有的部门编号
SELECT DISTINCT department_id FROM employees;

#9. +号的使用 
/*
mysql中的+号仅仅只有一个功能:运算符
select 100+90;
select '123'+90;其中一个为字符型,视图将字符型转换为数值型,如果转换成功,则继续做加法运算
如果转换失败,则将字符型数值转换为0
*/
# 案例:查询员工名和姓连接成一个字段,并显示为姓名
SELECT CONCAT(last_name,first_name) AS '姓名' FROM employees;

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

# 进阶4:常见函数
/*

概念:类似java中的方法,将一组逻辑语句封装在方法体中,对外暴露方法名
好处:1. 隐藏了实现细节 2. 提高代码复用性

调用:select 函数名() form 表;

特点:
	1.叫什么(函数名)
	2.干什么(函数功能)
分类:
	1. 单行函数
	如:concat,length,ifnull等
	2. 分组函数
	功能:做统计使用,又称为统计函数,聚合函数,组函数

*/

#1, 字符函数

# length() 获取参数值的字节个数

SELECT LENGTH('mars');
SELECT LENGTH('张三s');

# concat 拼接字符串
SELECT CONCAT(last_name,'_',first_name) AS 姓名 FROM employees;

# upper,lower
SELECT UPPER('John');
SELECT CONCAT(UPPER(last_name),LOWER(first_name)) AS 'Name' FROM employees;

# substr,substring 索引从1开始
# 截取从指定索引处后面所有字符
SELECT SUBSTR('李莫愁爱上了陆展元',7) AS output;
# 截取从指定索引处指定字符长度的字符
SELECT SUBSTR('李莫愁安上了陆展元',1,3) AS output;

# 案例:姓名中首字符大写,其他字符小写,然后拼接
SELECT CONCAT(UPPER(SUBSTR(last_name,1,1)),'_',LOWER(SUBSTR(last_name,2))) AS 'Nanme' FROM employees;

# instr 返回子串第一次出现的索引,如果找不到返回0
SELECT INSTR('杨不悔爱上了殷六侠','殷六侠') AS out_put;

# trim 去前后空格
SELECT TRIM('  张 珊  ') AS out_put;
SELECT TRIM('o' FROM 'oooo张oooo删oooo') AS out_put;

# lpad 用指定字符实现左填充指定长度
SELECT LPAD('殷素素',10,'*') AS out_put;

# rpad 用指定字符实现右填充指定长度
SELECT RPAD('殷素素',10,'*') AS out_put;
# replace 替换
SELECT REPLACE('张无忌爱上了周芷若','周芷若','西瓜') AS out_put;

# 数学函数

# round 四舍五入
SELECT ROUND(-1.55) AS out_put;
SELECT ROUND(1.427,2) AS out_put;

# ceil 向上取整
SELECT CEIL(-1.02);

# floor 向下取整
SELECT FLOOR(9.99);

# truncate 截断
SELECT TRUNCATE(1.65,1);

# mod 取余
SELECT MOD(10,3); a - a/b*b
SELECT MOD(-10,-3);

# 日期函数
# now 返回当前系统日期+时间
SELECT NOW();
# curdate 返回当前系统时间,不包含日期
SELECT CURDATE();
SELECT CURTIME();

# 可以获取指定的部分,年,月,日,时,分,秒
SELECT YEAR(NOW()) AS 年;
SELECT YEAR('1998-1-1') AS 年;
SELECT YEAR(hiredate) FROM employees;

SELECT MONTH(NOW()) AS 月; # 12
SELECT MONTHNAME(NOW()) AS 月; # December

# str_to_data 将字符通过指定格式转换成日期
SELECT STR_TO_DATE('1998-3-2','%Y-%c-%d') AS out_put;

# 查询入职日期为1992-4-3的员工信息
SELECT * FROM employees WHERE hiredate = '1992-4-3';

SELECT * FROM employees WHERE hiredate = STR_TO_DATE('4-3 1992','%c-%d %Y');

# date_format:将日期转换为字符
SELECT DATE_FORMAT(NOW(),'%y年%m月%d日') AS out_put;

# 查询所有奖金的员工名和入职日期(xx月/xx日 xx年)
SELECT last_name,DATE_FORMAT(hiredate,'%m月/%d日 %y年') AS 入职时间 FROM employees;


# 其他函数
SELECT VERSION();
SELECT DATABASE();
SELECT USER();
SELECT PASSWORD();

# 流程控制函数
# if函数 if else效果
SELECT IF(10>5,'大','小') AS 输出;
SELECT last_name,commission_pct,IF(commission_pct IS NULL,'没有奖金','拥有奖金') FROM employees;

# case函数的使用: switch case效果
/*
1,
case 要判断的字段或表达式
when 常量1 then 要显示的值或语句
when 常量2 then 要显示的值或语句
................................
;
2,
case 
when 条件1 then 要显示的值或语句
when 条件2 then 要显示的值或语句
................................
;
*/

# 案例:查询员工的工资,要求
# 部门号=30,显示工资为1.1倍
# 部门号=40,显示工资为1.2倍

SELECT salary AS 原始工资,department_id,
CASE department_id
WHEN 30 THEN salary*1.1
WHEN 40 THEN salary*1.2
END AS 新的工资
FROM employees;

# 案例:查询员工的工资情况
# 如果工资>20000,显示A级别
# 如果工资>15000,显示B级别
# 如果工资>10000,显示C级别
# 否则,显示B级别

SELECT salary,
CASE
WHEN salary>15000 THEN 'A'
WHEN salary>12000 THEN 'B'
WHEN salary>10000 THEN 'C'
ELSE 'D'
END AS '工资级别'
FROM employees;

# 分组函数
/*
功能:用作统计使用,又称为聚合函数或同级函数或组函数

分类: sum(),avg(),max(),min(),
count()返回非空值的个数

特点:
1. sum,avg一般用于处理数值型
	max,min,count可以处理任何类型
2. 以上函数都忽略null值

3. 可以和distinct搭配去重使用

4. conunt函数的单独介绍
	一般使用count(*)来统计结果集的行数
	
5. 和分组函数一同查询的字段要求是group by后的字段

*/

SELECT SUM(salary) FROM employees;
SELECT AVG(salary) FROM employees;
SELECT MAX(salary) 最大,MIN(salary) 最小,COUNT(salary) 计数 FROM employees;

# 和distinct搭配
SELECT SUM(DISTINCT salary),SUM(salary) FROM employees;
SELECT COUNT(DISTINCT salary),COUNT(salary) FROM employees;

# count函数的详细介绍 返回表中的所有行
SELECT COUNT(*) FROM employees;
SELECT COUNT(1) FROM employees;

# 和分组函数一通查询的字段有限制
SELECT AVG(salary),employee_id FROM employees;

# 案例:查询员工表中最大入职时间和最小入职时间的相差天数(diffrence)
SELECT MAX(hiredate)AS 最大入职时间,MIN(hiredate) AS 最小入职时间,DATEDIFF(MAX(hiredate),MIN(hiredate)) AS 入职相差时间 FROM employees;

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

# 进阶7:子查询
/*
定义:出现在其他语句中的select语句,成为子查询或内查询
外部的查询语句,成为主查询或外查询

分类:
按子查询出现的位置:
	select 后面:
		标量子查询
	from 后面:
		支持表子查询
	where 或 having后面:☆
		标量子查询(单行) √
		列子查询(多行) √
		行子查询
	exists后面(相关子查询):
		表子查询
按结果集的行列数不同:
	标量(结果集只有一行一列)
	列子查询(结果姐只有一列多行)
	行子查询(结果集有多行多列)
	表子查询(结果集一般多行多列)
*/


# 一. where或having后面
# 1. 标量子查询(单行子查询)