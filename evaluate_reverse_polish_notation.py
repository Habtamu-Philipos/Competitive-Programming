import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.truediv,  
        }
        stack = []
        for c in tokens:
            if stack and c in ops:
                last = int(stack.pop())
                frst= int(stack.pop())
                new = ops[c](frst, last)
                stack.append(new)
            else: stack.append(c)
        return int(stack[0])
