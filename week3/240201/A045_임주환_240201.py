word = str(input())

each_word = [0 for i in range(26)]

word = word.upper()

for x in word:
    each_word[ord(x) - ord('A')] += 1

max = 0
result = ''

for i in range(len(each_word)):
    if max < each_word[i]:
        max = each_word[i]
        result = chr(i + ord('A'))
    elif max == each_word[i]:
        result = '?'

print(result)