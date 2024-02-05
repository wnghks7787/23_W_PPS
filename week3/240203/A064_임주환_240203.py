class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)

        wrong = 0

        for i in range(len(heights)):
            if expected[i] != heights[i]:
                wrong += 1

        return wrong