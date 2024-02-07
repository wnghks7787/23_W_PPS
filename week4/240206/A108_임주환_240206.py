test = int(input())

for i in range(test):
    x = input()

    x_reversed = x[::-1]
    summation = str(int(x) + int(x_reversed))

    palindrome = True
    for j in range(int(len(summation) / 2)):
        if summation[j] != summation[len(summation) - 1 - j]:
            palindrome = False
            break

    if palindrome:
        print("YES")
    else:
        print("NO")