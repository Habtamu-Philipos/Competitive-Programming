class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def getIndex(currIndx,steps,length):
            newIndx = currIndx + steps - 1
            if newIndx >= length : 
                newIndx %= length
                 
            return newIndx
        def ans(arr, indx):
            length = len(arr)
            if length == 1: return arr[0]
            else: 
                arr.pop(indx)
                return ans(arr,getIndex(indx,k,length-1))
        return ans([i for i in range(1,n+1)],getIndex(0,k,n))
