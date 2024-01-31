class Solution:
    def addDigits(self, num: int) -> int:
        result = num
        while True:
            num = result
            result = 0

            for x in str(num):
                result += int(x)
            if result < 10:
                break

        return result