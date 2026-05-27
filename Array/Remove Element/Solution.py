from typing import List

class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        r=len(nums)-1
        count=0

        # start from left
        # when val found
        # search non-val element from right
        # swap
        # check for count by using condition (val!=nums[i])

        while(l<r):
            if(nums[l]==val):
                if(nums[r]==val):
                    while(nums[r]==val and r>l):
                        r-=1
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                r-=1
            l+=1
            
        for i in range(len(nums)):
            if(val!=nums[i]):
                count+=1
        return count

sol = Solution()   
print(sol.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))