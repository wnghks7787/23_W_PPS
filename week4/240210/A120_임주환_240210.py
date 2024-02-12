class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        alphabet_s = [0 for _ in range(26)]
        alphabet_t = [0 for _ in range(26)]

        for i in range(len(t)):
            if i + 1 == len(t):
                alphabet_t[ord(t[i]) - ord('a')] += 1
            else:
                alphabet_s[ord(s[i]) - ord('a')] += 1
                alphabet_t[ord(t[i]) - ord('a')] += 1

        for i in range(26):
            if alphabet_s[i] != alphabet_t[i]:
                return chr(ord('a') + i)