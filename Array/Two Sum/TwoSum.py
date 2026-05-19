class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        k={}
        currentSum=0
        for i in range(len(nums)):
            k[nums[i]]=i
        print(k)
        for i in range(len(nums)):
            if target-nums[i] in k and k[target-nums[i]]!=i:
                return[i,k[target-nums[i]]]

        # n-square
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         currentSum=nums[i]+nums[j]
        #         if currentSum==target:
        #             return [i,j]