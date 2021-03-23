# Django介绍

# 简介
#     Django makes it easier to build better web apps more quickly and with less code

# 特点

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

#     windows
#         安装虚拟环境命令
#             virtaulenvwrapper是virtualenv的扩展包,用于更方便管理虚拟环境
#                 - 将所有虚拟环境整合在一个目录下
#                 - 管理(新增,删除,复制)虚拟环境
#                 - 快速切换虚拟环境
#             1)安装
#                 pip install virtualenvwrapper-win
#             2)修改创建圩您虚拟环境默认位置
#                 python安装目录下的Scripts目录修改mkvirtualenv.bat文件,修改24行信息
#             3)创建虚拟环境
#                 mkvirtualenv name
#             4)激活切换环境
#                 workon  [vnev]
#             5)安装指定版本django
#                 pip install django==1.11.11
#             6)创建django项目
#                 django-admin startproject name
#                 python manage.py runserver [127.0.0.1:8000]
#             7)创建django子应用
#                 python manager.py startapp name
#             8)退出虚拟环境
#                 deactivate

# 创建django项目
#     django-admin startproject 工程名称

# 工程目录说明
#     与项目同名的目录
#         settings.py         项目的整体配置文件
#         urls.py             项目的url配置文件
#         wsgi.py             项目与wsgi兼容的web服务器入口
#         manage.py           项目管理文件,通过它管理项目

# 运行开发服务器
#     django提供了一个纯python编写的轻量级web服务器,仅在开发近端使用
#     python manage.py runserver [ip:端口]
#     django默认工作在调试Debug模式下,如果有增删改查文件,服务器会自动重启
#     按ctrl+c停止服务

# 创建子应用
#     在开发过程中通常将工程项目拆分为不同的子功能模块,各功能模块之间可以保持相对独立,在其他项目中需要用到某个特定功能模块时,
#     可以将代码整体复制过去,达到复用
#     flask框架中类似子功能应用模块概念为蓝图Blueprint
#     django视图编写是放在子应用中的
#     python managy.py startapp 名称
