s = input()

suffix = []

for i in range(len(s)):
    suffix.append(s[i:])

suffix_sorted = sorted(suffix)

for suf in suffix_sorted:
    print(suf)