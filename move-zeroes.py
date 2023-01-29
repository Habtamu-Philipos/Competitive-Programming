class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        start = 0 
        for end in range(len(nums)):
            if nums[end] :
                nums[start],nums[end]= nums[end],nums[start]
                start+=1
        return nums
