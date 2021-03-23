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

#TODO: 字符函数

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

#TODO: 数学函数

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


#TODO: 其他函数
SELECT VERSION();
SELECT DATABASE();
SELECT USER();
SELECT PASSWORD();

#TODO: 流程控制函数
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

#TODO: 分组函数
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
