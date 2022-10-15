class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            return results
        
        if expression.isdigit():
            return [int(expression)]
        
        results = []
        
        for i, c in enumerate(expression):
            if c in '*-+':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                
                results.extend(compute(left, right, c))
        
        return results