n = int(input())

name = ""
players = []

for i in range(n):
    x = str(input())
    players.append(x[0])

for i in range(26):
    if players.count(chr(i + ord('a'))) >= 5:
        name += (chr(i + ord('a')))

if name == "":
    print("PREDAJA")
else:
    print(name)