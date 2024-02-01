class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(num + 1):
            if i == 0:
                continue
            elif num == (i ** 2):
                return True
            elif num < (i ** 2):
                return False