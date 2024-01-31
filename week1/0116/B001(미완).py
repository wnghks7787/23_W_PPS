import numpy as np

def make_matrix(n, pair_list):
    mat = np.zeros((n, n), dtype=int)
    for pair in pair_list:
        mat[pair[0] - 1][pair[1] - 1] = 1
        mat[pair[1] - 1][pair[0] - 1] = 1

    return mat

# def BFS(mat):


n = int(input())
c_pair = int(input())

virus_com = [1]
com = []

for i in range(c_pair):
    c1, c2 = map(int, input().split())

    com.append([c1, c2])

mat = make_matrix(n, com)

print(mat)


for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            if i + 1 in virus_com:
                virus_com.append(j + 1)
            elif j + 1 in virus_com:
                virus_com.append(i + 1)

virus_com_n = np.unique(virus_com).size

print(virus_com_n)