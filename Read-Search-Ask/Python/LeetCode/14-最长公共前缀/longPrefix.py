# 编写一个函数来查找字符串数组中的最长公共前缀。

# 如果不存在公共前缀，返回空字符串 ""。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-common-prefix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 方式一
class Solution(object):
    def longPrefix(self,strs):
        result = ''
        i = 0
        
        while True:
            try:
                sets = set(string[i] for string in strs)
                if len(sets) == 1:
                    result += sets.pop()
                    i += 1
                else:
                    break
            except Exception:
                break

        return result

# 方式二

s = Solution()
print(s.longPrefix(['flower','flow','flo']))