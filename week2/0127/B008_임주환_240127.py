class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = 0

        if len(nums) == 1:
            if target <= nums[0]:
                return 0
            else:
                return 1

        while True:
            n = int(len(nums) / 2)

            if target == nums[n]:
                idx += n
                return idx
            elif target < nums[n]:
                nums = nums[:n]
            else:
                nums = nums[n:]
                idx += n

            if target > nums[0] and len(nums) == 1:
                idx += n
                return idx
            elif target <= nums[0] and len(nums) == 1:
                return idx