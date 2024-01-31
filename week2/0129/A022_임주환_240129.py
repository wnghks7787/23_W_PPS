import math

N = int(input())

Y = 0
M = 0

call_times = list(map(int, input().split()))

for call_time in call_times:
    call_time+=1
    Y += (math.ceil(call_time / 30) * 10)
    M += (math.ceil(call_time / 60) * 15)

if M == Y:
    print("Y M", Y)
elif M < Y:
    print("M", M)
else:
    print("Y", Y)