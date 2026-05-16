class LinkedList:
    
    def __init__(self):
        self.nums=[]
    
    def get(self, index: int) -> int:
        if index < len(self.nums):
            return self.nums[index]
        else:
            return -1
        

    def insertHead(self, val: int) -> None:
        if not self.nums:
            self.nums.append(val)
        
        else:
            self.nums.append(-1)
            print(self.nums)
            for i in range(len(self.nums)-1,-1,-1):
                self.nums[i] = self.nums[i-1]
            self.nums[0]=val
            print(self.nums)
            

    def insertTail(self, val: int) -> None:
        self.nums.append(val)       

    def remove(self, index: int) -> bool:
        print(index)
        if self.nums.pop(index):
            return True 
        else:
            return False

    def getValues(self) -> List[int]:
        return self.nums
