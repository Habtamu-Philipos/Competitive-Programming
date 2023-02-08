class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) == 0 : return 0
        left = 0
        odd_count = 0
        nice_sub_arr = 0
        ans = 0

        for r in range(len(nums)):
            if nums[r]%2 != 0:
                odd_count +=1
                nice_sub_arr = 0
            
            while odd_count == k:
                if nums[left] % 2 != 0:
                    odd_count -=1
                nice_sub_arr +=1
                left +=1
            ans += nice_sub_arr
        return ans
