from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        q = []
        depth = 0
        q.append(root)

        while len(q) > 0:
            size = len(q)
            for i in range(size):
                currNode = q.pop()
                if currNode.left != None:
                    q.append(currNode.left)
                if currNode.right != None:
                    q.append(currNode.right)

            depth += 1

        return depth
