class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        if not nums:
            return False

        remainderMap = {0: -1}
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            remainder = total % k
            if remainder not in remainderMap:
                remainderMap[remainder] = i
            elif i - remainderMap[remainder] >=2:
                return True
        
        return False