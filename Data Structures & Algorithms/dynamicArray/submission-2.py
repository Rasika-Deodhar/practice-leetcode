import array

class DynamicArray:

    def __init__(self, capacity: int):
        self.length = 0
        self.capacity  = capacity
        self.nums = [-1] * capacity

    def get(self, i: int) -> int:
        return self.nums[i]
    
    def set(self, i: int, n:int) -> None:
        self.nums[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.capacity:
            self.resize()
        i = self.getSize()
        self.nums[i] = n

    def popback(self) -> int:
        popped=self.nums[0]
        for i in range(len(self.nums)-1):
            if self.nums[i+1]==-1:
                popped = self.nums[i]
                # self.nums[i] = -1
        return popped

    def resize(self) -> None:
        self.capacity*=2
        nums1 = [-1]*self.capacity
        for i in range(len(self.nums)):
            nums1[i] = self.nums[i]
        self.nums = nums1

    def getSize(self) -> int:
        count=0
        for i in range(len(self.nums)):
            if self.nums[i]!=-1:
                count+=1
        return count
        
    def getCapacity(self) -> int:
        return self.capacity
