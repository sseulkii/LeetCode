class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        
        d = [1] * len(s)
        sub = ""
        
        for i in range(len(s)):
            if s[i] in sub:
                idx = sub.index(s[i])
                sub = sub[idx + 1:]
            sub += s[i]
            d[i] = len(sub)
            
        return max(d)