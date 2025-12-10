class Node:
    def __init__(self, key,left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
class BST:
    def __init__(self):
        self.root = None
'''get()'''
def get(self, key):
    x = self.root
    while x is not None and key!= x.key:
        if key < x.key:
            x = x.left
        else:
            x = x.right
    return x
'''recursive_get()'''
def recursive_get(x, key): # x is the current node being searched,first node is the root
    if x is None or key == x.key:
        return x
    if key < x.key:
        return recursive_get(x.left, key)
    else:
        return recursive_get(x.right, key)
    '''put()'''
def put(self,key):
    Z = Node(key)
    x=root
    y=None
    while x is not None:
        y=x
        if Z.key<x.key:
            x=x.left
        else:
            x=x.right    #finding the last position of the path to insert the new node
    if y is None:
        self.root=Z
    elif Z.key<y.key:
        y.left=Z
    else:
        y.right=Z
'''recursive_put()'''
def recursive_put(x, key):
    if x is None:
        return Node(key)
    if key < x.key:
        x.left = recursive_put(x.left, key) #ifx.left is None, it will return Node(key)
    else:
        x.right = recursive_put(x.right, key)
    return x
'''size()'''
def size(root):
    if root is None:
        return 0
    return size(root.left) + 1 + size(root.right)
'''max()'''
def max(root):
    if root is None:
        return None
    while root.right is not None:
        root = root.right
    return root.key
'''recursive_max()'''
def recursive_max(x):
    if x.right is None:
        return x.key
    return recursive_max(x.right)
'''floor()'''
def floor(root, key):
    if root is None:
        return None
    if root.key == key:
        return root.key
    if key < root.key:
        return floor(root.left, key)
    t = floor(root.right, key)
    if t is not None: # if t is not None, it means the key is in the right subtree
        return t
    return root.key # if t is None, it means the key is not in the right subtree, so return the key of the current node
'''remove_min()'''
def _remove_min(x: Node):
    if x.left is None:
        return x.right
    x.left = BST._remove_min(x.left)
    return x # return the new root of the subtree
'''remove()'''
def remove(self, key):
    def _remove(x: BST.Node):
        if x is None:
            return None
        if key < x.key:
            x.left = _remove(x.left)
        elif key > x.key:
            x.right = _remove(x.right)
        else:
            if x.right is None:
                return x.left
            if x.left is None:
                return x.right
            t = x # save the node to be removed
            x = BST._min(t.right) # let x be the minimum node in the right subtree
            x.right = BST._remove_min(t.right) # add the right subtree of t without the minimum node
            x.left = t.left # add the left subtree
        return x
    self._root = _remove(self._root)