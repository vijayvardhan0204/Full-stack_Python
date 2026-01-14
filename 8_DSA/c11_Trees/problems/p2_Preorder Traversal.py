# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root):
    if not root:
        return []

    stack = [root]
    res = []

    while stack:
        node = stack.pop()
        res.append(node.val)

        # Push right first so left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return res


# ---------- Build Example Tree ----------
# Tree structure:
#            1
#          /   \
#         2     3
#        / \     \
#       4   5     8
#          / \   /
#         6   7 9

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)

root.right.right = TreeNode(8)
root.right.right.left = TreeNode(9)

# ---------- Run Traversal ----------
print(preorderTraversal(root))
