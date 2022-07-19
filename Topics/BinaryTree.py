# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    #104 Max depth of binary tree
    # create a variable to count the depth of the tree
def maxDepth(self, root: [TreeNode]):
    # DFS

    # Handle the case where there is not tree node
    if not root:
        return 0
    # count sum of left side of the tree
    left = 1 + self.maxDepth(root.left)
    # count sum of right side of the tree
    right = 1 + self.maxDepth(root.right)
    # return the max depth
    return max(left, right)
        

print(maxDepth([3,9,20,None,None,15,7]))


# O(n^2) solution
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#       first number of preorder is always going to be the root
#       first number of inorder is the left children...check where root locate  
                
        if not preorder or not inorder: # base case
            return None
        root = TreeNode(preorder[0])
        r_index = inorder.index(preorder[0])         # O(n) search
        root.left = self.buildTree(preorder[1:r_index+1], inorder[:r_index])     # O(n) recursive call
        root.right = self.buildTree(preorder[r_index+1:], inorder[r_index+1:])     
        return root

# O(n) solution
# create hash map for inorder to find index position of each element
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        _lookup = {}
        for i, num in enumerate(inorder):
            _lookup[num] = i
        
        i = 0
        def helper(l, r):
            if l > r:
                return None
            nonlocal i # i is the index of the new root
            v = preorder[i]
            root = TreeNode(v)
            i += 1 # keeps traverse over preorder list
            inorder_index = _lookup[v]
            root.left = helper(l, inorder_index-1)
            root.right = helper(inorder_index+1, r)
            
            return root
        
        return helper(0, len(preorder)-1)
            

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
# negative value can be in the path
# for all positive nodes, we can't add everything up and be done
    # because each node can only traverse once
    # how you split the node is important
    # only 1 split is allowed
# solve sub problem first
# DFS
# O(n)
        res = 0
        def dfs(root):
            if not root:
                return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            # handle negative value
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
        
            # if split
            maxSum_split = root.val + leftMax + rightMax
            # if not
            maxSum_path = root.val + max(leftMax, rightMax)

            global res
            # update split result
            res = max(maxSum_split, res)

            # because only 1 split is allowed, when return the value 
            # to previous level, only return max path not split value
            return maxSum_path 
            
        dfs(root)
        return res



class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS? need to check each route
        # output: num of good nodes
        # starting with root
        # 1 + helper()
        # helper return 1/0
        # helper(node, curMax, )
        
        def helper(node, curMax):
            if not node:
                return 0
            # compare the node with curMax
            # curMax = max(node, curMax)
            curMax = max(node.val, curMax)
            left = helper(node.left, curMax)
        # left = helper
        # right = helper
            right = helper(node.right, curMax)
            if curMax <= node.val:
                return 1+left+right
            else:
                return 0+left+right
        return helper(root, root.val)

class Solution:
	lastNode = None
	
	def flatten(self, root):
		if not root:
			return
		if self.lastNode:
			self.lastNode.left = None
			self.lastNode.right = root

		self.lastNode = root    # update the last node to the current node
		self.flatten(root.left)
		self.flatten(root.right)


def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root:
        return None
    if root == p or root == q: # whenever you find the match # we want earliest level as ancestor
        return root
    
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    
    if left and right:
        return root
    if left:
        return left
    if right:
        return right
    
    return None