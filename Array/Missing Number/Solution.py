class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for index, num in enumerate(nums):
            if index!=num:
                return index
        return len(nums)