class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        
        def dfs(node, path):
            if not node:
                return
            
            # If leaf node → store path
            if not node.left and not node.right:
                res.append(path + str(node.val))
                return
            
            # Continue path
            dfs(node.left, path + str(node.val) + "->")
            dfs(node.right, path + str(node.val) + "->")
        
        dfs(root, "")
        return res