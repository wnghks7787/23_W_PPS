x = int(input())

books = []
books_one = []

for i in range(x):
    tmp = input()

    if tmp not in books_one:
        books_one.append(tmp)

    books.append(tmp)


best = []
best_num = 0
for book in books_one:
    if best_num < books.count(book):
        best.clear()
        best.append(book)
        best_num = books.count(book)
    elif best_num == books.count(book):
        best.append(book)

best = sorted(best)
print(best[0])