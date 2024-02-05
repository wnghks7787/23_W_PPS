word = input()
time = 0
list_time = 0

for char in word:
    if ord(char) >= ord('A') and ord(char) <= ord('C'):
        time += 3
    elif ord(char) >= ord('D') and ord(char) <= ord('F'):
        time += 4
    elif ord(char) >= ord('G') and ord(char) <= ord('I'):
        time += 5
    elif ord(char) >= ord('J') and ord(char) <= ord('L'):
        time += 6
    elif ord(char) >= ord('M') and ord(char) <= ord('O'):
        time += 7
    elif ord(char) >= ord('P') and ord(char) <= ord('S'):
        time += 8
    elif ord(char) >= ord('T') and ord(char) <= ord('V'):
        time += 9
    else:
        time += 10

print(time)