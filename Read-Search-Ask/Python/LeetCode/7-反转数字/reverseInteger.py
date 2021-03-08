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
