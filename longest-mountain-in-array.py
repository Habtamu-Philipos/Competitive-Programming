class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        count = 0
        for indx in range(1,len(arr) -1):
            if arr[indx -1] < arr[indx] > arr[indx +1]:
                beg = end=indx
                while beg > 0 and arr[beg]> arr[beg-1]:
                    beg-=1
                while end+1 <len(arr) and arr[end]> arr[end+1]:
                    end+=1
                count = max(count,(end-beg +1))  
        return count
