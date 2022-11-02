class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        for cookie in s:
            for greed in g:
                if cookie >= greed:
                    count += 1
                    g.remove(greed)
                    break
                else:
                    break
        return count