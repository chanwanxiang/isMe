# 字典
# 统计一个字符串中每个字符的个数

str = 'BEAUTIFUL THING NEVER ASK FOR ATTENTION'

dt = dict()

# 方法一
# for i in str:
#     if i not in dt.keys():
#         dt[i] = 1
#     else:
#         dt[i] += 1

# 方法二
for i in str:
    # dt.get(key,default=None) 返回指定键的值,如果键的值不存在是,返回该默认值
    dt[i] = dt.get(i, 0) + 1

print(dt)
