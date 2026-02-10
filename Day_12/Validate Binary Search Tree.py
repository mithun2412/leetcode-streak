class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, mn, mx):
            if not node:
                return True

            # current node must be strictly between mn and mx
            if not (mn < node.val < mx):
                return False

            # left subtree: values < node.val
            # right subtree: values > node.val
            return (validate(node.left, mn, node.val) and
                    validate(node.right, node.val, mx))

        return validate(root, float('-inf'), float('inf'))
