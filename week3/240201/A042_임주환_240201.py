class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_a = []
        stack_b = []

        for x in s:
            if x == "#":
                if len(stack_a) != 0:
                    stack_a.pop()
            else:
                stack_a.append(x)
        for x in t:
            if x == "#":
                if len(stack_b) != 0:
                    stack_b.pop()
            else:
                stack_b.append(x)

        if stack_a == stack_b:
            return True
        else:
            return False