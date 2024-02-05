from collections import deque

N = int(input())
rotate = False

cards = deque([i + 1 for i in range(N)])

while True:
    if len(cards) == 1:
        break
    
    if not rotate:
        cards.popleft()
    else:
        cards.rotate(-1)
    rotate = not rotate

print(cards[0])