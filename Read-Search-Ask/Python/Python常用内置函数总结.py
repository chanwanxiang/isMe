## 数学相关

# 取绝对值
print(abs(-1))  #1

# 取最大/小值
print(min([1,2]))  #1
print(max([1,2]))  #2

# 四舍五入
print(round(2.5))  #3

## 类型转换

# 返回x对应的字符
print(chr(65))  #A

# 返回字符对应的ASC码数字编号
print(ord('A'))  #A

# isinstance() 函数来判断一个对象是否是一个已知的类型,返回布尔值
print(isinstance(1,int))  #True

# type()不会认为子类是一种父类类型,不考虑继承关系
# isinstance()会认为子类是一种父类类型,考虑继承关系

## 字符串处理

# eval()函数用来执行一个字符串表达式,并返回表达式的值
print(eval('2*3'))  #6

# 首字母大写 str.capitalize
print('is'.capitalize())  #Is

# 字符串替换 str.replace
print('is'.replace('s','S'))  #iS

# 字符串切割 str.split
print('is Me'.split(' '))  #['is', 'Me']

## 序列处理

# enumerate() 函数用于讲一个可遍历对象(如列表,元祖或者字符串)组合为一个索引序列,同时列出数据和数据下标,一般用在for循环中,返回一个enumerate对象

nums = [1,2,3,4]

print(enumerate(nums))  #<enumerate object at 0x000001AF6B13EAF8>

for i,j in enumerate(nums):
    print(i,j)

## 字典函数

# dict.get(Key,default=None),返回指定键的值,如果键不在字典中范湖默认值为None或者设置的默认值

# 输出一个序列中字符的个数
# seq = 'LIFE IS SHORT I USE PYHOTN'

# dc = dict()

# for i in seq:
#     dc[i] = dc.get(i,0) + 1

# print(dc)  #{'L': 1, 'I': 3, 'F': 1, 'E': 2, ' ': 5, 'S': 3, 'H': 2, 'O': 2, 'R': 1, 'T': 2, 'U': 1, 'P': 1, 'Y': 1, 'N': 1}