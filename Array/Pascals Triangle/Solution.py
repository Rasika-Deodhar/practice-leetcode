class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        if numRows==0:
            return triangle

        triangle.append([1])

        for i in range(1,numRows):
            prevRow = triangle[i-1]
            
            currentRow = []
            currentRow.append(1)

            for j in range(1,i):
                currentRow.append(prevRow[j-1]+prevRow[j])
            currentRow.append(1)
            triangle.append(currentRow)

        
        return triangle