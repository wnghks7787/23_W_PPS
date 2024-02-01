class Solution:
    def checkRecord(self, s: str) -> bool:
        a_count = 0
        l_count = 0

        for x in s:
            if x == 'A':
                a_count += 1
                l_count = 0
            elif x == 'L':
                l_count += 1
            elif x == 'P':
                l_count = 0
            if a_count >= 2 or l_count >= 3:
                return False
        return True