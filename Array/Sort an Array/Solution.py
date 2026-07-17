import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        heap = nums[:]
        result=[]
        heapq.heapify(heap)        
        while(heap):
            result.append(heapq.heappop(heap))

        return result