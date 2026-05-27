from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        val=len(nums) # by default - set last index
        for i in range(len(nums)):
            if target <= nums[i]: # if target index exists - set that one and break
                val=i
                break
        return val
    
sol = Solution()   
print(sol.searchInsert(nums = [1,3,5,6], target = 7))