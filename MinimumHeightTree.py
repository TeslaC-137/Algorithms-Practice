'''Minimal Height Tree:

Given a sorted array of integers construct a BST with minimum height'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
def minimumHeightTreeHelper(A, start, end):
    if end < start:
        return None
    mid = (start+end)//2
    node = TreeNode(A[mid])
    node.left = minimumHeightTreeHelper(A, start, mid-1)
    node.right = minimumHeightTreeHelper(A, mid+1, end)
    return node


def buildMinimumHeightTree(A):
    return minimumHeightTreeHelper(A, 0, len(A)-1)



    
    
