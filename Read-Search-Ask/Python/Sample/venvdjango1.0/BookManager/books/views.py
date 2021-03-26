from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from books.models import BookInfo
from django.urls import reverse
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
    name = request.META['HTTP_NAME']
    print(name,contenttype)

    return HttpResponse('deteail')
