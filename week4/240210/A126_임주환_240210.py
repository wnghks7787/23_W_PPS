x = input()

x_len = len(x)

if x_len <= 2:
    print(x)
    quit()
elif x_len == 4:
    print(144)
    quit()

answer = 99
for j in range(int(x) - 99):
    j += 100
    j_str = str(j)
    
    d = 0
    for i in range(10):
        if int(j_str[0]) + d == int(j_str[1]) and int(j_str[1]) + d == int(j_str[2]):
            answer += 1
            break
        elif int(j_str[0]) - d == int(j_str[1]) and int(j_str[1]) - d == int(j_str[2]):
            answer += 1
            break

        d += 1

print(answer)