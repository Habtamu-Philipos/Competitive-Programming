class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        num = []
        l = 0 
        total = 0
        if sum(nums) < target: return 0
        for r in range(len(nums)):
            total+=nums[r]
            if target == nums[r]: return 1
            while total >= target:
                    num.append(r-l+1)
                    total -=nums[l]
                    l +=1
        return min(num)
