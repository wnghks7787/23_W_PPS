class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s_deque = deque(s)
        goal = deque(goal)

        while True:
            if s_deque == goal:
                return True
            else:
                s_deque.rotate(1)
            
            if s_deque == deque(s):
                return False
            