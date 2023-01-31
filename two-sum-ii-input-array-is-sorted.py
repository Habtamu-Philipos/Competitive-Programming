class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        beg = 0
        end = len(numbers) -1
        num = []
        while beg < end:
            if numbers[beg] + numbers[end] == target:
                num.append(beg+1)
                num.append(end+1)
                return num
            elif numbers[beg] + numbers[end] > target:
                end-=1
            else: beg+=1
