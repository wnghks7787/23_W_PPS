def solution(board, moves):
    answer = 0
    board_len = len(board[0])
    stack = []
    
    for move in moves:
        puppet = 0
        for i in range(board_len):
            if board[i][move - 1] != 0:
                puppet = board[i][move - 1]
                board[i][move - 1] = 0
                break
        if puppet != 0:
            stack.append(puppet)
        
        if len(stack) > 1 and stack[-1] == stack[-2]:
            answer += 2
            stack.pop()
            stack.pop()
        
    return answer