class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_tmp = nums1[:m]

        i = 0
        while True:
            if len(nums1_tmp) > 0 and len(nums2) > 0:
                if nums1_tmp[0] >= nums2[0]:
                    nums1[i] = nums2[0]
                    del nums2[0]
                else:
                    nums1[i] = nums1_tmp[0]
                    del nums1_tmp[0]
            elif len(nums1_tmp) == 0 and len(nums2) > 0:
                nums1[i] = nums2[0]
                del nums2[0]
            elif len(nums1_tmp) > 0 and len(nums2) == 0:
                nums1[i] = nums1_tmp[0]
                del nums1_tmp[0]
            else:
                break
            i += 1