class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        count = 0

        for i in range(len(g)):
            for j in range(len(s)):
                if g[i] <= s[j]:
                    count += 1
                    s.remove(s[j])
                    break

        return count

        