# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoursiveSearch(self, root: Optional[Treenode], l: List[int]) -> List[int]:
        if not root:
            return l

        l = self.recoursiveSearch(root.left, l)
        l.append(root.val)
        l = self.recoursiveSearch(root.right, l)

        return l
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        l = self.recoursiveSearch(root, [])

        for i in range(len(l)-1):
            if l[i] >= l[i+1]:
                return False
        
        return True

    


        