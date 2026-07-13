class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate = {}

        for num in nums:
            if num not in duplicate:
                duplicate[num]=1
            else:
                return num
        return 0