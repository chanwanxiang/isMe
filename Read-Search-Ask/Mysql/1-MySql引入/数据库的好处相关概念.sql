# mysql引入

# 数据库的好处
#     1. 持久化数据到本地
#     2. 可以实现结构化查询,方便管理

# 数据库的相关概念
#     DB:数据库(database):存储数据的“仓库”,它保存了一系列有组织的数据。
#     DBMS:数据库管理系统(Database Management System)。数据库是通过DBMS创建和操作的容器。
#     SQL:结构化查询语言(Structure Query Language),专门用来与数据库通信的语言。

# mysql常用命令
#     命令行登录数据库指定gbk格式防止命令行乱码:mysql -u root -p123456 --default-character-set=gbk
#     查看当前所有的数据库:show databases;
#     打开指定的库:use 库名;
#     查看当前的所有表:show tables;
#     查看其他库的所有表:show tables from 库名;
#     创建表:
#     create table 表名(
#     ​ 列名 列类型,
#     ​ 列名 列类型,
#     ​ …
#     );
#     查看表结构:desc 表名;

# mysql语法规范
#     1.不区分大小写,建议关键字大写,表名、列名小写
#     2.每句话用;或\g结尾
#     3.每条命令根据需要,各子句一般分行写,关键字不能缩写也不能分行
#     4.注释
#         单行注释:#注释文字
#         单行注释:-- 注释文字(要有空格)
#         多行注释:/* 注释文字 */
