class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        que = deque(sorted(tokens))
        score =0
        max_score = 0

        while que:
            if power >= que[0]:
                power -= que.popleft()
                score += 1
                max_score = max(score,max_score)
            elif score > 0:
                power += que.pop()
                score -= 1
            else: break
        return max_score
