class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        d = [0] * len(s)
        d[0] = 1
        tmp = s[0]
        
        for i in range(1, len(s)):
            if s[i] not in tmp:
                tmp += s[i]
                d[i] = len(tmp)
            else:
                idx = tmp.index(s[i])
                tmp = tmp[idx + 1:]
                tmp += s[i]
                d[i] = len(tmp)
                
        return max(d)