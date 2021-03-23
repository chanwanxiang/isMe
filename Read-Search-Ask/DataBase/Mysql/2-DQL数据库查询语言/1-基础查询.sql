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
SELECT salary AS out put FROM employees;

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
