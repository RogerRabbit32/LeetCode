# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:        
        layer = [[root.left], [root.right]]
        while any(layer[0]) or any(layer[1]):
            _layer = [[],[]]
            
            for i in [0,1]:
                for n in layer[i]:
                    if n:
                        _layer[i].extend([n.left, n.right])
                    else:
                        _layer[i].extend([None, None]) 
            
            for i in range(len(layer[0])):
                l = layer[0][-i-1].val if layer[0][-i-1] else None
                r = layer[1][i].val if layer[1][i] else None
                
                if l!=r:
                    return False
                  
            layer = [i for i in _layer]
            
        return True
    