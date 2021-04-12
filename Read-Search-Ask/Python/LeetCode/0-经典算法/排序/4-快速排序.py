# 快速排序

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
