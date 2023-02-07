class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        beg= 0
        end = len(cardPoints) -k
        total = sum(cardPoints[end:])
        ans = total
        while end < len(cardPoints):
            total += (cardPoints[beg]  - cardPoints[end])
            ans = max(ans, total)
            end+=1
            beg+=1
        return ans
