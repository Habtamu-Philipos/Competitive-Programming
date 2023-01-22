class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        nums=list(num)
        stack=[]
        for val in nums:
            while k > 0 and stack and stack[-1] > val:
                    stack.pop()
                    k-=1
            stack.append(val)
        stack = stack[:len(stack) - k]
        res=''.join(stack)
        return str(int(res)) if res else '0'
