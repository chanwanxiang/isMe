# web框架专门处理动态资源请求

import sys
import time
import os.path as op

# 路由列表手动添加路由 Django路由
routelist = [
    # ('/index.html', index),
    # ('/center.html', center),
]

# 带参数装饰器添加路由 Flask路由
def route(path):
    # 装饰器
    def decorator(func):
        # 当执行装饰器的时候就需要把路由添加到路由列表里
        # 装饰函数时候只需添加一次路由
        routelist.append((path,func))
        def inner():
            result = func()
            return result

        return inner
    # 返回一装饰器
    return decorator

# 首页数据
@route('/index.html') # 
def index():
    # 状态信息
    status = '200 OK'
    # 响应头
    responseheader = [('Server', 'PWS/1.1')]
    # 1. 打开指定模板文件,读取模板文件中的数据
    with open(file=op.join(sys.path[0], 'template/index.html'), mode='r', encoding='utf-8') as f:
        filedata = f.read()
    # 2. 查询数据库,模板里面的模板变量{%content%}替换成以后从数据库里查询的数据
    # web框架处理后的数据
    # 获取当前时间
    data = time.ctime()
    responsebody = filedata.replace('{%content%}', data)
    # 返回的是元祖
    return status, responseheader, responsebody

# 个人中心数据
@route('/center.html')
def center():
    # 状态信息
    status = '200 OK'
    # 响应头
    responseheader = [('Server', 'PWS/1.1')]
    # 1. 打开指定模板文件,读取模板文件中的数据
    with open(file=op.join(sys.path[0], 'template/center.html'), mode='r', encoding='utf-8') as f:
        filedata = f.read()
    # 2. 查询数据库,模板里面的模板变量{%content%}替换成以后从数据库里查询的数据
    # web框架处理后的数据
    # 获取当前时间
    data = time.ctime()
    responsebody = filedata.replace('{%content%}', data)
    # 返回的是元祖
    return status, responseheader, responsebody

# 404数据
def notFound():
    # 状态信息
    status = '404 NOT FOUND'
    # 响应头
    responseheader = [('Server', 'PWS/1.1')]
    # web框架处理后的数据
    data = '404 NOT FOUND'
    # 返回的是元祖
    return status, responseheader, data

def handleRuquest(env):
    # 获取动态请求资源路径
    requestpath = env['requestpath']
    print('动态资源请求地址:', env['requestpath'])
    # 判断请求动态资源路径,选择指定函数处理对应动态资源请求

    # 遍历路由列表,匹配请求url
    for path, func in routelist:
        print(path, func)
        if requestpath == path:
            # 找到指定路由,执行对应处理函数
            result = func()
            return result
    else:
        # 没有动态资源数据,返回404状态信息
        result = notFound()
        return result

if __name__ == '__main__':
    print(routelist)
