class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        answer = [0 for _ in range(len(nums))]

        for i in range(len(answer)):
            
            for j in range(len(nums)):
                if i % 2 == 0:
                    if nums[j] % 2 == 0:
                        answer[i] = nums[j]
                        del nums[j]
                        break
                else:
                    if nums[j] % 2 == 1:
                        answer[i] = nums[j]
                        del nums[j]
                        break

        return answer