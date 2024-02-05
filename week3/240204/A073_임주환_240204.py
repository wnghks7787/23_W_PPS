class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(n):
            tmp = ""
            i += 1

            if i % 3 == 0:
                tmp += "Fizz"
            if i % 5 == 0:
                tmp += "Buzz"
            if i % 3 != 0 and i % 5 != 0:
                tmp += str(i)

            answer.append(tmp)

        return answer