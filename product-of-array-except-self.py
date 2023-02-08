class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans= [1]*len(nums)
        right = 1
        left = 1
        beg = 0
        while beg + 1 < len(nums):
            right *= nums[beg]
            ans[beg+1] = right
            beg+=1   
        while beg-1>=0:
            left *= nums[beg]
            ans[beg-1] *= left 
            beg-=1
        return ans
