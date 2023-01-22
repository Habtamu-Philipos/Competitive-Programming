class Solution:
    def reverseParentheses(self, s: str) -> str:
        lst= list(s)
        stack = []
        i = 0 
        while(i<len(lst)):
            if lst[i]!=')':
                stack.append(lst[i])
                print(stack)
            else: 
                stackPopped=[]
                while (stack[-1]!='('):
                    stackPopped.append(stack.pop())
                    print(stackPopped)
                print(stack)
                stack.pop()
                stack.extend(stackPopped)
                print(stack)
            i+=1
        return ''.join(stack)   
