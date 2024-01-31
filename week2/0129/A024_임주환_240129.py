class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        twenty = 0

        possibility = True

        for bill in bills:
            if bill == 5:
                five += 1
            
            if bill == 10:
                if five == 0:
                    possibility = False
                    break
                else:
                    five -= 1
                    ten += 1
            
            if bill == 20:
                if (ten >= 1) and (five >= 1):
                    ten -= 1
                    five -= 1
                    twenty += 1
                elif five >= 3:
                    five -= 3
                    twenty += 1
                else:
                    possibility = False
                    break

        return possibility