# Django介绍

# 1. 简介
#     Django makes it easier to build better web apps more quickly and with less code

# 2. 特点

#     1)重量级框架
#         提供了项目工程管理的自动化脚本工具
#         数据库ORM支持(对象关系映射:object relational mapping)
#         模板
#         表单
#         Adimin管理站点
#         文件管理
#         认证权限
#         session机制
#         缓存

#     2) MVC(Model-View-Controller)和MTV模式
#         标准MVC                                                         DjangoMTV
#         M:model,主要是封装对数据库层的访问,对数据中的数据进行增删改查操作         M       
#         V:view,用于封装结果,生成页面展示的html,css,js内容                    T
#         C:controller,用于接收请求,处理业务逻辑,与model和view交互,返回结果      V

# 虚拟环境

#     为什么要搭建虚拟环境?
#         在开发过程中,当需要使用python的某些工具包/框架时需要联网安装
#             如联网安装Django框架的django的1.0.0版本
#             sudo pip install django==1.0.0

#     如果在一台电脑上,想开发多个不同的项目,需要用到一个包的不同版本,如果使用上面命令,在同一个目录下安装或者更新,新版本会覆盖以前的版本,其他的项目就无法运行了
#     虚拟环境
#         作用可以搭建独立的python运行环境,使得单个项目的运行环境与其他项目互不影响
#         所有的虚拟环境都为与/home/下的隐藏目录.virtualenvs下

# 如何搭建虚拟环境?

#     linux
#     安装虚拟环境命令
#         sudo pip install virtualenv
#         sudo pip install virtualenvwrapper

#     安装完虚拟环境后,如果提示找不到mkvirtualenv命令,须配值环境变量
#         1)创建目录来存放虚拟环境
#             mkdir
#             $HOME/.virtualenvs
