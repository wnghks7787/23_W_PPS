class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zeros = nums.count(0)
        length = len(nums)

        nums_tmp = copy.deepcopy(nums)

        j = 0
        for i in range(length):
            if nums_tmp[i] == 0:
                nums[length - zeros] = 0
                zeros -= 1
            else:
                nums[j] = nums_tmp[i]
                j += 1