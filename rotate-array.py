class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k  % len(nums)
        beg , end = 0, len(nums)-1
        while beg < end:
            nums[beg],nums[end] = nums[end],nums[beg]
            beg+=1
            end-=1
        beg , end = 0, k-1
        
        while beg < end:
            nums[beg],nums[end] = nums[end],nums[beg]
            beg+=1
            end-=1
        beg , end = k, len(nums)-1
        
        while beg < end:
            nums[beg],nums[end] = nums[end],nums[beg]
            beg+=1
            end-=1
        return nums
