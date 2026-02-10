# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def io(self,node):
    #     if not node:
    #         return
    #     self.io(node.left)
    #     self.res.append(node.val)
    #     self.io(node.right)
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     self.res=[]
    #     self.io(root)
    #     return self.res


    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        stack = []
        curr = root

        while curr or stack:
            # Step 1: Go as left as possible
            while curr:
                stack.append(curr)
                curr = curr.left

            # Step 2: Process node
            curr = stack.pop()
            res.append(curr.val)

            # Step 3: Go to right subtree
            curr = curr.right

        return res
