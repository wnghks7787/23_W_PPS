class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        num = 0

        for i in range(length):
            ten = 10 ** i
            num += (digits[length - i - 1] * ten)
        
        num += 1

        num_str = str(num)
        num_list = []
        for number in num_str:
            num_list.append(int(number))

        return num_list