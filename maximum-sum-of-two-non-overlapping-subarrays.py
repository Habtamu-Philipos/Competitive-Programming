class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        if len(nums) < firstLen + secondLen: return 0
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        res, maxL, maxM = nums[firstLen + secondLen - 1], nums[firstLen - 1], nums[secondLen - 1]
        for i in range(firstLen + secondLen, len(nums)):
            maxL = max(maxL, nums[i - secondLen] - nums[i - secondLen - firstLen])
            maxM = max(maxM, nums[i - firstLen] - nums[i - firstLen - secondLen])
            res = max(res, maxL + nums[i] - nums[i - secondLen], maxM + nums[i] - nums[i -firstLen])
        return res
