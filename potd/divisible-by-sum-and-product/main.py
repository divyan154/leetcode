class Solution:
    def checkDivisibility(self, n: int) -> bool:
        prod , tot , num = 1, 0, n
        
        while n != 0:
            rem = n % 10
            prod *= rem
            tot += rem
            n = n // 10
        print(tot)
        print(prod)
        return True if num % (prod + tot) == 0 else False 

# Time complexity - 0(logn)
# Space Complexity -  0(1)