__author__ = 'WangZhe'


class Node:
    __slots__ = 'val', 'left', 'right', 'level', 'state'

    def __init__(self, val):
        self.val = int(val)
        self.left = None
        self.right = None
        self.level = 0
        self.state = 0

    def __str__(self):
        return str(self.val)


class BST:

    def __init__(self, serialization):
        if len(serialization) == 0:
            self.root = None
        else:
            self.root = self.build_tree(serialization)

    def BST_legal(self):
        return self._BST_legal(self.root)

    def _BST_max(self, root):
        if root is None:
            return -float('inf')
        elif root.left is None and root.right is None:
            return root.val
        else:
            return max(self._BST_max(root.left), root.val, self._BST_max(root.right))

    def _BST_min(self, root):
        if root is None:
            return float('inf')
        elif root.left is None and root.right is None:
            return root.val
        else:
            return min(self._BST_min(root.left), root.val, self._BST_min(root.right))

    def _BST_legal(self, root):
        if root is None:
            return True
        elif root.left is None and root.right is None:
            return True
        elif root.left is None:
            right_min = self._BST_min(root.right)
            if root.val < right_min:
                return self._BST_legal(root.right)
            else:
                return False
        elif root.right is None:
            left_max = self._BST_max(root.left)
            if root.val > left_max:
                return self._BST_legal(root.left)
            else:
                return False
        else:
            left_max = self._BST_max(root.left)
            right_min = self._BST_min(root.right)
            if left_max < root.val < right_min:
                return self._BST_legal(root.left) and self._BST_legal(root.right)
            else:
                return False



    def build_tree(self, serialization):
        # serialization = [1,2,3,#,#,4,#,#,5]
        current_level = 0
        current_index = 0
        root = Node(serialization[0])
        each_level = {0: [root]}
        it = 1

        while it < len(serialization):
            i = serialization[it]
            current_node = each_level[current_level][current_index]

            if current_index == len(each_level[current_level]) - 1 and current_node.state == 2:
                current_level += 1
                current_index = 0

            elif i == '#' and (current_node.state == 0 or current_node.state == 1):
                current_node.state += 1
                it += 1

            elif current_node.state == 2:
                current_index += 1

            elif current_node.state == 0:
                current_node.left = Node(i)
                current_node.left.level = current_node.level + 1
                current_node.state = 1
                if each_level.get(current_node.level + 1) is None:
                    each_level[current_node.level + 1] = [current_node.left]
                else:
                    each_level[current_node.level + 1].append(current_node.left)
                it += 1

            elif current_node.state == 1:
                current_node.right = Node(i)
                current_node.right.level = current_node.level + 1
                current_node.state = 2
                if each_level.get(current_node.level + 1) is None:
                    each_level[current_node.level + 1] = [current_node.right]
                else:
                    each_level[current_node.level + 1].append(current_node.right)
                it += 1
        return root




if __name__ == '__main__':
    print(BST(['-12','#','85','57']).BST_legal())


