n = int(input())

count = 0

for i in range(n):
    word = input()
    group = True

    chrs = [0 for _ in range(26)]
    x_before = ""

    for x in word:
        if x_before == "":
            chrs[ord(x) - ord('a')] += 1
            x_before = x
        else:
            if x_before == x:
                continue
            elif chrs[ord(x) - ord('a')] == 0:
                chrs[ord(x) - ord('a')] += 1
                x_before = x
            else:
                group = False
                break
    if group:
        count += 1

print(count)