class Solution:
    # def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     self.result = []
    #     self.dfs(root)
    #     return self.result

    # def dfs(self, node):
    #     if not node:
    #         return
    #     self.result.append(node.val)
    #     self.dfs(node.left)
    #     self.dfs(node.right)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [root]
        res=[]
        
        while stack:
            n=stack.pop()
            res.append(n.val)
            if n.right:
                stack.append(n.right)
            if n.left:
                stack.append(n.left)
            
        return res

