class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        str_n = str(n)

        return str_n.count('1')