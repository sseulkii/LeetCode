class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        s = ""
        
        for c in paragraph:
            if c.isalpha():
                s += c.lower()
            else:
                s += " "
            
        words = s.split()
        d = {}
        
        for word in words:
            if word in banned:
                continue
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
        
        return max(d.items(), key = lambda x: x[1])[0]