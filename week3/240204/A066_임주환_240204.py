x = input()

x_list = list(x)
x_sort = sorted(x_list)
x_reverse = list(reversed(x_sort))

for x in x_reverse:
    print(x, end="")
print()