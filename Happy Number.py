class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  
        while True:
            sum = 0
            while n:
                sum = sum + (n % 10) * (n % 10)
                n = n // 10
            n = sum
            if n == 1:
                return True
            if n in seen:  
                return False
            seen.add(n)