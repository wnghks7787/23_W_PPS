def solution(s):
    answer = ''
    
    jadens = list(map(str, s.split(" ")))
    
    for jaden in jadens:
        jaden = jaden.lower()
        jaden = jaden.capitalize()
        answer += jaden
        answer += " "
    answer = answer[:-1]
    
    return answer