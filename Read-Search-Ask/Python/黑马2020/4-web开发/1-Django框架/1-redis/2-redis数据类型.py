# 服务端客户端命令

# 服务端

#     服务器端的命令为redis-server
#     可以使用help查看帮助文档
#         redis-server --help

#     个人习惯
#         ps aux | grep redis 查看rdis服务进程
#         kill -9 pid         杀死redis服务

# 客户端

#     客户端的命令为redis-cli
#     可以使用help查看帮助文档
#         redis-cli --help

#     连接redis
#         redis-cli

#     运行测试命令
#         ping

#     切换数据库
#         数据看没有名称,默认16个,通过0-15标识,连接redis默认选择第一个数据库
#             select 10

# 数据操作

#     数据结构
#         redis是key-value的数据结构,每条数据都是一个键值对
#         键的类型是字符串
#         TODO: 键不能重复

#         值的类型分为五种:
#             字符串  string
#             哈希    hash
#             列表    list
#             集合    set
#             有序集合 zset
        
#     数据操作行为

#         1. 保存
#             如果设置的键不存在则为添加,已经存在则是修改

#             设置键值
#                 set key value
#                 例: 设置键为name值为mass数据
#                     set name mass
#             设置键值及过期的时间
#                 setex key secconds value
#                 例: 设置键为aaaa值为bbbb过期时间3秒数据
#                     setex aaaa 3 bbbb
#             设置多个键值
#                 mset key1 value1 key2 value2...
#                 例: 设置键为a1值为python,键为a2值为java,键为a3值为c++
#                     mset a1 python a2 java a3 c++
#             追加值
#                 append key value
#                 例: 向键为a1中追加值ic
#                     append a1 ic

        2. 获取
            根据键获取值,如果不存在此键则返回nil
                get key
                例: 获取键name的值
                    get name
            
            根据多个键获取多个值
                mget key1 key2...
                    例: 获取键a1,a2,a3的值
                        mget a1 a2 a3

        3. 修改           
                    

        4. 删除