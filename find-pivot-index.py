class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightSum = sum(nums)
        leftSum = 0
        count = 0
        for beg in range(len(nums)):
            
            rightSum -= nums[beg]
            if rightSum == leftSum :
                return beg
            leftSum +=nums[beg]
        return -1
