from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from books.models import BookInfo
from django.urls import reverse
from django.shortcuts import redirect
import json

# Create your views here.

def index(request):
    # def render(request, template_name, context=None, content_type=None, status=None, using=None):
    # 参数1 当前请求
    # 参数2 模板文件
    # 参数3 传递参数

    # 实现业务逻辑
    #     到数据库查询数据
    #     组织数据
    #     传递模板

    # 把所有书籍查询出来
    # objects可以理解为模型的管理类,对模型的增删改查依赖于它
    books = BookInfo.objects.all()
    context = {
        'books':books
    }

    # 页面展示错误信息
    # result = 10 / 0

    # 路由命名及reverse反解析
    # path = reverse('books:index')
    # return redirect(request,path,context)

    return render(request,'books/index.html',context)


def detail(request,categoryid,bookid):
    # GET请求
    # # 位置,关键字参数进行传参匹配
    # print(categoryid,bookid)
    # params = request.GET
    # # 获取一键多值 QueryDict .getlist方法
    # username = params.getlist('username')
    # # 获取一键一值 .get方法
    # password = params.get('password')
    # print(username,password)

    # # POST请求 Form Date
    # params = request.POST
    # print(params)

    # # POST请求 Non-Form Data
    # # JSON形式的字符串
    # body = request.body.decode()
    # # 转换为字典,方便数据操作
    # data = json.loads(body)
    # # JSON
    # #     json.dumps      将字典转换为JSON形式的字符串
    # #     json.loads      将JSON形式的字符串转换为字典
    # print(data)

    # 请求头
    contenttype = request.META['CONTENT_TYPE']
    # POSTMAN添加name参数
    # name = request.META['HTTP_NAME']
    # print(name,contenttype)

    # HttpResponse
    # content           只传递字符串,不要传递对象字典数据,可以使用jsonResonse直接传递字典
    # statue            HTTP statues code must be an integer frmo 100 to 599
    # content-type      语法形式为大类/小类的MIME类型,形如text/html,text/css,text/javascript,application/json,image/png,image/gif等

    return redirect('http://www.baidu.com')
    return HttpResponse('deteail',status=200)

def setCookie(request):
    # 1)浏览器第一次请求服务器未携带任何cookie信息
    # 2)服务器接收到没有cookie信息的请求,设置一个cookie携带在响应中
    # 3)浏览器接收到携带cooike信息的响应,浏览器保存cookie信息到本地中


    # 判断有无cookie信息

    # 获取用户信息
    username = request.GET.get('username')
    # 服务器设置cookie信息
    response = HttpResponse('setCookie')
    response.set_cookie('username',username)

    return response

def getCookie(requeset):
    # 4)浏览器再次向服务器发送携带cookie信息的请求
    # 5)服务器接收到携带cookie信息的请求,实现状态保持

    # 服务器接收和查看cookie信息
    cookies = requeset.COOKIES
    # cookies是一个字典
    username = cookies.get('username')
    # 得到用户信息进行其他操作
    print(username)

    return HttpResponse('getCookie')
