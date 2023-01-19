class Solution:
    def sortSentence(self, s: str) -> str:
        S = s.split()
        num = []
        strng =[]
        final = []
        for i in range(len(S)):
            lst = list(S[i])
            nums = lst[-1]
            strngs = lst[:-1]
            strgs = ''.join(strngs)
            num.append(nums)
            strng.append(strgs)
        for i in range(0,len(num)):
            for j in range(len(num) -  i - 1):
                if num[j] > num[j + 1]:
                    (temp1, temp2 )= (num[j], strng[j])
                    (num[j], strng[j]) = (num[j + 1], strng[j+1])
                    (num[j+1],strng[j+1]) = (temp1, temp2)
        for i in range(len(num)):
            sorti =  strng[i]
            final.append(sorti)
        result= ' '.join(final)
        return result 
