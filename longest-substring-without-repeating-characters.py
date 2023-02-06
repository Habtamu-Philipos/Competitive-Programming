class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst = list(s)
        r = 0
        leng = 0
        for i in range(len(lst)):
            ans=[]
            while r < len(lst) and lst[r] not in ans:
                ans.append(lst[r])
                r += 1
            r= i + 1
            leng = max(leng, len(ans))
        return leng
