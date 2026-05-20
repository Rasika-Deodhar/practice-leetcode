from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=0
        r=0
        count=0
        unique=set()
        while(r<len(nums)):
            if nums[r] not in unique:
                unique.add(nums[r])
                count+=1
                if(l<r):
                    nums[l]=nums[r]
                l+=1
            r+=1

        print(count)
        return count

        