class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        lst = list(s)
        vowels= ['a','e','i','o','u']
        count = 0 
        new_count =0
        for beg, letter in enumerate(lst):
            if letter in vowels:
                new_count +=1
            if   beg >= k and lst[beg - k] in vowels:
                new_count -=1
            count = max(count,new_count)
        return count
