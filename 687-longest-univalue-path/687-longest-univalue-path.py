# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res :int = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs ( node : TreeNode, pre_val : int ) :

            if node is None :  # 마지막이면 -1 리턴
                return -1
            
            left  = dfs(node.left , node.val )
            right = dfs(node.right, node.val )
            
        
            self.res = max(self.res, left+right+2)
            
            if pre_val == node.val :
                return max(left, right) + 1
            else :
                return -1
        dfs(root,9999)
        return self.res
        