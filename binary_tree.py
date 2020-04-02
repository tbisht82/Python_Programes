class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)


def get_ancestors(r, target, ancestors):
    if r is None:
        return False
    if r.value == target:
        return True
    if get_ancestors(r.left, target, ancestors) or get_ancestors(r.right, target, ancestors):
        ancestors.append(r.value)
        return True
    return False


def find_common_parent(r, a, b):
    if a == b:
        print(a)
    elif a == r.value:
        print(a)
    elif b == r.value:
        print(b)
    else:
        a_ancestors = []
        get_ancestors(r, a, a_ancestors)
        b_ancestors = []
        get_ancestors(r, b, b_ancestors)

        common_parents = [i for i in a_ancestors if i in b_ancestors]

        if len(common_parents) >= 2:
            print(str(common_parents[1]) + ' and ' + str(common_parents[0]))
        else:
            print(common_parents[0])


tree = BinaryTree(2)
tree.root.left = Node(1)
tree.root.right = Node(3)
tree.root.right.left = Node(4)
tree.root.right.right = Node(5)
tree.root.right.right.right = Node(6)

find_common_parent(tree.root, 1, 5)
find_common_parent(tree.root, 3, 6)
find_common_parent(tree.root, 4, 6)
