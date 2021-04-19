## 一. Python基础

### 1 语法

#### 1.1 输入与输出

##### 1.1.1 代码中修改不可变数据类型会出现什么问题?

```python
a = 'abc'
print(a[0])
a[0] = 'b'
```

> TypeError: str object does not support item assignment

##### 1.1.2 a=1,b=2,不用中间变量交换a,b的值?

方法一:

```python
a = a+b
b = a-b
a = a-b
```

方法二:

```python
a, b = b, a 
```

##### 1.1.3 pirnt调用底层什么方法?

print 方法默认调用 sys.stdout.write 方法,即往控制台打印字符串

##### 1.1.4 简述input()函数理解?

input()获取用户输入,不论用户输入的是什么,获取到的都是字符串类型

#### 1.2 条件与循环

##### 1.2.1 range和xrange的区别?

两者用法相同,不同的是 range 返回的结果是一个列表,而 xrange 的结果是一个生成器,前者是直接开辟一块内存空间来保存列表,后者是边循环边使用,只有使用时才会开辟内存空间,所以当列表很长时,使用 xrange 性能要比range好,Python3中没有xrange函数

#### 1.3 文件操作

##### 1.3.1 4G内存如何读取5G文件?

可以通过生成器,分多次读取,每次读取数量相对少的数据(比如500MB)进行处理,处理结束后在读取后面的500MB的数据

##### 1.3.2 read、readline和readlines的区别?

read:读取整个文件
readline:读取下一行,使用生成器方法
readlines:读取整个文件到一个迭代器以供我们遍历

#### 1.4 异常

##### 1.4.1 在except中return后还会不会执行finally中的代码?怎么抛出自定义异常?

会继续处理 finally 中的代码,用 raise 方法可以抛出自定义异常

##### 1.4.2 介绍一下 except 的作用和用法？

except: 捕获所有异常 
except: <异常名>: 捕获指定异常 
except: <异常名 1, 异常名 2> : 捕获异常1或者异常 2 
except: <异常名>,<数据>:捕获指定异常及其附加的数据 
except: <异常名 1,异常名 2>:<数据>:捕获异常名1或者异常名2,及附加的数据

#### 1.5 模块与包

##### 1.5.1 常用的Python标准库都有哪些?

os 操作系统、time 时间、random 随机、pymysql 连接数据库、threading 线程、multiprocessing 进程、queue 队列

##### 1.5.2 赋值、浅拷贝和深拷贝的区别?

```python
import copy
a = [1, 2, 3, 4, ['a', 'b']]  #原始对象

b = a  #赋值,传对象的引用,赋值引用,a和b都指向同一个对象 # TODO:引用赋值,与传值赋值区分
c = copy.copy(a)  #对象拷贝,浅拷贝  #  浅拷贝,a和c是一个独立的对象,但他们的子对象还是指向统一对象(是引用),只拷贝顶级对象,或者说父级对象
d = copy.deepcopy(a)  #对象拷贝,深拷贝  #  深拷贝,a和b完全拷贝了父对象及其子对象,两者是完全独立的 ,拷贝所以对象,顶级对象及其嵌套对象 # TODO: 传值赋值

a.append(5)  #修改对象a  #a = [1, 2, 3, 4, ['a', 'b'],5]
a[4].append('c')  #修改对象a中的['a', 'b']数组对象  #a = [1, 2, 3, 4, ['a', 'b','c'],5]

print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)

# 输出结果:
a =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
b =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
c =  [1, 2, 3, 4, ['a', 'b', 'c']]
d =  [1, 2, 3, 4, ['a', 'b']]
```

**赋值**
在Python中,对象的赋值就是简单的对象引用

```python
a = b
```

在上述情况下, a 和 b 是一样的,他们指向同一片内存, b 不过是 a 的别名,是引用
我们可以使用 b is a 去判断,返回 True,表明他们地址相同,内容相同,也可以使用 id() 函数来查看两个列表的地址是否相同
赋值操作(包括对象作为参数、返回值)不会开辟新的内存空间,它只是复制了对象的引用,也就是说除了 b 这个名字之外,没有其他的内存开销,修改了 a,也就影响了 b,同理,修改了 b 也就影响了 a

**浅拷贝**
浅拷贝会创建新对象,其内容非原对象本身的引用,而是原对象内第一层对象的引用 
浅拷贝有三种形式:切片操作、工厂函数、copy 模块中的 copy 函数 
比如上述的列表 a 
切片操作:b = a[:] 或者 b = [x for x in a] 
工厂函数:b = list(a) 
copy 函数:b = copy.copy(a) 
浅拷贝产生的列表 b 不再是列表 a 了,使用 is 判断可以发现他们不是同一个对象,使用 id 查看, 他们也不指向同一片内存空间但是当我们使用 id(x) for x in a 和 id(x) for x in b 来查看 a 和 b 中元 素的地址时,可以看到二者包含的元素的地址是相同的
在这种情况下,列表 a 和 b 是不同的对象,修改列表 b 理论上不会影响到列表 a 但是要注意的是,浅拷贝之所以称之为浅拷贝,是它仅仅只拷贝了一层,在列表 a 中有一个嵌套的 list,如果我们修改了它,情况就不一样了
比如：a[4].append('c'),查看列表 c,会发现列表 c 也发生了变化,这是因为,我们修改了嵌套的 list,修改外层元素,会修改它的引用,让它们指向别的位置,修改嵌套列表中的元素,列表的地址并未发生变化,指向的都是用一个位置

**深拷贝**
深拷贝只有一种形式,copy 模块中的 deepcopy() 函数,深拷贝和浅拷贝对应,深拷贝拷贝了对象的所有元素,包括多层嵌套的元素.因此,它的时间和空间开销要高,同样的对列表 a,如果使用 d = copy.deepcopy(a),再修改列表 d 将不会影响到列表 a,即使嵌套的列表具有更深的层次,也不会产生任何影响,因为深拷贝拷贝出来的对象根本就是一个全新的对象, 不再与原来的对象有任何的关联

**拷贝的注意点**
对于非容器类型,如数字、字符,以及其他的原子类型,没有拷贝一说,产生的都是原对象的引用
如果元组变量值包含原子类型对象,即使采用了深拷贝,也只能得到浅拷贝

##### 1.5.3 \__init__和\_\_new\_\_的区别?

init 在对象创建后,对对象进行初始化
new 是在对象创建之前创建一个对象,并将该对象返回给 init

##### 1.5.4 Python中如何生成随机数?

在Python中用于生成随机数的模块是 random,在使用前需要 import

```python
import random

# 生成一个 0-1 之间的随机浮点数
print(random.random())
# 生成[a,b]之间的浮点数
print(random.uniform(1.1, 1.2))
# 生成[a,b]之间的整数
print(random.randint(2, 5))
# 从特定序列中随机取一个元素,这里的序列可以是字符串、列表、元组等
print(random.choice('12345'))

```

##### 1.5.5 输入某年某月某日,判断这一天是这一年的第几天?

在Python中用于日期模块是 datetime,在使用前需要 import

```python
import datetime 

def dayofyear(): 
    year = input('请输入年份:') 
    month = input('请输入月份:') 
    day = input('请输入天:') 
    date1 = datetime.date(year=int(year),month=int(month),day=int(day)) 
    date2 = datetime.date(year=int(year),month=1,day=1) 
                  
    return (date1 - date2 + 1).days
                  
```

##### 1.5.6 打乱一个排好序的list对象ls?

```python
import random

ls = [1,2,3,4,5]
print(random.shuffle(ls))

```

##### 1.5.7 说明一下 os.path 和 sys.path 分别代表什么?

os.path 主要是用于对系统路径文件的操作
sys.path 主要是对 Python 解释器的系统环境参数的操作(动态的改变 Python 解释器搜索路径)

##### 1.5.8 Python 中的 os 模块常见方法?

os.remove() 删除文件 
os.rename() 重命名文件
os.getcwd() 取得当前工作目录
os.path.join() 将分离的各部分组合成一个路径名
os.path.exists() 是否存在
os.path.getsize() 返回文件大小
os.path.isfile()是否为文件

##### 1.5.9 Python 的 sys 模块常用方法?

sys.argv 命令行参数 List,第一个元素是程序本身路径
sys.modules.keys() 返回所有已经导入的模块列表
sys.path 返回模块的搜索路径,初始化时使用 PYTHONPATH 环境变量的值

##### 1.5.10 模块和包是什么?

在 Python 中,模块是搭建程序的一种方式
每一个 Python 代码文件都是一个模块,并可以引用 其他的模块,比如对象和属性,一个包含许多 Python 代码的文件夹是一个包,一个包可以包含模块和子文件夹

#### 1.6 Python特性

##### 1.6.1 Python 是强语言类型还是弱语言类型?

Python 是强类型的动态脚本语言
强类型:不允许不同类型相加 
动态:不使用显示数据类型声明,且确定一个变量的类型是在第一次给它赋值的时候
脚本语言:一般也是解释型语言,运行代码只需要一个解释器,不需要编译

##### 1.6.2 Python 是如何进行类型转换的?

内建函数封装了各种转换函数,可以使用目标类型关键字强制类型转换
进制之间的转换可以用 int('str', base='n')将特定进制的字符串转换为十进制,再用相应的进制转换函数将十进制转换为目标进制

可以使用内置函数直接转换的有
list---->tuple tuple(list)
tuple---->list list(tuple)

##### 1.6.3 Python 中的作用域?

Python 中,一个变量的作用域总是由在代码中被赋值的地方所决定
当 Python 遇到一个变量的话，它会按照这的顺序进行搜索
本地作用域(Local)--->当前作用域被嵌入的本地作用域(Enclosing locals)--->全局/模块作用域 (Global)--->内置作用域(Built-in)

##### 1.6.4 简述解释型和编译型编程语言

解释型语言编写程序不需要编译,在执行的时候,专门有一个解释器能够将 VB 语言翻译成机器语言,每个语句都是执行的时候才翻译这样解释型语言每执行一次就要翻译一次,效率比较低.

用编译型语言写的程序执行之前,需要一个专门的编译过程,通过编译系统,把源高级程序编译成为机器语言文件运行时不需要翻译,所以编译型语言的程序执行效率较高

##### 1.6.5 位和字节的关系?

bit就是位,也叫比特位,是计算机表示数据最小的单位
byte就是字节,1byte=8bit,1byte就是1B,一个字符=2字节,1KB=1024B
字节就是Byte,也是B.位就是bit也是b
转换关系如下:1KB=1024B 1B= 8b

##### 1.6.6 (二|八|十六)进制转换成十进制

先将其转换为字符串,再使用int函数,指定进制转换为二进制 

```python
print(int('0b1111011',2))  #123

print(int('011',8))  #9

print(int('0x12',16))  #18

```

##### 1.6.7 十进制转化为(二|八|十六)进制

```python
print(bin(10))  #0b1010  # Binary

print(oct(20))  #0o24    # Octal

print(hex(30))  #0x1e    # Hexadecimal

```

##### 1.6.8 Ascii,Unicode,UTF-8,GBK区别?

Ascii编码,最早只有127个字母被编码到计算机中,大小写英文字母,数字和一些符号
Unicode把所有的语言统一到一套编码之中,解决不同语言出现乱码问题,常用两个字节表示一个字符
UTF-8编码是可变长编码的Unicode编码(节省空间),UTF-8把一个Unicode编码根据不同的数字大小编码成1-6个字节,英文字母被编码成1个字节,汉字通常是3个字节

##### 1.6.9 机器码和字节码

机器码就是计算机可以直接执行,并且执行速度最快的代码
字节码是一种中间状态(中间码)的二进制代码(文件),需要直译器转译后才能成为机器码

##### 1.6.10 列举布尔值为 False 的常见值?

除了标准值 False 和 None,所以类型的数字 0,空序列(空字符,空元祖,空列表,空字典)都为假

### 2 数据类型

#### 2.1 string

##### 2.1.1 什么是可变、不可变数据类型?

可变不可变指的是内存中的值是否可以被改变
不可变类型指的是对象所在内存块里面的值不可以改变,有数值、字符串、元组
可变类型则是可以改变,主要有列表、字典、集合

##### 2.1.2 如何理解 Python 中字符串中的\字符?

有三种不同的含义
1.转义字符
2.路径名中用来连接路径名
3.编写太长代码手动软换行

##### 2.1.3 写过反转字符串的方法

方法一 切片

```python
str = '12345'

pirnt(str[::-1])

```

方法二 列表reverse方法

```python
str = '12345'

ls = list(str)
ls.reverse()

print(''.join(ls))

```

方法三 列表推导

```python
str = '12345'

nstr = ''.join(str(-x) for x in range(1, len(str)+1))

```



##### 2.1.4 将字符串"k:1|k1:2|k2:3|k3:4"，处理成 Python 字典：{k:1， k1:2， ... } ,字典里的 k 作为字符串处理

##### 2.1.5 请按 ls 中元素的 age 由大到小排序

#### 2.2 tuple

tuple:元组,元组将多样的对象集合到一起,不能修改,通过索引进行查找,使用括号()
应用场景:把一些数据当做一个整体去使用,不能修改

```python
a = '1'
b = '1',


pirnt(type(a))  #string

pirnt(type(b))  #tuple

```

#### 2.3 list

list是 Python 中使用最频繁的数据类型,在其他语言中通常叫做数组,通过索引进行查找,使用方括号[], 列表是有序的集合

##### 2.3.1 列表常用操作

1) 增加

在指定位置插入数据 列表.insert(index, value)

```python
ls = [1, 2, 3, 4, 5]

# 列表下标为0的地方插入数据
ls.insert(0,0)

# 列表下标为6的地方插入数据,列表最大下标为4,自动补位插到最后位置
ls.insert(6,6)

```

在列表末尾追加数据 列表.append(value)

```python
ls = [1, 2, 3, 4, 5]

# 末尾追加
ls.append(6)

```

将可迭代对象追加到列表 列表.extend(iterable)

```python
str = '12345'
ls = []

ls.extend(str)

```

2)删除

删除指定索引数据 del 列表[index]

```python
ls = [1, 2, 3, 4, 5]

del ls[4]

```

删除第一个出现的指定元素 列表.remove(value)

```python
ls = [1, 2, 3, 4, 5]

ls.remove(5)

```

删除末尾数据 列表.pop() 返回值是被删除元素

```python
ls = [1, 2, 3, 4, 5]

ls.pop()

```

删除指定索引元素并返回此元素 列表.pop(index)

```python
ls = [1, 2, 3, 4, 5]

ls.pop(4)

```

清空列表元素 列表.clear()

```python
ls = [1, 2, 3, 4, 5]

ls.clear()

```

3)排序

升序排序 列表.sort(reverse=False)

```python
ls = [5, 4, 3, 2, 1]

ls.sort()

```

逆序反转 列表.reverse()

```python
ls = [5, 4, 3, 2, 1]

ls.reverse()

```

4)统计相关

数据在列表中出现的次数 列表.count(value)

```python
ls = [1, 2, 3, 4, 5]

ls.count(1)

```

##### 2.3.2 ls[10]和ls[10:]

尝试获取列表的切片,开始的 index 超过了成员个数不会产生 IndexError,而是仅仅返回一个空列表

```python
ls = [1, 2, 3, 4, 5]


print(ls[10])  #IndexError: list index out of range

print(ls[10:])  #[]

```

##### 2.3.3 给定两个列表,怎么找出他们相同的元素和不同的元素?

```python
l1 = [1, 2, 3]
l2 = [3, 4, 5]

set1 = set(l1)
set2 = set(l2)

print(set1&set2)
print(set1^set2)

```

##### 2.3.4 列表去重

方法一 set去重

```python
ls = [1, 1, 2, 2, 3, 3, 4, 4]

nls = list(set(ls))
# key主要是用来进行比较的元素,只有一个参数,具体的函数的参数就是取自于可迭代对象中,指定可迭代对象中的一个元素来进行排序.
nls.sort(key=ls.index)

```

方法二 循环去重

```python
ls = [1, 1, 2, 2, 3, 3, 4, 4]

nls = []

for x in ls:
    if x not in nls:
        nls.append(x)
        
```

方法三 dict属性

```python
ls = [1, 1, 2, 2, 3, 3, 4, 4]

newdic = {}.fromkeys(ls)

nls = list(newdic)

```

#### 2.4 dict

##### 2.4.1 现有字典dic = {'a':5, 'b':4, 'c':3}请按字典中的 value 值进行排序?

```python
dic = {'a':5, 'b':4, 'c':3}

sorted(dic.items(),key = lambda x:x[1])
```

##### 2.4.2 字典和json的区别?

字典是一种数据结构,json 是一种数据的表现形式,字典的 key 值只要是能 hash 的就行,json 的必须是字符串

##### 2.4.3 字典推导式

```python
dic = {key: value for (key, value) in iterable}
```

##### 2.4.4 输出一个字符串中每个字符的个数

方法一 dict.get方法

```python
str = 'life is short I use python'

dic = dict()

for x in str:
    dic[x] = dic.get(x,0) + 1
    
print(dic)

# dict.get(Key,default=None),返回指定键的值,如果键不在字典中返回默认值为None或者设置的默认值

```

方法二 dict属性

```python
str = 'life is short I use python'

dic = dict()

for x in str:
    if x not in dic.keys():
        dic[x] = 1
    else:
        dic[x] += 1
        
print(dic)

```

#### 2.5 set

set 集合,在 Python 中的书写方式的{},集合与之前列表、元组类似,可以存储多个数据,但是这些数据是不重复的
集合对象还支持 union(联合), intersection(交), difference(差)和sysmmetric_difference(对称差集)等数学运算

##### 2.5.1 集合常用操作

1)列表去重

```python
ls = [1, 1, 2, 2, 3, 3, 4, 4]

set(ls)

```

2)交集(共有部分)

```python
a = {1, 2, 3, 4, 5}
b = {1, 3, 5, 7, 9}

print(a & b)

```

3)并集(总共部分)

```python
a = {1, 2, 3, 4, 5}
b = {1, 3, 5, 7, 9}

print(a|b)

```

4)差集(另一个集合中没有部分)

```python
a = {1, 2, 3, 4, 5}
b = {1, 3, 5, 7, 9}

print(a - b)
```

5)对称差集(在二者中,但不会同时出现在二者中)

```python
a = {1, 2, 3, 4, 5}
b = {1, 3, 5, 7, 9}

print(a ^ b)
```

## 二. Python高级

### 1 元类

#### 1.1 Python 中类方法、类实例方法、静态方法有何区别?

**类方法**
是类对象的方法,在定义时需要在上方使用'@classmethod'进行装饰,形参为 cls,表示类对象,类对象和实例对象都可调用 

**类实例方法**
是类实例化对象的方法,只有实例对象可以调用,形参为 self,指代对象本身

**静态方法**
是一个任意函数,在其上方使用'@staticmethod'进行装饰,可以用对象直接调用,静态方法实际上跟该类没有太大关系

### 2 内存管理和垃圾回收机制

#### 2.1 Python的内存管理机制及调优手段?

**内存管理机制:引用计数、垃圾回收、内存池**

**引用计数**

引用计数是一种非常高效的内存管理手段
当一个 Python 对象被引用时其引用计数增加 1,当其不再被一个变量引用时则计数减 1,当引用计数等于 0 时对象被删除

**垃圾回收**

+ 引用计数
  引用计数也是一种垃圾收集机制,而且也是一种最直观,最简单的垃圾收集技术
  当 Python 的某 个对象的引用计数降为 0 时,说明没有任何引用指向该对象,该对象就成为要被回收的垃圾了
  比如某个新建对象,它被分配给某个引用,对象的引用计数变为 1
  如果引用被删除,对象的引用计数为 0,那么该对象就可以被垃圾回收
  不过如果出现循环引用的话,引用计数机制就不再起有效的作用了
+ 标记清除
  如果两个对象的引用计数都为 1,但是仅仅存在他们之间的循环引用,那么这两个对象都是需要被回收的,也就是说,它们的引用计数虽然表现为非 0,但实际上有效的引用计数为 0,所以先将循环引用摘掉,就会得出这两个对象的有效计数
+ 分代回收
  从前面“标记-清除”这样的垃圾收集机制来看,这种垃圾收集机制所带来的额外操作实际上与系统中总的内存块的数量是相关的,当需要回收的内存块越多时,垃圾检测带来的额外操作就越多,而垃圾回收带来的额外操作就越少,反之,当需回收的内存块越少时,垃圾检测就将比垃圾回收带来更少的额外操作
  举个例子,当某些内存块 M 经过了 3 次垃圾收集的清洗之后还存活时,我们就将内存块 M 划到一个集合 A 中去,而新分配的内存都划分到集合 B 中去,当垃圾收集开始工作时,大多数情况都只对集合 B 进 行垃圾回收,而对集合 A 进行垃圾回收要隔相当长一段时间后才进行,这就使得垃圾收集机制需要处理的内存少了,效率自然就提高了,在这个过程中,集合 B 中的某些内存块由于存活时间长而会被转移到集合 A 中,当然集合 A 中实际上也存在一些垃圾,这些垃圾的回收会因为这种分代的机制而被延迟

#### 2.2 内存泄露是什么,如何避免?

内存泄露指由于疏忽或错误造成程序未能释放已经不再使用的内存的情况
内存泄漏并非指内存在物理上的 消失,而是应用程序分配某段内存后,由于设计错误,失去了对该段内存的控制,因而造成了内存的浪 费,导致程序运行速度减慢甚至系统崩溃等严重后果
有 __del__() 函数的对象间的循环引用是导致内存泄漏的主凶,不使用一个对象时使用:del object 来删除一个对象的引用计数就可以有效防止内存泄漏问题,通过 Python 扩展模块 gc 来查看不能回收的对象的详细信息,可以通过 sys.getrefcount(obj) 来获取对象的引用计数,并根据返回值是否为 0 来判断是否内存泄漏

### 3 函数

#### 3.1 函数参数

##### 3.1.1 Python 函数调用的时候参数的传递方式是值传递还是引用传递?

**Python 的参数传递有:位置参数、默认参数、可变参数、关键字参数**

函数的传值到底是值传递还是引用传递，要分情况

不可变参数用值传递
像整数和字符串这样的不可变对象,是通过拷贝进行传递的,因为你无论如何都不可能在原处改变不可变对象

可变参数引用传递
比如像列表,字典这样的对象是通过引用传递、和 C 语言里面的用指针传递数组很相似,可变对象能在函数内部改变

##### 3.1.2 对缺省参数的理解

缺省参数指在调用函数的时候没有传入参数的情况下,调用默认的参数,在调用函数的同时赋值时,所传入的参数会替代默认参数 *args 是不定长参数,他可以表示输入参数是不确定的,可以是任意多个
**kwargs 是关键字参数,赋值的时候是以键 = 值的方式,参数是可以任意多对在定义函数的时候不确定会有多少参数会传入时,就可以使用两个参数

##### 3.1.3 为什么函数名字可以当做参数用?

Python 中一切皆对象,函数名是函数在内存中的空间,也是一个对象

##### 3.1.4 Python 中 pass 语句的作用是什么?

在编写代码时只写框架思路,具体实现还未编写就可以用 pass 进行占位,使程序不报错,不会进行任何操作

#### 3.2 内建函数

##### 3.2.1 filter、map函数和reduce函数?

1)从参数来讲
map()包含两个参数,第一个参数是一个函数,第二个是序列(列表或元组),其中,函数(即 map 的第一个参数位置的函数)可以接收一个或多个参数
reduce()第一个参数是函数,第二个是序列(列表或元组),但是,其函数必须接收两个参数

2)从对传进来的数值作用来讲
map()是将传入的函数依次作用到序列的每个元素,每个元素都是独自被函数作用一次
reduce()是将传入的函数作用在序列的第一个元素得到结果后,把这个结果继续与下一个元素作用(累积计算)

```python
# 筛选列表中大于5的元素
ls = [1, 2, 3, 4, 5]

nls = filter(lambda x:x>3, ls)

print(list(nls))

```

```python
# 列表元素平方
ls = [1, 2, 3, 4, 5]

nls = map(lambda x:x**2, ls)

print(list(nls))

```

```python
# 求3阶乘
from functools import reduce

fact = reduce(lambda x,y:x*y,range(1,4))

print(fact)

```

##### 3.2.2 什么是 lambda 函数,有什么好处?

lambda 函数是一个可以接受任意多个参数(包括可选参数)并且返回单个表达式值函数,这种函数得名于省略了用 def 声明函数标准步骤 

1. lambda 函数比较轻便,即用即仍,适合需要完成一项功能,但此功能只在一处使用,连名字都很随意情况下
2. 匿名函数,一般用来给filter、map这样的函数式编程服务
3. 作为回调函数,传递给某些应用,比如消息处理

### 三. 设计模式

#### 3.1 单例模式

单例模式是一种常用的软件设计模式,在它的核心结构中只包含一个被称为单例类的特殊类
通过单例模式可以保证系统中一个类只有一个实例而且该实例易于外界访问,从而方便对实例个数的控制并节约系统资源
如果希望在系统中某个类的对象只能存在一个,单例模式是最好的解决方案

##### 3.1.1 手写单例

在 python 中,可以使用多种方法实现单例模式

**1.使用模块**
Python的模块是天然单例模式,因为模块在第一次导入时,会生成 .pyc 文件,当第二次导入时,直接加载 .pyc 文件,不会再次执行模块代码

```python
# mysingle.py 
class MySingle: 
    def foo(self): 
        pass 

sinleton = MySingle() 

# 将上面的代码保存在文件 mysingle.py 中,然后

from mysingle import sinleton 

singleton.foo()

```

**2.使用\_\_new__()**

为了使类只能出现一个实例,我们可以使用\_\_new__来控制实例的创建

```python
class Singleton(object):
    def __new__(cls):
    	# 每一次实例化的时候,我们都只会返回这同一个 instance 对象
        if not hasattr(cls, 'instance'):
            cls.instance=super(Singleton, cls).__new__(cls)
        return cls.instance


obj1=Singleton()
obj2=Singleton()

obj1.attr='value'

print(obj1 is obj2)  #True
print(obj1.attr, obj2.attr) #value value

```

3.使用装饰器

4.使用metaclass(元类)



##### 3.1.2 单例模式应用场景

#### 3.2 装饰器

##### 3.2.1 什么是装饰器,手写一个计时器记录方法执行性能装饰器?

##### 3.2.2 什么是闭包?

在函数嵌套的前提下,内部函数使用了外部函数的变量,并且外部函数返回了内部函数,我们把这个使用外部函数变量的内部函数称为闭包

**闭包构成条件**
	函数嵌套(函数里面再定义函数)的前提下
	内部函数使用了外部函数的变量(还包括外部函数的参数)
	外部函数返回了内部函数,这个使用了外部函数变量的内部函数称之为闭包

##### 3.2.3 装饰器有什么作用?

#### 3.3 迭代器、生成器

##### 3.3.1 迭代器、生成器区别？

**迭代器** 

**一个对象拥有\__iter__() 和 \_\_next\_\_() 方法,则这个对象就是迭代器(迭代器协议)**

可以用在 for...in... 语句中的都是可迭代的,比如 list, strings, files...因为这些可迭代的对象你可以随意的读取所以非常方便易用,
但是你必须把它们的值放到内存里,当它们有很多值时就会消耗太多的内存

```python
from collections import Iterable


ls = [1,2,3,4,5]
tu = (1,2,3,4,5)
dc = {1:2,3:4}
st = {1,2,3,4,5}

str = '12345'

# 判断一个对象是否可以迭代,上述都是可迭代的对象
print(isinstance(ls,Iterable))  #True
print(isinstance(tu,Iterable))  #True
print(isinstance(dc,Iterable))  #True
print(isinstance(st,Iterable))  #True

print(isinstance(str,Iterable))  #True

```

**生成器(generator)**

生成器也是迭代器的一种,但是你只能迭代它们一次,因为它们不是全部存在内存里,它们只在要调用的时候在内存里生成,
生成器和迭代器的区别就是用()代替[],还有你不能用 for i in generator 第二次调用生成器,生成器会首先计算0,然后会在内存里丢掉0去计算1,直到计算完全

##### 3.3.2 将列表中的 [] 改成 () 之后数据结构是否发生改变?

数据结构从列表变为生成器

```python
ls = [x*x for x in range(10)]

print(ls,type(ls))  #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81] <class 'list'>

en = (x*x for x in range(10))

print(en)  #<generator object <genexpr> at 0x000002A04FC21ED0>

```

通过列表生成式,可以直接创建一个列表,且创建一个包含百万元素的列表,不仅是占用很大的内存空间,
如:我们只需要访问前面的几个元素,后面大部分元素所占的空间都是浪费的
因此,没有必要创建完整的列表(节省大量内存空间)

在Python中,我们可以采用生成器:**边循环,边计算**的机制来应对这种需求

#### 3.3 方法重载与方法重写?

##### 3.3.1 方法重载

是在一个类里面,方法名字相同,而参数不同,返回类型可以相同也可以不同
重载是让类以统一的方式处理不同类型数据的一种手段

##### 3.3.2 方法重写

子类不想原封不动地继承父类的方法,而是想作一定的修改,这就需要采用方法的重写,方法重写又称方法覆盖

### 四. 面向对象

#### 4.1 对象

##### 4.1.1 Python中的可变对象和不可变对象?

不可变对象,该对象所指向的内存中的值不能被改变
当改变某个变量时候,由于其所指的值不能被改变,相当于把原来的值复制一份后再改变,这会开辟一个新的地址,变量再指向这个新的地址
可变对象,该对象所指向的内存中的值可以被改变
变量(准确的说是引用)改变后,实际上是其所指的值直接发生改变,并没有发生复制行为,也没有开辟新的出地址,通俗点说就是原地改变

**Python 中,数值类型(int 和 float)、字符串 str、元组 tuple 都是不可变类型,而列表 list、字典 dict、集合 set 是可变类型**

##### 4.1.2 Python中 is 和 == 的区别?

is 判断的是 a 对象是否就是 b 对象,是通过 id 来判断的 
== 判断的是 a 对象的值是否和 b 对象的值相等,是通过 value 来判断的

##### 4.1.3 对面向对象的理解?

面向对象是相对于面向过程而言的,面向过程语言是一种基于功能分析的、以算法为中心的程序设计方法
而面向对象是一种基于结构分析的、以数据为中心的程序设计思想

**面向对象有三大特性:封装、继承、多态**

##### 4.1.4 OOP 编程三大特征是什么?

**封装**
就是将一个类的使用和实现分开,只保留部分接口和方法与外部联系

**继承**
子类自动继承其父级类中的属性和方法,并可以添加新的属性和方法或者对部分属性和方法进行重写,增加代码可重用性

**多态**
多个子类中虽然都有同一个方法,但是这些子类实例化的对象调用这些相同方法后却可以获得不同的结果,多态增加了增加了应用灵活性(多态概念依赖继承)

### 五. 正则表达式

#### 5.1 正则语法

##### 5.1.1 Python 中 match 和 serach 的区别?

##### 5.1.2 Python 中字符串查找和替换?

### 六. 系统编程

#### 6.1 谈谈多进程、多线程以及协程理解?

#### 6.2 Python 虚拟环境使用?

##### 6.2.1 什么是 Python 虚拟环境

一种采用协作式隔离的运行时环境,允许 Python 用户和应用程序在安装和升级 Python 分发包时不会干扰到同一系统上运行的其他 Python 应用程序的行为

##### 6.2.2 venv 基本使用和原理

查看 venv 命令参数

> python -m venv -h

![image-20210401215357140](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210401215357140.png)

创建虚拟环境

> python -m venv venvdemo

![image-20210401215831406](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210401215831406.png)

虚拟环境原理

> 修改环境变量,把虚拟环境的Python路径加入环境变量最前,环境变量使用原则近者优先.

![image-20210401220456638](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210401220456638.png)

##### 6.2.3 保存和复制虚拟环境

虚拟环境依赖导出

> pip freeze > requirement.txt

![image-20210401220936652](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210401220936652.png)

### 七. 网络编程

#### 7.1 UDP 总结

#### 7.2 TCP 总结

#### 7.3 简述 TCP 和 UDP 区别以及优缺点?

#### 7.4 简述浏览器通过 wsgi 请求动态资源过程?

#### 7.5 简述浏览器访问 www.baidu.com 的过程?

#### 7.7 GET 和 POST 请求区别有哪一些?

GET 请求,请求的数据会附加在 URL 之后,以?分割 URL 和传输数据,多个参数用&连接
URL 的 编码格式采用的是 ASCII 编码,而不是 unicode,即是说所有的非 ASCII 字符都要编码之后再传输

POST 请求,POST 请求会把请求的数据放置在 HTTP 请求包的包体中,因此,GET 请求的数据会暴露在地址栏中,而POST请求则不会

传输数据大小,在开发中,浏览器或服务器对 URL 有长度限制,因此,使用 GET 请求时,传输的数据会受到 URL 长度限制
对于 POST,由于不是 URL 传值,理论上传输数据大小不受限制,实际上各个服务器会规定对 POST 提交数据大小进行限定

安全性,POST 的安全性比 GET 高

效率,GET 比 POST 效率高

+ GET 请求过程
  1.浏览器请求 TCP 连接(第一次握手)
  2.服务器答应进行 TCP 连接(第二次握手)
  3.浏览器确认,并发送 GET 请求头和数据(第三次握手,这个报文比较小,所以 HTTP 会在此时进行第一次数据发送)
  4.服务器返回 200 OK 响应
+ POST 请求过程
  1.浏览器请求 TCP 连接(第一次握手)
  2.服务器答应进行 TCP 连接(第二次握手)
  3.浏览器确认,并发送 POST 请求头(第三次握手,这个报文比较小,所以 HTTP 会在此时进行第一次数据发送)
  4.服务器返回 100 continue 响应
  5.浏览器开始发送数据
  6.服务器返回 200 OK 响应

#### 7.8 cookie 和 session

##### 7.8.1 cookie 和 session 的区别?

1.cookie 数据存放在客户的浏览器上,session 数据放在服务器上
2.cookie 不是很安全,别人可以分析存放在本地的 cookie 并进行 cookie 欺骗考虑到安全应当使 用 session
3.session 会在一定时间内保存在服务器上,当访问增多,会比较占用服务器的性能考虑到减轻服务器性能方面,应当使用 cookie 
4.单个 cookie 保存的数据不能超过 4K,很多浏览器都限制一个站点最多保存 20 个 cookie
5.建议将登陆信息等重要信息存放为 session,其他信息如果需要保留,可以放在 cookie 中

##### 7.8.2 cookie 和 session 的联系?

session 对 cookie 的依赖

cookie 采用客户端存储,session 采用的服务端存储的机制,session 是针对每个用户(浏览器端)的,session 值保存在服务器上,通过 sessionId 来区分哪个用户的 session,因此 sessionId 需要被绑定在浏览器端,sessionId 通常会默认通过 cookie 在浏览 器端绑定,当浏览器端禁用 cookie 时,可通过 URL 重写或者表单隐藏字段的方式将 sessionId 传回给服务器，以便服务通过 sessionId 获取客户端对应的 session

具体一次请求流程

当程序需要为客户端创建一个 session 的时候,服务器首先检测这个客户端请求里面是否已经包含了 session 的表示(sessionId),如果已经包含,则说明已经为客户端创建过一个 session,服务端根据 sessionId 检索出来 sesion 并使用,如果客户端请求不包含 sessionId,则为客户端创建一个 session,并生成一个 sessionId 返回给客户端保存

#### 7.9 简单描述 TCP 三次握手和四次挥手?

![image-20210419161819090](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210419161819090.png)

**三次握手**

1.客户端向服务端发送请求建立连接报文, SYN=1, seq=x,等待服务器确认
2.服务器收到客户端发送的请求建立连接报文响应 ack=x+1,并向客户端发送请求建立连接报文 SYN=1,seq=y
3.客户端收到服务器发送的确认建立连接请求 ACK 和请求建立连接 SYN=1 包,向服务器发送确认包(ack=y+1),发送完成客户端和服务端 TCP 连接成功,完成三次握手

**四次挥手**

#### 7.10 说说 HTTP 和 HTTPS 区别?

#### 7.11 HTTP协议状态码作用及常见状态码?

通过状态码告诉客户端服务器的执行状态,以判断下一步执行操作

常见状态机器码
100-199	表示服务器成功接收部分请求,要求客户端继续提交其余请求才能完成整个处理流程
200-299	表示服务器成功接收请求并已完成处理过程,常用 200(OK 请求完成)
300-399	表示为完成请求,客户需要进一步细化请求,常用 302(搜索请求页面已经临时转移到新的URL)
400-499	表示客户端请求有错误,常用 404(服务器无法找到请求页面)、403(服务器拒绝访问,权限不够)
500-599	表示服务端出现错误,常用 500(请求未完成,服务器遇到不可预知情况)

### 八. web开发

#### 8.1 django

##### 8.1.1 django 创建项目的命令?

> django-admin startproject 项目名称
> python manage.py startapp 应用名称

##### 8.1.2 django 创建项目后项目文件夹下的组成部分?

![image-20210416144220927](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210416144220927.png)

**项目文件夹的组成部分**

manage.py 是项目运行入口,指定配置文件路径
与项目同名的文件夹
\__init.py__ 是一个空文件,作用是这个目录可以被当做包使用
setting.py是项目整体配置文件
urls.py 是项目的 URL 配置文件
wsgi.py 是项目与 WSGI 兼容的web服务器

### 九. 数据库

##### 9.1 Python 中操作 Mysql 步骤?

![image-20210419183934396](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210419183934396.png)

```python
import pymysql

# conn = pymysql.connect(host='127.0.0.1',port=3333,user='root',password='1234',database='sample')

# 操作cursor方法获取游标,得到一个可以执行的sql语句,并且将操作结果作为字典返回
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# try:
#     # 使用execute方法执行sql查询
#     cursor.execute('select * from `case`')
#     # 使用fetchall查询所有 fetchone查询单条
#     date = cursor.fetchall()
#     # date = cursor.fetchone()

#     print(date)

# except Exception as e:
#     print(e)

# finally:
#     conn.close()

from warnings import filterwarnings

# 忽略mysql告警信息
filterwarnings('ignore',category=pymysql.Warning)

class mysqlDB:

    def __init__(self):
        # 建立数据库连接
        self.conn = pymysql.connect(host='127.0.0.1',port=3333,user='root',password='1234',database='xdcls')
        # 使用cursor方法获取操作游标,得到一个可以执行的sql语句,并且操作结果作为字典返回的游标
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        # 关闭游标
        self.cur.close()
        # 关闭连接
        self.conn.close()

    def query(self,sql,state='all'):
        self.cur.execute(sql)
        if state == 'all':
            data = self.cur.fetchall()
        else:
            data = self.cur.fetchone()
        return data

    def execute(self,sql):
        # 更新删除新增
        try:
            # 使用execute操作数据库
            rows = self.cur.execute(sql)
            # 提交事务
            self.conn.commit()
            return rows
        except Exception as e:
            print('数据库异常{0}'.format(e))
            self.conn.rollback()

if __name__ == "__main__":
    mydb = mysqlDB()
    # 查询
    rlt = mydb.query('select * from `case`')
    # 添加 必须使用双眼号,单眼号出错
    # rlt = mydb.execute("insert into `case`(app) values('xls')")
    print(rlt)
    
```

##### 9.2 SQL 的 selete 语句完整执行顺序?

```sql
SELECT *
FROM 表
WHERE 条件
GROUP BY 分组条件
HAVING 分组后的筛选条件
ORDER BY 排序字段
LIMIT 分页;
```

**执行顺序**

1)FROM 子句组装来自不同数据源的数据
2)WHERE 子句基于指定的条件对记录进行筛选
3)GROUP BY 子句将数据划分为多个分组
4)使用聚集函数进行计算
5)HAVING 子句筛选分组
6)计算所有的表达式
7)SELECT 子句查询字段
8)ORDER BY 子句对结果集进行排序

##### 9.3 Mysql数据库存储原理?

##### 9.4 事物的特性?

##### 9.5 数据库索引?

##### 9.6 数据库怎么优化查询效率?

##### 9.7 NoSQL 和关系数据库的区别?

### 十. 数据结构算法

#### 10.1 Python实现经典算法

##### 10.1.1 线性查找

线性查找适合无序序列查找元素

```python

# 算法步骤
#   线性查找指按一定的顺序检查数组中每一个元素,直到找到所要寻找的特定值为止

def lineSearch(sequ, item):
    for i in range(len(sequ)):
        if sequ[i] == item:
            return f'元素在{i}号位'
    else:
        return '元素不在序列中'


print(lineSearch([1, 2, 3, 4, 5], 4))

```

##### 10.1.2 二分查找

```python
# 算法步骤
#     我们手里有一个长度为n的正序数列,当我们想查找一个数x是否在这个数列当中的时候
#     1)取数列正中间的数mid
#         如果mid和x相等,则找到结果,查找成功返回True
#         如果mid比x大,则x应该在mid的左侧,我们把mid左侧当作一个新的数列li
#         如果mid比x小,则x应该在mid的右侧,我们把mid右侧当作一个新的数列li
#     2)对于新的数列li,进行1的查找工作
#     3)一直重复上面查找,生成新的数列li为空的时候则数列当中没有数x返回False

# 代码实现

# 1)递归方法,每次传入一个新的序列无法确认元素索引位置

def mergeSearch(sequ, item):
    # 传来序列每次都是新生成的,如果里面么有发现元素,则是查到尽头也没有找到
    if not sequ:
        return '不在序列之中'

    # 使用//向下取整取序列中间索引
    midinx = len(sequ)//2
    # 如果midinx比item大,则说明元素可能出现在midinx左边,对左边再进行二分查找
    if sequ[midinx] > item:
        return mergeSearch(sequ[0:midinx-1], item)
    # 如果midinx比item大,则说明元素可能出现在midinx右边,对右边再进行二分查找
    elif sequ[midinx] < item:
        return mergeSearch(sequ[midinx+1:-1], item)
    # 中间元素是要找的元素,返回真
    else:
        return True


print(mergeSearch([1, 2, 3, 4, 5], 4))

# 2)非递归方法,对一个序列进行循环查找,可以方便确认元素索引位置

def binarySearch(sequ, item):
    # 最小索引位置的默认值
    mininx = 0
    # 最大索引位置的默认值
    maxinx = len(sequ)-1
    # 循环条件序列中有元素
    while mininx < maxinx:
        # 使用//向下取整取序列中间索引
        midinx = (mininx+maxinx)//2
        # 如果midinx比item大,则说明元素可能出现在midinx左边,maxinx值为midinx-1
        if sequ[midinx] > item:
            maxinx = midinx - 1
        # 如果midinx比item小,则说明元素可能出现在midinx右边,mininx值为midinx+1
        elif sequ[midinx] < item:
            mininx = midinx + 1
        else:
            return f'元素在{midinx}号位'

    return '不在序列之中'


print(binarySearch([1, 2, 3, 4, 5], 4))

```

##### 10.1.3 冒泡排序

```python
# 算法步骤
#     1)比较相邻的元素,如果第一个比第二个大,就交换他们两个
#     2)对每一对相邻元素作同样的工作,从开始第一对到结尾的最后一对这步做完后,最后的元素会是最大的数
#     3)针对所有的元素重复以上的步骤,除了最后一个
#     4)持续每次对越来越少的元素重复上面的步骤,直到没有任何一对数字需要比较

# 时间复杂度O(n2)
# 空间复杂度O(1)
# 稳定

# 代码实现

ls = [5, 4, 3, 2, 1]

def bubbleSort(sequ):
    # 每次冒泡确定一个最大值,n个数需要n-1次冒泡
    for i in range(len(sequ)-1):
        # 标志位初始值为False
        flag = False
        # 初始序列中有n个数,两两比较次数为n-1次,每次冒泡确认一个最大值,剩下前n-1个数比较
        for j in range(len(sequ)-1-i):
            # 判断前面的数是否大于后面
            if sequ[j] > sequ[j+1]:
                # 在单次冒泡排序中,如果需要任意两个数交换位置,标志位变文True
                flag = True
                # 大于则交换位置
                sequ[j], sequ[j+1] = sequ[j+1], sequ[j]
        # 在单词冒泡排序中,如果没有任意连个数交互位置,则说明不需要在进行下一轮冒泡排序,直接退出循环
        if flag == False:
            break

    return sequ


print(bubbleSort(ls))

# TODO:
#     sequ[j],sequ[j+1] = sequ[j+1],sequ[j]
#     等价于
#     temp = sequ[j]
#     sequ[j] = sequ[j+1]
#     sequ[j+1] = temp

```

##### 10.1.4 选择排序

```python
# 算法步骤
#     1)首先在未排序序列中找到最小(大)元素,存放到排序序列的起始位置
#     2)再从剩余未排序元素中继续寻找最小(大)元素,然后放到已排序序列的末尾
#     3)重复第二步,直到所有元素均排序完毕

# 时间复杂度O(n2)
# 空间复杂度O(log2N)-O(n)
# 不稳定

# 代码实现

ls = [5, 4, 3, 2, 1]

def selectSort(sequ):
    # 每次选择一个最小的数排到序列前面,n个数需要n-1次选择排序
    for i in range(len(sequ)-1):
        # 记录初始位,定义为最小数索引
        mininx = i
        # 一次选择排序,从第二个数开始与定义最小索引比较
        for j in range(i+1, len(sequ)):
            # 如果最小索引的值比索引j的值大则交换位置
            if sequ[mininx] > sequ[j]:
                mininx = j
        # i不是最小数是,将i和最小数进行交换
        if mininx != i:
            sequ[i], sequ[mininx] = sequ[mininx], sequ[i]

    return sequ


print(selectSort(ls))

```

##### 10.1.5 插入排序

```python
# 算法步骤
#     1)从第一个元素开始,该元素可以认为已经被排序
#     2)取出下一个元素,在已经排序的元素序列中从后向前扫描
#     3)如果该元素(已排序)大于新元素,将该元素移到下一位置
#     4)重复步骤3,直到找到已排序的元素小于或者等于新元素的位置
#     5)将新元素插入到该位置后
#     6)重复步骤2-5

# 时间复杂度O(n2)
# 空间复杂度O(1)
# 稳定

# 代码实现

ls = [5, 4, 3, 2, 1]

def insertSort(sequ):
    # 第一个元素可以被认为已经被排序,遍历第一个元素之后的序列
    for i in range(1, len(sequ)):
        # 两数比较需要到sequ[0],即是sequ[i-1],i-1>0,i>=1
        while i > 0:
            # 取出未排序列的第一个元素,在已排元素序列中从后向前扫描
            if sequ[i] < sequ[i-1]:
                # 后面元素小于前面元素(第一次while循环前面元素即为有序序列的最后一位)则交换位置
                sequ[i], sequ[i-1] = sequ[i-1], sequ[i]
                i -= 1
            else:
                # 后面元素大于等于前面元素直接跳出本次循环
                break

    return sequ


print(insertSort(ls))

```

##### 10.1.6 快速排序

```python
# 算法步骤
#     1)随机选取序列中一个值,挨个跟后面的数值作比较
#     2)比该数值小的将放在左序列中,反之则放在右序列
#     3)返回左序列+[随机值]+右序列,左右序列使用递归的方式继续进行排序

# 时间复杂度O(nlog2N)
# 空间复杂度O(nlog2N)
# 不稳定

def quickSort(sequ):
    # 序列元素不超过1个则返回该序列
    if len(sequ) < 2:
        return sequ
    # 随机取数
    temp = sequ[0]
    # 比随机取数小的放在左序列
    leftSequ = [x for x in sequ if x < temp]
    # 比随机取数大的放在右序列
    rigtSequ = [x for x in sequ if x > temp]

    # 左右序列递归方式继续排序
    return quickSort(leftSequ) + [temp] + quickSort(rigtSequ)


print(quickSort([5, 4, 3, 2, 1]))

```

#### 10.2 leetcode 刷题