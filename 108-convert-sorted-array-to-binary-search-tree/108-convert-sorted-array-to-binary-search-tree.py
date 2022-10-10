# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        if not nums : 
            return None
        
        mid = len(nums)//2 # 소수점 안나오게 연산.
        
        node = TreeNode(nums[mid])  # 이진탐색
        node.left = self.sortedArrayToBST(nums[:mid]) # 이진탐색
        node.right = self.sortedArrayToBST(nums[mid + 1:]) # 이진탐색
        
        return node