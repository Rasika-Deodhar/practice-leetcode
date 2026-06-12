class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []:
            return []
        
        intervals.sort(key=lambda x:x[0])

        result = [intervals[0]]

        for i in range(1,len(intervals)):
            currentInterval = result[-1]
            nextInterval = intervals[i]

            if currentInterval[1] >= nextInterval[0]:
                currentInterval[1] = max(currentInterval[1], nextInterval[1])
            else:
                result.append(nextInterval)

        return result