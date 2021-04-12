# 给你一个整数x,如果x是一个回文整数,返回true;否则,返回false

# 回文数是指正序(从左向右)和倒序(从右向左)读都是一样的整数,例如,121是回文,而123不是

# 来源:力扣(LeetCode)
# 链接:https://leetcode-cn.com/problems/palindrome-number

class Solution(object):
    def isPal(self, x):
        a = abs(x)
        num = 0
        while a != 0:
            # 取模,个位数向上取
            tem = a % 10
            # 反转后的数字
            num = num*10 + tem
            # 整数除法,去除个位数之后的数
            a = a//10

        if x >= 0 and x == num:
            return True
        else:
            return False


s = Solution()
print(s.isPal(12121))
