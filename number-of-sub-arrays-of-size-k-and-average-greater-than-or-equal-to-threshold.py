class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        beg = 0
        end = 0
        currSum =  sum(arr[beg : k -1])
        count = 0
        while beg < len(arr) -k + 1:
            currSum += arr[beg + k -1]
            if currSum/k >= threshold:
                count += 1
            currSum -= arr[beg]
            end += 1
            beg += 1
        return count
