import copy


def BFS(mat, start_num):
    start_num -= 1
    queue = [start_num]
    result = []

    while True:
        if len(queue) == 0:
            break

        for i in range(len(mat)):
            if mat[queue[0]][i] == 1:
                if (i not in queue) and (i not in result):
                    queue.append(i)
                    mat[queue[0]][i] = 0
                    mat[i][queue[0]] = 0
        result.append(queue[0])
        queue.pop(0)

    return plus_one_in_list(result)

def DFS(mat, start_num):
    start_num -= 1
    stack = [start_num]
    result = [start_num]

    while True:
        if len(stack) == 0:
            break
        
        for i in range(len(mat)):  
            if mat[stack[-1]][i] == 1:
                if (i not in stack) and (i not in result):
                    stack.append(i)
                    result.append(stack[-1])
                mat[stack[-1]][i] = 0
                mat[i][stack[-1]] = 0
                break

        if 1 not in mat[stack[-1]]:
            stack.pop()

    return plus_one_in_list(result)

def make_matrix(mat_size, mat):
    result_mat = zero_matrix(mat_size)
    
    for i in range(len(mat)):
        result_mat[mat[i][0] - 1][mat[i][1] - 1] = 1
        result_mat[mat[i][1] - 1][mat[i][0] - 1] = 1

    return result_mat

def zero_matrix(mat_size):
    zero = []
    
    for i in range(mat_size):
        line = []
        for j in range(mat_size):
            line.append(0)
        zero.append(line)
    
    return zero

def plus_one_in_list(lists):
    for i in range(len(lists)):
        lists[i] += 1
    return lists

N, M, V = map(int, input().split())

mat = []

for i in range(M):
    a = list(map(int, input().split()))
    mat.append(a)

graph_dfs = make_matrix(mat_size=N, mat=mat)
graph_bfs = copy.deepcopy(graph_dfs)
graph_dfs = DFS(graph_dfs, V)
graph_bfs = BFS(graph_bfs, V)
print(*graph_dfs)
print(*graph_bfs)