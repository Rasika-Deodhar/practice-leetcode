from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=0
        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[j]=nums[i]
                j+=1
        for i in range(len(nums)-1,j-1,-1):
            nums[i]=0
        print(nums)

sol = Solution()
sol.moveZeroes([0,1,0,3,12])