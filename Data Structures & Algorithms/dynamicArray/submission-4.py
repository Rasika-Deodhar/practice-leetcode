class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.nums = [-1] * capacity

    def get(self, i: int) -> int:
        return self.nums[i]

    def set(self, i: int, n: int) -> None:
        self.nums[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.nums[self.length]=n
        self.length+=1

    def popback(self) -> int:
        print(self.nums, self.length)
        popped = self.nums[self.length-1]
        self.nums[self.length-1] = -1
        # self.nums[-1] = -1
        self.length-=1
        return popped

    def resize(self) -> None:
        self.nums = self.nums + [-1] * self.capacity
        self.capacity*=2

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
