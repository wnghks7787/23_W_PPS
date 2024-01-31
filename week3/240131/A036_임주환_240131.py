class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        length = right - left + 1
        sdn = left
        for i in range(length):
            flag = True

            for num in str(sdn):
                if int(num) == 0:
                    flag = False
                    break
                elif sdn % int(num) != 0:
                    flag = False
                    break
            
            if flag:
                result.append(sdn)
            sdn += 1

        return result