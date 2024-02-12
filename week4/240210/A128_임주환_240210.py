while True:

    s = input()
    
    if s == '.':
        break

    flag = True
    bracket = []
    for c in s:
        if c == '(' or c == '[':
            bracket.append(c)
        elif (c == ')' or c == ']') and len(bracket) == 0:
            flag = False
            break
        elif c == ')':
            if bracket[-1] != '(':
                flag = False
                break
            else:
                bracket.pop()
        elif c == ']':
            if bracket[-1] != '[':
                flag = False
                break
            else:
                bracket.pop()
        
    if flag and len(bracket) == 0:
        print('yes')
    else:
        print('no')