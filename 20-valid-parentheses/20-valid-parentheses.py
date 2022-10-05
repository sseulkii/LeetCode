class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        if len(s) % 2 == 1:
            return False
        
        for c in s:
            if c in ")]}":
                try:
                    pop = stack.pop()
                    if (c == ")" and pop != "(") or (c == "]" and pop != "[") or (c =="}" and pop != "{"):
                        return False
                except:
                    return False
            else:
                stack.append(c)
        
        if len(stack) >= 1:
            return False
        
        return True