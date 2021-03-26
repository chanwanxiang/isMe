from django.conf.urls import url
from books.views import index,detail

urlpatterns = [
    # name给url起名,可以通过name找到这个路由
    url(r'^index/$',index,name='index'),
    # 分组获取正则数据,位置参数
    # http:127.0.0.1/categoryid/bookid/
    # url(r'^(\d+)/(\d+)/$',detail),
    # 分组获取正则数据,关键字参数
    # http:127.0.0.1/categoryid=?
    url(r'^(?P<categoryid>\d+)/(?P<bookid>\d+)/$',detail),
]