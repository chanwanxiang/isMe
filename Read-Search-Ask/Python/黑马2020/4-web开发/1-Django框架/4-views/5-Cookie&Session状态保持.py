# 状态保持
#     浏览器请求服务器是无状态的
#     无状态指一次用户请求时,浏览器与服务器无法知道之前这个用户做过什么,每次请求都是一次新的请求
#     无状态原因是浏览器与服务器是使用Socket套接字进行通信的,服务器将请求结果返回给浏览器后,会关闭当前Socket连接
#         而且服务器也会在处理页面完毕后销毁页面对象
#     要保持下来用户浏览的状态,比如用户是否登录,浏览过哪些商品等,实现状态保持主要有两种方式
#         1)在客户端存储信息用Cookie
#         2)在服务端存储信息用Session

# Cookie
#     Cookie,有时也用其复数形式Cookies,指网站为了辨别用户身份,进行Session跟踪而存储在用户本地终端上的数据(通常经过加密)
#     Cookie是由服务器生成,发送给User-Agent(一般是浏览器),浏览器会将Cookie的key/value保存到本地的文本文件内,下次请求同一网站时就发送改Cookie给服务器
#     Cookie的名称和值可以有服务器开发自己定义,这样服务器可以知道该用户是否是合法用户以及是否需要重新登录
#     服务器可以利用Cookie包含信息的任意性来筛选并经常维护这些信息,以判断HTTP传输中的状态,Cookie最典型应用在记住用户ID
#     TODO:
#         Cookie是存储在浏览器中的一段纯文本信息,建议不要存敏感信息如密码,应为浏览器可能被其他人使用

# Cookie的特点
#     Cookie以键值对的格式进行信息的存储
#     Cookie基于域名安全,不同域名的Cookie是不能相互访问的
#     当浏览器请求某网站时,会将浏览器存储的跟网站相关的所有Cookie信息提交给网站服务器

# 设置Cookie
#     通过HttpResonse对象中的set_cookie方法设置Cookie
#         HttpResponse.set_cookie(cookie名,value=cookie值,max_age=cookie有效期)
#         max_age单位为秒,默认为None,如果是临时cookie,可将max_age设置为None

# 读取Cookie
#     通过HttpResonse对象中的COOKIES属性来读取本次请求携带的cookie值,request.COOKIES为字典类型
#         def cookie(requeset):
#             cookieName = requeset.COOKIES.get('username')

# 删除Cookie
#     可以通过HttpResponse对象中的delete_cookie方法来删除
#         response.delete_cookie('username')

# Session
#     django默认启用Session,可在setting.py文件配置

# Session存储方式
#     保存在数据库或者本地缓存,可在setting.py文件配置
#         1)数据库为默认存储方式
#             Session表结构包括三个数据:键值过期时间
#         2)本地缓存
#             存储在本机缓存中,如果丢失则不能找回,比数据库方式读写更快
#         3)混合存储
#             优先从本机缓存中获取,如无则通过数据库查询
#             SESSION_ENGINE='django.contrib.sessions.backends.cached_db'
#         4)Redis
#             在Redis中保存Session,需要引入第三方扩展,可以使用django-redis解决
#                 安装扩展
#                     pip install django-redis
#                 配置setting.py
#                     CACHES = {
#                         'default': {
#                             'BACKEND': 'django_redis.cache.RedisCache',
#                             'LOCATION': 'redis://127.0.0.1:6379/1',
#                             'OPTIONS': {
#                                 'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#                             }
#                         }
#                     }
#                     SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
#                     SESSION_CACHE_ALIAS = 'default'

# Session操作
#     通过HttpRequest对象的session属性进行会话的读写操作
#         1)以键值对的形式写session
#             request.session['key'] = value
#         2)根据键读取值
#             request.session.get('key',defaultValue)
#         3)清空所有session,在存储中删除值的部分
#             request.session.clear()
#         4)清除session数据,在存储中删除session整条数据
#             request.session.flush()
#         5)删除session中的指定键及值,在存储中只删除某个键及对应的值
#             del request.session['key']
#         6)设置session的有效期
#             request.session.set_expiry(value)
#             如果value是一个整数,那么session将在value秒没有活动后过期
#             如果value为0,那么用户session的Cookie将在用户的浏览器关闭时过期
#             如果value为None,那么seesion有效期将采用系统默认值,默认为两周,可以通过setting.py中配置SESSION_COOKIE_AGE来设置全局默认值         
