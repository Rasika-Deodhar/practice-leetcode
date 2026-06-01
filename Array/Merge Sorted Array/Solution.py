class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 and n == 1:
            nums1[0]=nums2[0]
            return
        if n == 0:
            return
        i=0 
        k=m
        j=0
        while(j < n and i < m+n):
            if nums1[i] > nums2[j]:
                for l in range(k,i,-1):
                    nums1[l]=nums1[l-1]
                nums1[i] = nums2[j]
                k+=1
                j+=1        
            i+=1
        if k<m+n:
            while(j<n):
                nums1[k]=nums2[j]
                j+=1
                k+=1
        print(nums1)