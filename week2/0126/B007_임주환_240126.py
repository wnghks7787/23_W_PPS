class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = 0
        n = len(nums)

        while True:
            n = int(len(nums) / 2)

            if target == nums[n]:
                idx += n
                return idx
            elif target > nums[n]:
                nums = nums[n:]
                idx += n
            elif target < nums[n]:
                nums = nums[:n]
            
            if len(nums) == 0 or target != nums[0] and len(nums) == 1:
                return -1