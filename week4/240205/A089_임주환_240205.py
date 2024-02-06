# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def makeBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 1:
            return TreeNode(val=nums[0])

        pivot = int(len(nums) / 2)
        root = nums[pivot]
        tree = TreeNode(val=root)

        left = nums[:pivot]
        tree.left = self.makeBST(nums=left)

        if len(nums) > pivot + 1:
            right = nums[pivot + 1:]
            tree.right = self.makeBST(nums=right)

        return tree


    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 1:
            result_tree = TreeNode(val=nums[0])
        
        result = self.makeBST(nums)
        return result