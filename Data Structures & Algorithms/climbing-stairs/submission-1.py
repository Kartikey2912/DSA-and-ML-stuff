class Solution:
    def climbStairs(self, n: int) -> int:
        
        def fib(n):
            a,b = 0, 1
            if n == 0:
                return 1
            elif n == 1:
                return 1
            else:
                for i in range(1, n):
                    temp = a+b
                    a = b
                    b = temp
                return b
        return fib(n+1) 
        