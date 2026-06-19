class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        current = best = nums[0]

        for i in nums[1:]:
            current = max(i, current+i)
            best = max(current, best)
        
        return best