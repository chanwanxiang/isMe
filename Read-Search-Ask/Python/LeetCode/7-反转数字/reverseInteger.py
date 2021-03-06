# 给你一个 32 位的有符号整数 x ,返回 x 中每位上的数字反转后的结果.

# 如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ,就返回 0.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-integer
# 著作权归领扣网络所有.商业转载请联系官方授权,非商业转载请注明出处.

class Solution:
    def reverse(self, x):
        num = 0
        # 取绝对值
        a = abs(x)

        while(a != 0):
            # 123
            # a = 123
            # num = 0
            # first iteration
            # a = 12
            # num = 3
            # second iteration
            # a = 1
            # num = 32
            # third iteration
            # a = 0
            # num = 321
            temp = a % 10
            num = num * 10 + temp
            a = int(a/10)

        if x > 0 and num < 2**31 - 1:
            return num
        elif x < 0 and num <= 2**31:
            return -num
        else:
            return 0


s = Solution()
print(s.reverse(-123))
