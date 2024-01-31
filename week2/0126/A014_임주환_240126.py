class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        start = nums[0]
        end = nums[0]

        result = []

        for i in range(len(nums)):
            if i == 0:
                continue
            elif nums[i - 1] + 1 == nums[i]:
                end = nums[i]
            else:
                if start == end:
                    result.append(str(start))
                else:
                    result.append("{0}->{1}".format(start, end))
                start = nums[i]
                end = nums[i]

        if start == end:
            result.append(str(start))
        else:
            result.append("{0}->{1}".format(start, end))
        return result