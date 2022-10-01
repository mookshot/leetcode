# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        Queue = collections.deque([root])

        while Queue:
            node = Queue.popleft()
            
            if node : 
                node.left , node.right = node.right , node.left

                Queue.append(node.left)    
                Queue.append(node.right)

        return root