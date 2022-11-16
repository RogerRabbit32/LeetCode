# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = [[root]]
        while res[-1]:
            _arr = []
            for n in res[-1]:
                if n.left:
                    _arr.append(n.left)
                if n.right:
                    _arr.append(n.right)
            res.append(_arr)
        return [[i.val for i in j] for j in res[:-1]]
                