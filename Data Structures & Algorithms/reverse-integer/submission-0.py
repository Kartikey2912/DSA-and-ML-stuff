class Solution:
    def reverse(self, x: int) -> int:
        flag = True
        if x < 0:
            flag = False
            x *= -1
        
        ans = 0
        cnt = 0
        while x:
            rem = x % 10
            ans = ans * 10 + rem
            cnt += 1
            x //= 10
        if not flag:
            ans *= -1
        if ans < -2 ** 31 or ans > 2**31 -1:
            return 0
        
        return ans
        