class Solution:
    def maxProduct(self, n: int) -> int:
        nums = []
        while n > 0 :
           nums.append(n%10)
           n//=10

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return nums[0] * nums[1]

        max1=0
        max2=0

        for i in nums:
            if i > max1:
                max2 = max1
                max1 = i
            elif i > max2:
                max2 = i
        
        return max1*max2