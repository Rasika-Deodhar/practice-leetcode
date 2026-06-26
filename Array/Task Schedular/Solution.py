class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskMap = {}

        for task in tasks:
            if task not in taskMap:
                taskMap[task] = 0
            taskMap[task] += 1
        
        maxFreq = max(taskMap.values())
        countMax = sum(1 for count in taskMap.values() if count==maxFreq)

        formula = (maxFreq - 1) * (n + 1) + countMax

        result = max(formula, len(tasks))

        return result