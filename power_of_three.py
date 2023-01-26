class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n/3 == 1 or n/3 == 1/3 : return True
        if n/3 == 0 : return False
        return self.isPowerOfThree(n/3)
