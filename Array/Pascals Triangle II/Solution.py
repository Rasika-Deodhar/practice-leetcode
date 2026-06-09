class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        result = []

        leftZero = [0,1]
        rightZero = [1,0]

        for i in range(rowIndex):
            result=[x+y for x,y in zip(leftZero,rightZero)]
            leftZero = [0]+result
            rightZero = result+[0]        

        return result