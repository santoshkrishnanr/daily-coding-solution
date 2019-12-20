"""
This problem was asked by Google.
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
For example, given the following Node class
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    string = []
    def preorder(root):
        if root is None:
            string.append('-')
            return
        string.append(str(root.val))
        preorder(root.left)
        preorder(root.right)
    preorder(root)
    return ' '.join(string)

def deserialize(string):
    def preorder(iterator):
        val = next(iterator)
        if val == '-':
            return None
        root = Node(int(val))
        root.left = preorder(iterator)
        root.right = preorder(iterator)
        return root
    iterator = iter(string.split(' '))
    return preorder(iterator) 

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

binaryTree = Node(1, Node(2, Node(3)), Node(4))
serializedResult = serialize(binaryTree)
print(serializedResult)
deserializedTree = deserialize(serializedResult)
inorder(deserializedTree)