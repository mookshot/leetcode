# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    val : int = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        if root is None : 
            return None

        # 오른쪽 맨 아래까지 순회.
        # 올라오면서 더해준다. 
        
        self.bstToGst(root.right)
        self.val += root.val
        root.val = self.val
        self.bstToGst(root.left)
        
        return root
        
        