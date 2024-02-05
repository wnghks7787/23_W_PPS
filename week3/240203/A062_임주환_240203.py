def solution(a, b):
    answer = ''
    date = 0
    
    if a > 1:
        date += 31
    if a > 2:
        date += 29
    if a > 3:
        date += 31
    if a > 4:
        date += 30
    if a > 5:
        date += 31
    if a > 6:
        date += 30
    if a > 7:
        date += 31
    if a > 8:
        date += 31
    if a > 9:
        date += 30
    if a > 10:
        date += 31
    if a > 11:
        date += 30
        
    date += b
    
    if date % 7 == 0:
        answer = 'THU'
    elif date % 7 == 1:
        answer = 'FRI'
    elif date % 7 == 2:
        answer = 'SAT'
    elif date % 7 == 3:
        answer = "SUN"
    elif date % 7 == 4:
        answer = "MON"
    elif date % 7 == 5:
        answer = "TUE"
    elif date % 7 == 6:
        answer = "WED"
    return answer