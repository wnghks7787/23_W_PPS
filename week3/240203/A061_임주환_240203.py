class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        answer = ""

        while True:
            if columnNumber % 26 == 0:
                answer += 'Z'
                columnNumber -= 1

                if (columnNumber / 26) == 1:
                    break
            else:
                answer += chr(ord('A') - 1 + columnNumber % 26)
            columnNumber = int(columnNumber / 26)

            if columnNumber <= 0:
                break

        return answer[::-1]