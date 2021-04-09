# 选择排序

# 算法步骤
#     1)首先在未排序序列中找到最小(大)元素,存放到排序序列的起始位置
#     2)再从剩余未排序元素中继续寻找最小(大)元素,然后放到已排序序列的末尾
#     3)重复第二步,直到所有元素均排序完毕

# 代码实现

ls = [5, 4, 3, 2, 1]

def SelectSort(sequ):
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


print(SelectSort(ls))
