class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

    def _get_height(node: Node):
        if node is None:
            return -1
        else:
            return node.height
"""get() in avl tree"""
def _right_rotate(y: Node):
    # 步骤1：确定x和β
    x = y.left
    y.left = x.right  # 把x的右子树β，挂到y的左孩子位置
    # 步骤2：将y作为x的右孩子
    x.right = y
    # 步骤3：更新y和x的高度（先更新y，因为x的高度依赖y）
    y.height = max(AVL._get_height(y.left), AVL._get_height(y.right)) + 1  # y的新高度 = 左右子树最大高度 + 1
    x.height = max(AVL._get_height(x.left), AVL._get_height(x.right)) + 1  # x的新高度 = 左右子树最大高度 + 1
    return x
def _left_rotate(x: Node):
    # 步骤1：确定y和β
    y = x.right
    x.right = y.left  # 把y的左子树β，挂到x的右孩子位置
    # 步骤2：将x作为y的左孩子
    y.left = x
    # 步骤3：更新x和y的高度（先更新x，因为y的高度依赖x）
    x.height = max(AVL._get_height(x.left), AVL._get_height(x.right)) + 1  # x的新高度 = 左右子树最大高度 + 1
    y.height = max(AVL._get_height(y.left), AVL._get_height(y.right)) + 1  # y的新高度 = 左右子树最大高度 + 1
    return y
'''put in avl tree'''
def _put(x: AVL.Node):
    if x is None:
        return AVL.Node(key)
    elif key < x.key:
        x.left = _put(x.left)
    elif key > x.key:
        x.right = _put(x.right)
    # update the height
    x.height = max(AVL._get_height(x.left), AVL._get_height(x.right)) + 1
    # get the balance factor
    bf = AVL._get_balance_factor(x)
    if bf > 1 and key < x.left.key:  # case 1 三个全在左边
        return AVL._right_rotate(x)
    if bf < -1 and key > x.right.key:  # case 2 三个全在右边
        return AVL._left_rotate(x)
    if bf > 1 and key > x.left.key:  # case 3 三个先左后右
        x.left = AVL._left_rotate(x.left)
        return AVL._right_rotate(x)
    if bf < -1 and key < x.right.key:  # case 4 三个先右后左
        x.right = AVL._right_rotate(x.right)
        return AVL._left_rotate(x)
    return x