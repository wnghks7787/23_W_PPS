class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = '0b' + a
        b = '0b' + b

        sum = int(a, 2) + int(b, 2)
        sum = bin(sum)[2:]
        return sum