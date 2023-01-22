class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr=[]
        for i in range(n):
            if (i+1) % 3 == 0 and (i+1) % 5 == 0:
                ans= "FizzBuzz"
                arr.append(ans)
            elif (i+1) % 3 == 0: 
                ans ="Fizz"
                arr.append(ans)
            elif (i+1) % 5 == 0:
                ans = "Buzz" 
                arr.append(ans)
            else: arr.append(str(i+1))
        return arr
