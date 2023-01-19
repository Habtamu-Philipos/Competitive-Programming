class Solution: 
    
    def select(self, arr, i):
        self.arr = arr
        self.i = i
        self.x= i -1 
        for i in range(self.i,len(self.arr)):
            if self.arr[i] < self.arr[self.x]:
                  self.x = i
        return self.x
            
        
            
                
    
    def selectionSort(self, arr,n):
        self.arr = arr
        self.n = n
        for step in range(self.n):
            selected = Solution.select(self,self.arr, step+1)
            (self.arr[step],self.arr[selected]) =(self.arr[selected],self.arr[step])
        return self.arr
