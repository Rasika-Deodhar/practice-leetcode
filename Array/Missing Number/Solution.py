class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 0 1 ... n-1

        nums.sort()

        for i in range(len(nums)):
            if i+1 not in nums:
                return i+1
        
        return 0
