# 给定一个整数数组 nums 和一个整数目标值 target,请你在该数组中找出 和为目标值 的那 两个 整数,并返回它们的数组下标.

# 你可以假设每种输入只会对应一个答案.但是,数组中同一个元素不能使用两遍.

# 你可以按任意顺序返回答案.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/two-sum
# 著作权归领扣网络所有.商业转载请联系官方授权,非商业转载请注明出处.

# 方式一
# class Solution(object):
#     def twoSum(self, nums, target):
#         dt = {}
#         for i, num in enumerate(nums):
#             if target - num in dt:
#                 return [dt[target-num], i]
#             # 记录数字下标
#             dt[num] = i


# s = Solution()
# print(s.twoSum([1, 2, 3], 3))  # [0, 1]

# 方式二
# class Solution(object):
#     def twoSum(self,nums,target):
#         for i in nums:
#             j = target - i
#             startindex = nums.index(i)
#             nextindex = startindex + 1
#             tempNums = nums[nextindex:]
#             if j in tempNums:
#                 return(nums.index(i),nextindex+tempNums.index(j))

# s = Solution()
# print(s.twoSum([1,2,3],4))

# 方式三
class Solution(object):
    def twoSum(self, nums, target):
        dc = dict()
        for i in range(len(nums)):
            if target - nums[i] not in dc:
                dc[nums[i]] = i
            else:
                return [dc[target-nums[i]], i]


s = Solution()
print(s.twoSum([1, 2, 3], 4))


# 扩展
# enumerate(sequence, [start=0])
# sequence -- 一个序列、迭代器或其他支持迭代对象.
# start -- 下标起始位置.
# 返回 enumerate(枚举) 对象.
