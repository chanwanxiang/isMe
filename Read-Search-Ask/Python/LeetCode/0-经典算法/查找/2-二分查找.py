# 二分查找

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
