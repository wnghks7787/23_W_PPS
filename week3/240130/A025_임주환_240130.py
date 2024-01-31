class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x = -16

        while True:
            if 4 ** x == n:
                return True
            else:
                x += 1
            if x > 15:
                break

        return False