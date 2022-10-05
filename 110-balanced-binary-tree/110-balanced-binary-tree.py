# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = True 
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 모든 노드의 서브트리 높이 차이가 1이하인것.
        # 높이차이를 어떻게 비교하지?
        # left 와 right를 계속 비교하면서 가면 될듯.
        
        
        if root is None : 
            return self.res
        
        
        def dfs(node : TreeNode ) -> int : 
            
            if node is None : 
                return 0
            
            left  = dfs(node.left)
            right = dfs(node.right)
            
            if abs(left - right) > 1 :
                self.res = False
                print("left : ", left)
                print("right : ", right)
                print("node.val : ", node.val)
                    
            return max(left,right) + 1

        tmp = dfs(root)
        return self.res