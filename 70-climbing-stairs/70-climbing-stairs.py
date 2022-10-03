class Solution:
    def climbStairs(self, n: int) -> int:
        d = [0] * 46
        
        def climb(x):
            
            if x == 1 or x == 2:
                return x
            
            if d[x] != 0:
                return d[x]
            
            d[x] = climb(x - 1) + climb(x - 2)
            
            return d[x]
            
        return climb(n)