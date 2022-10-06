class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        
        d = [1] * len(s)
        
        left, right = 0, 0
        sub = ""
        
        while left <= right and right < len(s):
            if s[right] in sub:
                idx = sub.index(s[right])
                sub = sub[idx + 1:]
            sub += s[right]
            d[right] = len(sub)
            right += 1
            
        return max(d)