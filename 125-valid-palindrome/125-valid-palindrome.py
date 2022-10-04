from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        q = deque([])
        
        for c in s:
            if c.isalnum():
                q.append(c.lower())
        
        while q:
            if len(q) == 1:
                return True
            if q.popleft() != q.pop():
                return False
            
        return True