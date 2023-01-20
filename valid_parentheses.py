class Solution:
    def isValid(self, s: str) -> bool:
        S = list(s)
        stack = []
        close_to_open = {')':'(', ']':'[', '}':'{'}
        for k in S:
            if k in close_to_open:
                if  stack and stack[-1]==close_to_open[k]:
                    stack.pop()
                else: return False
            else : stack.append(k)
        return  True if not stack else False
