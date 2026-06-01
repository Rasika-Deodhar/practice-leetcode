class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits)-1,-1,-1):
            if i==len(digits)-1:
                currSum = sum([digits[i],carry,1])
            else:
                currSum = sum([digits[i],carry])
                carry=0
        
            if currSum < 10 and carry == 0:
                digits[i] = currSum
                break
            else:
                digits[i]=currSum%10
                carry+=int(currSum/10)
            

        if carry:
            digits.insert(0,carry)

        return digits