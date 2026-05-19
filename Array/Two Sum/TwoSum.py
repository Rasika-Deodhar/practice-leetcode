class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # O(n)
        k={}
        for i,v in enumerate(nums):
            k[target-v] = i
        print(k)
        for i,v in enumerate(nums):
            if v in k and k[v]!=i:
                return [i,k[v]]

        # n-square
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         currentSum=nums[i]+nums[j]
        #         if currentSum==target:
        #             return [i,j]