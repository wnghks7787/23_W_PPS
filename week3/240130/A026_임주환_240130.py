def solution(x):
    answer = True
    
    num = 0
    
    for s in str(x):
        num += int(s)
        
    if x % num != 0:
        answer = False
    return answer