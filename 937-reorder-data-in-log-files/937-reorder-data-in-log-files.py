class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        
        
        for log in logs:
            if log[-1].isalpha():
                space = log.index(" ")
                letter_logs.append([log[:space + 1], log[space + 1:]])
            else:
                digit_logs.append(log)
                
        letter_logs.sort(key = lambda x: (x[1], x[0]))
        
        letter_logs = ["".join(log) for log in letter_logs]
            
        return letter_logs + digit_logs