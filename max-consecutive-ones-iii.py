class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        beg = 0 
        for end,n in enumerate(nums):
            k-=(1-n)
            if k < 0 :
                k +=(1- nums[beg])
                beg+=1
        return end - beg + 1
