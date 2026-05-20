
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefixString = ""
        j=0
        minLengthIndex = min(range(len(strs)), key=lambda i:len(strs[i]))
        while j<len(strs[minLengthIndex]):
            currentString=""
            for i in range(len(strs)):
                if currentString == "":
                    currentString+=strs[i][j]
                if currentString[-1]!=strs[i][j]:
                    return prefixString
            prefixString+=currentString
            j+=1
        return prefixString
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["ab", "a"]))