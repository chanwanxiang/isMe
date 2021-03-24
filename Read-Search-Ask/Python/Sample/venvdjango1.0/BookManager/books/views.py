from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from books.models import BookInfo

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
    # result = 10 / 0

    return render(request,'books/index.html',context)
