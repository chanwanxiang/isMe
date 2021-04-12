# 线性查找
#     适合无序序列查找元素

# 算法步骤
#   线性查找指按一定的顺序检查数组中每一个元素,直到找到所要寻找的特定值为止

def lineSearch(sequ,item):
    for i in range(len(sequ)):
        if sequ[i] == item:
             return f'元素在{i}号位'
    else:
        return '元素不在序列中'

print(lineSearch([1,2,3,4,5],4))
