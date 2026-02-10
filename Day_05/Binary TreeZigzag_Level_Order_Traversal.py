# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []

        queue = deque([root])   # for level order traversal
        result = []
        left_to_right = True    # direction flag

        while queue:
            level = []
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # reverse level if direction is right to left
            if not left_to_right:
                level.reverse()

            result.append(level)
            left_to_right = not left_to_right  # change direction

        return result
