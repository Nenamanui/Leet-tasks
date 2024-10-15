class Solution:
    def fib(self, n: int) -> int:
        num = {0 : 0, 1 : 1}
        if n == 0 or n == 1:
            return n
        for item in range(2, n + 1):
            num[item] = num[item - 1] + num[item - 2]
        return num[n]