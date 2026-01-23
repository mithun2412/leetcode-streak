# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def pot(self, node, l):
        if node is None:
            l.append(None)   # important to track structure
            return

        l.append(node.val)
        self.pot(node.left, l)
        self.pot(node.right, l)

    def isSameTree(self, p, q):
        l1 = []
        l2 = []

        self.pot(p, l1)
        self.pot(q, l2)

        return l1 == l2
