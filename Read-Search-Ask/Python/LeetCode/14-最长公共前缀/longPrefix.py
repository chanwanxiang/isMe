# 编写一个函数来查找字符串数组中的最长公共前缀

# 如果不存在公共前缀,返回空字符串''

# 来源:力扣(LeetCode)
# 链接:https://leetcode-cn.com/problems/longest-common-prefix

# 方式一
# class Solution(object):
#     def longPrefix(self,strs):
#         result = ''
#         i = 0
        
#         while True:
#             try:
#                 sets = set(string[i] for string in strs)
#                 if len(sets) == 1:
#                     result += sets.pop()
#                     i += 1
#                 else:
#                     break
#             except Exception:
#                 break

#         return result

# 方式二
class Solution(object):
    def longPrefix(self,strs):
        result = ''

        for i in range(len(strs[0])):
            for string in strs[1:]:
                if len(string) <= i  or strs[0][i] != string[i]:
                    break
            else:
                result += strs[0][i]

        return result


s = Solution()
print(s.longPrefix(['flower','flow','flo']))
