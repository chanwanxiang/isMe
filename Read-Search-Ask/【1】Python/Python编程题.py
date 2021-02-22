## 编写一个程序，它将找到所有这些数字，可被7整除，但不是5的倍数，2000年至3200(包括在内)。得到的数字应按逗号分隔的顺序打印在一行上。

# ls = [str(x) for x in range(2000,3201) if x%5 != 0 and x%7 == 0]
# print(','.join(ls))

## 编写一个可以计算给定数的阶乘的程序。结果应该以逗号分隔的顺序打印在一行上。假设向程序提供以下输入:8,则输出为:40320

# def fact(x):
#     if x == 1:
#         return 1
#     return x*fact(x-1)

# print(fact(8))

## 使用给定的整数n，编写一个程序生成一个包含(i, i*i)的字典，该字典包含1到n之间的整数(两者都包含)。然后程序应该打印字典。假设向程序提供以下输入:8则输出为:{1:1，2:4，3:9，4:16，5:25，6:36，,7:49，8:64}

# def dct(x):
#     dt = {}
#     for x in range(1,x+1):
#         dt[x] = x*x
#     return dt

# print(dct(8))

## 问题:编写一个程序，该程序接受控制台以逗号分隔的数字序列，并生成包含每个数字的列表和元组。假设向程序提供以下输入:34岁,67年,55岁,33岁,12日,98年则输出为:['34'， '67'， '55'， '33'， '12'， '98']('34'， '67'， '55'， '33'， '12'， '98')

# import re

# str = input('请输入序列值->')
# ls = re.findall('[0-9]+',str)
# print(ls)
# print(tuple(ls))

## 问题:定义一个至少有两个方法的类: getString:从控制台输入获取字符串 printString:打印大写母的字符串。还请包含简单的测试函数来测试类方法。提示:使用_init__方法构造一些参数

# class InputString():
#     def __init__(self):
#         self.str = str

#     def getString(self):
#         self.str = input('请输入字符串->')

#     def printString(self):
#         print(self.str.upper())

# if __name__ == '__main__':
#     iS = InputString()
#     iS.getString()
#     iS.printString()

## 编写一个程序，根据给定的公式计算并打印值:Q=sqrt{[(2*C*D)/H]}。以下是C和H的固定值:C是50。H是30。D是一个变量，它的值应该以逗号分隔的序列输入到程序中。
## 例子假设程序的输入序列是逗号分隔的:100，150，180
## 程序输出为:18，22，24
## 提示:如果接收到的输出是小数，则应四舍五入到其最近的值(例如，如果接收到的输出是26.0，则应打印为26)。在为问题提供输入数据的情况下，应该假设它是控制台输入。

# import math

# seq = map(int,input('请输入序列值->').split(','))

# print(seq)

# for x in seq:
#     print(x)
#     print(round(math.sqrt((2*50*x)/30)))

## 编写一个程序，以2位数字，X,Y作为输入，生成一个二维数组。数组的第i行和第j列中的元素值应该是i*j。
## 注意:i= 0,1 . .,X - 1;    j = 0, 1,­Y-1。
## 例子假设程序有以下输入:3、5
## 则程序输出为:[[0,0,0,0,0],[0,1,2,3,4],[0,2,4,6,8]]
## 提示:注意:如果要为问题提供输入数据，应该假设它是一个控制台输入，以逗号分隔。

# x,y = map(int,input('请输入两位数字->').split(','))

# for i in range(x):
#     ls = []
#     for j in range(y):
#         ls.append(i*j)
#     print(ls)

## 编写一个程序，接受逗号分隔的单词序列作为输入，按字母顺序排序后按逗号分隔的序列打印单词。假设向程序提供以下输入:
## without,hello,bag,world
## 则输出为:
## bag,hello,without,world
## 提示:在为问题提供输入数据的情况下，应该假设它是控制台输入。

# seq = input('请输入字符串->').split(',')
# seq.sort()
# print(','.join(seq))

## 问题:编写一个程序，接受一行序列作为输入，并在将句子中的所有字符大写后打印行。
## 假设向程序提供以下输入:
## Hello world
## Practice makes perfect
## 则输出为:
## HELLO WORLD
## PRACTICE MAKES PERFECT
## 提示:在为问题提供输入数据的情况下，应该假设它是控制台输入。

# seqs = []

# while True:
#     seq = input('请输入序列->')
#     if seq:
#         seqs.append(seq.upper())
#     else:
#         break

# for seq in seqs:
#     print(seq)

## 编写一个程序，接受一系列空格分隔的单词作为输入，并在删除所有重复的单词并按字母数字排序后打印这些单词。
## 假设向程序提供以下输入:
## hello world and practice makes perfect and hello world again
## 则输出为:
## again and hello makes perfect practice world
## 提示:在为问题提供输入数据的情况下，应该假设它是控制台输入。
## 我们使用set容器自动删除重复的数据，然后使用sort()对数据进行排序。

# seq = input('请输入序列->').split(' ')
# ls = list(dict.fromkeys(seq))
# ls.sort()
# print(','.join(ls))

## 编写一个程序，接受一系列逗号分隔的4位二进制数作为输入，然后检查它们是否可被5整除。 可被5整除的数字将以逗号分隔的顺序打印。
## 例：
## 0100,0011,1010,1001
## 那么输出应该是：
## 1010
## 注意：假设数据由控制台输入。

# seq = input('请输入序列->').split(',')

# ls = []
# for x in seq:
#     if int(x,2)%5 == 0:
#         ls.append(x)
    
# print(','.join(ls))

## 题：编写一个程序，它将找到1000到3000之间的所有这些数字（均包括在内），这样数字的每个数字都是偶数。
## 获得的数字应以逗号分隔的顺序打印在一行上。

# ls =map(str,[x for x in range(1000,3001) if int(str(x)[0])%2 == 0 and int(str(x)[1])%2 == 0 and int(str(x)[2])%2 == 0 and int(str(x)[3])%2 == 0])

# print(list(ls))

## 编写一个接受句子并计算字母和数字的程序。假设为程序提供了以下输入：
## Hello world! 123
## 然后，输出应该是：
## 字母10
## 数字3

import re

str = input('请输入字符串->')
dt = dict.fromkeys(['char','number'],0)

print(dt)

for x in str:
    if re.findall('[a-z]|[A-Z]',x):
        dt['char'] += 1
    elif re.findall('[0-9]',x):
        dt['number'] += 1
print('字母{}'.format(dt['char']))
print('数字{}'.format(dt['number']))