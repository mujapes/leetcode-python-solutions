"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        depth = 0
        for d in root.children:
            depth = max(depth, self.maxDepth(d))
        return depth + 1

# Runtime: 43 ms, Beats 89.52%
# Memory: 20.86 MB, Beats 65.78%
