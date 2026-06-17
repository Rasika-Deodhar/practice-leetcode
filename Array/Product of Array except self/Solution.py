class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prodAll = 1
        hasZero = 0

        for i in nums:
            if i == 0:
                hasZero+=1
                continue
            prodAll *= i
        
        if hasZero == len(nums):
            result = [0] * hasZero
            return result
        
        for i in range(len(nums)):
            if hasZero:
                if hasZero <2 and nums[i]==0:
                    result.append(prodAll)
                else:
                    result.append(0)
            else:
                result.append(int(prodAll/nums[i]))
        
        return result
