# 罗马数字包含以下七种字符:I, V, X, L,C,D和M

# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 例如,罗马数字2写做II,即为两个并列的1,12 写做XII,即为X+II

# 通常情况下,罗马数字中小的数字在大的数字的右边,但也存在特例,例如4不写做IIII,而是IV,数字1在数字5的左边,所表示的数等于大数5减小数1得到的数值4,同样地,数字9表示为IX,这个特殊的规则只适用于以下六种情况

# I 可以放在V(5)和X(10)的左边,来表示4和9
# X 可以放在L(50)和C(100)的左边,来表示40和90
# C 可以放在D(500)和M(1000)的左边,来表示400和900
# 给定一个罗马数字,将其转换成整数,输入确保在1到3999的范围内

# 来源:力扣(LeetCode)
# 链接:https://leetcode-cn.com/problems/roman-to-integer

class Solution(object):
    def romanToInt(self, s):
        # 字母数字映射
        numMap = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # 返回结果
        result = 0
        # 遍历输入的字符串,i=0时直接加入result,i大于零开始判断与前位关系,如果大于前一位,在本身详相减规则的基础上还要把上次相加
        for i in range(len(s)):
            if i > 0 and numMap[s[i]] > numMap[s[i-1]]:
                result += numMap[s[i]] - 2*numMap[s[i-1]]
            else:
                result += numMap[s[i]]
        return result


s = Solution()
print(s.romanToInt('CMXCIX'))
