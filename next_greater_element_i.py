class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indx_nums1 = {n:i for i, n in enumerate(nums1)}
        stack = []
        result = [-1] * len(nums1)
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                x= stack.pop()
                y=indx_nums1[x]
                result[y]= nums2[i]
            if nums2[i] in  nums1:
                stack.append(nums2[i]) 
        return result
