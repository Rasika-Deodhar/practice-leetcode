class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows = len(matrix)
        cols = len(matrix[0])

        topRow = 0
        bottomRow = rows-1
        leftCol = 0
        rightCol = cols-1

        while(topRow <= bottomRow and leftCol <= rightCol):

            # left to right
            for i in range(leftCol, rightCol+1):
                result.append(matrix[topRow][i])
            topRow += 1

            # top to bottom
            for i in range(topRow, bottomRow+1):
                result.append(matrix[i][rightCol])
            rightCol -= 1

            # right to left
            if (topRow <= bottomRow):
                for i in range(rightCol, leftCol-1, -1):
                    result.append(matrix[bottomRow][i])
                bottomRow -= 1

            # bottom to top
            if (leftCol <= rightCol):
                for i in range(bottomRow, topRow-1, -1):
                    result.append(matrix[i][leftCol])
                leftCol += 1
        
        return result
