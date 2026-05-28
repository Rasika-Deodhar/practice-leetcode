class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        # l = find 0
        # r = fing non 0
        # swap and count
        count=0
        l=0
        r=len(nums)-1
        while(l<r):
            while(l<len(nums) and nums[l]!=0):
                l+=1
            while(r>0 and nums[r]==0):
                r-=1
            if(l<r):
                temp = nums[r]
                nums[r] = nums[l]
                nums[l] = nums[r]
                count+=1
            l+=1
            r-=1
        return count
    
s = Solution()
print(s.minimumSwaps([0,1,0,3,12]))