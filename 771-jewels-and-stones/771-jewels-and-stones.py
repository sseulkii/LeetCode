class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        d = {}
        
        for jewel in jewels:
            d[jewel] = 0
            
        for stone in stones:
            if stone in d:
                d[stone] += 1
                
        count = 0
        for v in d.values():
            count += v
            
        return count