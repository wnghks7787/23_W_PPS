s = input()

count = 0

for char in s:
    count += 1

    if count == 10:
        count = 0
        print(char, end="\n")
    else:
        print(char, end="")
print()