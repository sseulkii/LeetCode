class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        
        for s in strs:
            anagram = "".join(sorted(s))
            
            if anagram not in d:
                d[anagram] = [s]
            else:
                d[anagram] += [s]
                
        result = []
        for v in d.values():
            result.append(v)
            
        return result