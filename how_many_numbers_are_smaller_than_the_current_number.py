class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = 0
        output = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    count  +=  1
            output.append(count)
            count = 0
        return output
