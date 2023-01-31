class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i,c in enumerate(s):
            lastIndex[c]=i

        beg,end = 0, 0
        res = []
        for i,c in enumerate(s):
            beg+=1
            end = max(end,lastIndex[c]) 
            if i == end:
                res.append(beg)
                beg=0
        return res 
