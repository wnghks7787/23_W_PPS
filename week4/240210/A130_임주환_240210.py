x = int(input())

money = []
for i in range(x):
    tmp = int(input())

    if tmp == 0:
        money.pop()
        continue
    
    money.append(tmp)

print(sum(money))