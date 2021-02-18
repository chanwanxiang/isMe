# Python语言特性

# 一. Python的函数参数传递
# 两个例子:
# 例1
a = 1
def funA(a):
    print('函数执行之前a内存地址->'+str(id(a)))  #函数执行之前a内存地址->140735206810256
    a = 2
    print('函数执行之后a内存地址->'+str(id(a)))  #函数执行之后a内存地址->140735206810288

funA(a)
print(a,id(a))  #1 140735206810256

# 例2
a = []
def funB(a):
    print('函数执行之前a内存地址->'+str(id(a)))  #函数执行之前a内存地址->2481546879624
    a.append(1)
    print('函数执行之后a内存地址->'+str(id(a)))  #函数执行之后a内存地址->2481546879624
funB(a)
print(a,id(a))  #[1] 2481546879624

# 所有的变量都可以理解是内存中一个对象的`引用`

# 通过id来看引用a的内存地址可以比较理解：

# 第1个例子可以看到,在执行完a = 2之后,a引用中保存的值,即内存地址发生变化,由原来1对象的所在的地址变成了2这个实体对象的内存地址

# 而第2个例子a引用保存的内存值就不会发生变化：

# 这里记住的是类型是属于对象的,而不是变量而对象有两种,'可更改'（mutable）与'不可更改'（immutable）对象在python中,strings, tuples, 和numbers是不可更改的对象,而 list, dict, set 等则是可以修改的对象(这就是这个问题的重点)

# 当一个引用传递给函数的时候,函数自动复制一份引用,这个函数里的引用和外边的引用没有半毛关系了.所以第一个例子里函数把引用指向了一个不可变对象,当函数返回的时候,外面的引用没半毛感觉.而第二个例子就不一样了,函数内的引用指向的是可变对象,对它的操作就和定位了指针地址一样,在内存里进行修改.

# 如果还不明白的话,这里有更好的解释: http://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference

# 二. @staticmethod 和 @classmethod
# Python其实有3个方法,即静态方法(staticmethod),类方法(classmethod)和实例方法,如下:

def foo(x):
    print('executing foo(%s)'%(x))

class A(object):
    def foo(self,x):
        print('executing foo(%s,%s)'%(self,x))
    @classmethod
    def classfoo(cls,x):
        print('executing classfoo(%s,%s)'%(cls,x))

    @staticmethod
    def staticfoo(x):
        print('executing staticfoo(%s)'%x)

a=A()
# 实例方法
a.foo(1)
# A.foo(1) #TypeError: foo() missing 1 required positional argument: 'x' 实例方法用 类.方法 不可以用
# 类方法
a.classfoo(1)
A.classfoo(1)
# 静态方法
a.staticfoo(1)
A.staticfoo(1)

# 这里先理解下方法参数里面的self和cls.这个self和cls是对类或者实例的绑定,对于一般的函数来说我们可以这么调用foo(x),这个函数就是最常用的,它的工作跟任何东西(类,实例)无关.对于实例方法,我们知道在类里每次定义方法的时候都需要绑定这个实例,就是foo(self, x),为什么要这么做呢?因为实例方法的调用离不开实例,我们需要把实例自己传给方法,调用的时候是这样的a.foo(x)(其实是foo(a, x)).类方法一样,只不过它传递的是类而不是实例,A.classfoo(x).注意这里的self和cls可以替换别的参数,但是python的约定是这俩,还是不要改的好.
# 对于静态方法其实和普通的函数一样,不需要对谁进行绑定,唯一的区别是调用的时候需要使用a.staticfoo(x)或者A.static_foo(x)来调用.

# 实例方法  	类方法	    静态方法
# a.foo(x)     a.classfoo(x)	  a.staticfoo(x)
# A.不可用  	A.classfoo(x)      A.staticfoo(x)
# 更多关于这个问题:

# http://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python
# https://realpython.com/blog/python/instance-class-and-static-methods-demystified/

# 三. 迭代器和生成器
# 这个是stackoverflow里python排名第一的问题,值得一看: http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python

# 这是中文版: http://taizilongxu.gitbooks.io/stackoverflow-about-python/content/1/README.html

# iterables(迭代器)
#   可以用在for...in...语句中的都是可迭代的,比如lists,strings,files...因为这些可迭代的对象你可以随意的读取所以非常方便易用,
#   但是你必须把它们的值放到内存里,当它们有很多值时就会消耗太多的内存

# generator(生成器)
#     生成器也是迭代器的一种,但是你只能迭代它们一次,原因很简单,因为它们不是全部存在内存里,它们只在要调用的时候在内存里生成，生成器和迭代器的区别就是用()代替[],还有你不能用for i in generator第二次调用生成器,首先计算0,然后会在内存里丢掉0去计算1,直到计算完4

# 这里有个关于生成器的创建问题面试官有考： 问： 将列表生成式中[]改成() 之后数据结构是否改变？ 答案：是，从列表变为生成器

# ls = [x*x for x in range(10)]
# print(ls,type(ls))  #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81] <class 'list'>

# gr = (x*x for x in range(10))
# print(gr)  #<generator object <genexpr> at 0x000002A04FC21ED0>

# 通过列表生成式，可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含百万元素的列表，不仅是占用很大的内存空间，如：我们只需要访问前面的几个元素，后面大部分元素所占的空间都是浪费的。因此，没有必要创建完整的列表（节省大量内存空间）。在Python中，我们可以采用生成器：边循环，边计算的机制—>generator

# from collections import Iterable

# str = '12345'
# ls = [1,2,3,4,5]
# tu = (1,2,3,4,5)
# dc = {1:2,3:4}
# st = {1,2,3,4,5}

# # 判断一个对象是否可以迭代,上述都是可迭代的对象
# print(isinstance(str,Iterable))  #True
# print(isinstance(ls,Iterable))  #True
# print(isinstance(tu,Iterable))  #True
# print(isinstance(dc,Iterable))  #True
# print(isinstance(st,Iterable))  #True

# # 可迭代协议
# # dir监测数据对象所拥有的内置函数
# print(dir('12'))
# print(dir([1,2]))
# print(dir((1,2)))
# print(dir({1:2}))
# print(dir({1,2}))

# # __iter__方法存在于这5种数据类型

# print([1,2].__iter__())  #<list_iterator object at 0x0000017CFC908320>

# # iterator(迭代器)
# print(set(dir([1,2].__iter__()))-set(dir([1,2])))  #{'__setstate__', '__length_hint__', '__next__'}

# iter = [1,2,3,4,5].__iter__()  #<list_iterator object at 0x0000017CFC908320>

# # 获取迭代器中元素长度
# print(iter.__length_hint__())

# # 根据索引值指定从哪里开始迭代
# print(iter.__setstate__(0))

# # 一个一个取值
# print(iter.__next__())  #1
# print(iter.__next__())  #2

# 不使用for循环遍历列表

lst = [1,2,3,4,5]

lstiter = lst.__iter__()

while True:
    try:
        item = lstiter.__next__()
        print(item)
    except StopIteration:
        break

# 迭代器遵守迭代器协议,必须拥有__iter__()和__next__()方法

from collections import Iterator

print('__iter__' in dir(range(5)))  #True
print('__next__' in dir(range(5)))  #False

print(isinstance(range(5),Iterator))  #False

# range()是可迭代的,但不是迭代器


# for循环可迭代的对象(iterable) 字符串、列表、元祖、字典、集合
# for i in ls:
#     print(i)

# for j in 12345:
#     print(j)  #TypeError: 'int' object is not iterable

# 迭代器好处节省内存

# 生成器 文本监听
# 本质就是一个迭代器

# 1.生成器函数

def produce():
    # 下面条
    for i in range(200):
        yield f'做了第{i}碗面'

g = produce()
print(g)  #<generator object produce at 0x000002161AD45570>
print(g.__next__())
print(g.__next__())
print(g.__next__())

# 2. 生成器表达式
ls = [f'第{x}个梦' for x in range(10)]
print(ls)  #['第0个梦', '第1个梦', '第2个梦', '第3个梦', '第4个梦', '第5个梦', '第6个梦', '第7个梦', '第8个梦', '第9个梦']

gt = (f'第{x}个梦' for x in range(10))
print(gt)  #<generator object <genexpr> at 0x000001E10E8A65E8>
print(gt.__next__())
print(next(gt))

# 面试题

# 生成器的函数
def demo():
    for i in range(4):
        yield i

g = demo()

# 生成器表达式
g1 = (i for i in g)
print(g1)  #<generator object <genexpr> at 0x000002AC16D16570>

g2 = (i for i in g)  #<generator object <genexpr> at 0x000002AC16D166D8>
print(g2)

print(list(g1))  #[0, 1, 2, 3]
print(list(g2))  #[]