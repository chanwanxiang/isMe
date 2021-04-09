# 冒泡排序

# 算法步骤
#     1)比较相邻的元素,如果第一个比第二个大,就交换他们两个
#     2)对每一对相邻元素作同样的工作,从开始第一对到结尾的最后一对这步做完后,最后的元素会是最大的数
#     3)针对所有的元素重复以上的步骤,除了最后一个
#     4)持续每次对越来越少的元素重复上面的步骤,直到没有任何一对数字需要比较

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
