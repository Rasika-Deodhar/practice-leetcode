class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        int_list = [int(num) for num in str(x)]

        ifHarshad =  sum(int_list) if x % sum(int_list) == 0 else -1

        return ifHarshad