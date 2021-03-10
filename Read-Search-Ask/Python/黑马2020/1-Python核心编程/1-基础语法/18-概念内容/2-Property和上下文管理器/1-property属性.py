# property属性

# 1. property属性介绍
#     定义property属性就是把一个方法当做属性进行使用,这样做可以简化代码使用

#     定义property属性的两种方式
#         1. 装饰器方式
#         2. 类属性方式

# 2. 装饰器的方式

class Student(object):
    def __init__(self):
        # 私有属性
        self.__age == 0

    # 当对象调用age属性的时候就会执行下面的方法
    @property
    def age(self):
        return self.__age

student = student()
age = student.age()
print(age)