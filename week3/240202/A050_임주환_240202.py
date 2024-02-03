password = input()

for x in password:
    if x == "A":
        print("X", end="")
    elif x == "B":
        print("Y", end="")
    elif x == "C":
        print("Z", end="")
    else:
        print(chr(ord(x) - 3), end="")
print()