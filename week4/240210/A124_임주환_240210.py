x = int(input())

prime = []
current_prime = 2

while True:
    if x == 1:
        break

    if x % current_prime == 0:
        prime.append(current_prime)
        x = int(x / current_prime)
    else:
        current_prime += 1

for i in range(len(prime)):
    print(prime[i])