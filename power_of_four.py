class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n/4 == 1 or n/4 == 1/4 : return True
        if n/4 == 0 : return False
        return self.isPowerOfFour(n/4) 
