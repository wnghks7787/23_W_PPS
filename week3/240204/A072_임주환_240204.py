class Solution:
    def dayOfYear(self, date: str) -> int:
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:])

        answer = 0


        if month > 1:
            answer += 31
        if month > 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                answer += 29
            else:
                answer += 28
        if month > 3:
            answer += 31
        if month > 4:
            answer += 30
        if month > 5:
            answer += 31
        if month > 6:
            answer += 30
        if month > 7:
            answer += 31
        if month > 8:
            answer += 31
        if month > 9:
            answer += 30
        if month > 10:
            answer += 31
        if month > 11:
            answer += 30

        answer += day
        return answer