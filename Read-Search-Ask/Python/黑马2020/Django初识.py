# Django框架
#     封装    大量的功能封装
#     简化    把相对负责的功能进行封装后做到简化
#     优化    py代码代码优化提升效率
#     漏洞    弥补了已知网站的传输漏洞,比如sql注入
#     管理    框架以模块划分,负责不同的功能,清晰易于管理

# 关于网站框架的MVC结构
#     M = Model       模型,控制数据库表结构
#     V = View        视图,负责具体前端输出内容,如颜色,文字,表单等
#     C = Controller  控制器,具体负责实现的功能,如加减乘除,增删改查

#     ROUTER 路由
#         用户访问地址,通过ROUTER映射到控制器(Controller)功能

#     Template 渲染模板
#         用户要看到页面的内容对应了View

# Django框架的MVC
#     标准MVC                     DjangoMVC
#     Model           模型        Model 
#     View            视图        Template
#     Controller      控制器      View

# Django框架的MVC流程
#     用户 -> 发出访问请求 -> (Nginx|Apatch)服务器 -> Django(Router-View(Controller)-Model-Template[渲染所有代码]) --> 浏览器展示的内容  --> 用户

# Django入门命令以及设置
#     1. 创建Django工程       django-admin startproject mains
#     2. 在工程下创建App       python manage.py startapp addNum
#     3. 创建库表             python manage.py makemigrations
#     4. 执行库表建立          python manage.py migrate
#     5. 模板渲染嵌入语法       在HTML中可以嵌入后台语言区分符号 --> {%命令%} {{变量}}

#     6. Django时间设置
#     7. Django App添加
#     8. Templates 目录设置(App目录下,需要单独创建)

